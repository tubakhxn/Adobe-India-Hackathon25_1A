import pdfplumber
import os
import json
import re
from collections import Counter

def clean_text(text):
    """
    Removes CID font encoding artifacts like '(cid:123)' from a string,
    but preserves the original string if it consists only of such artifacts.
    """
    if not isinstance(text, str):
        return ""
    
    # Create a version of the text with CIDs removed.
    # Also remove any extra whitespace that might be left.
    cleaned = re.sub(r'\(cid:\d+\)', '', text).strip()
    
    # If cleaning the string makes it empty, it means the original was composed
    # entirely of CID artifacts. In that case, we return the original string
    # to indicate that some content was present, even if unreadable.
    if not cleaned:
        return text.strip()
    
    # Otherwise, return the version with CIDs removed.
    return cleaned

def detect_headings(lines, font_stats):
    outline = []
    for item in lines:
        txt = clean_text(item['text'])
        if not txt or len(txt) < 2:
            continue
        size = item['size']
        bold = item['bold']
        bbox = item['bbox']
        page_num = item['page_num']
        # Heading detection: size-based + bold + positional cues
        if size >= font_stats['h1']:
            outline.append({'level': 'H1', 'text': txt, 'page': page_num})
        elif size >= font_stats['h2']:
            outline.append({'level': 'H2', 'text': txt, 'page': page_num})
        elif size >= font_stats['h3']:
            outline.append({'level': 'H3', 'text': txt, 'page': page_num})
    return outline

def extract_tables(pdf):
    tables_info = []
    for i, page in enumerate(pdf.pages, 1):
        # find_tables() returns a list of Table objects
        found_tables = page.find_tables()
        for t_idx, table in enumerate(found_tables):
            header = None
            # The .extract() method returns the table's text as a list of lists (rows and cells)
            extracted_table = table.extract()
            
            # Check if the table was extracted successfully and has at least one row
            if extracted_table and len(extracted_table) > 0:
                header_row = extracted_table[0] # The first row is a list of cell strings
                # Clean the text of each cell and join the non-empty ones to form a header title
                cleaned_cells = [clean_text(str(cell)) for cell in header_row if cell is not None]
                header = " | ".join([cell for cell in cleaned_cells if cell])
            
            # Use the extracted header as the title, or a default "Table X"
            title = f"Table {t_idx + 1}" if not header else header
            tables_info.append({'level': 'Table', 'text': title.strip(), 'page': i})
    return tables_info

def extract_title(pdf):
    # Use largest text on first page as title
    page = pdf.pages[0]
    words = page.extract_words(extra_attrs=['size', 'fontname'])
    if not words:
        return ""
    largest = max(words, key=lambda w: float(w["size"]))
    return clean_text(largest["text"])

def stats_from_fonts(words):
    sizes = [float(w['size']) for w in words]
    if len(sizes) == 0:
        return {'h1': 18, 'h2': 16, 'h3': 14}
    common_sizes = Counter(sizes).most_common()
    largest = common_sizes[0][0]
    sizes_sorted = sorted(list(set(sizes)), reverse=True)
    return {
        'h1': sizes_sorted[0],
        'h2': sizes_sorted[1] if len(sizes_sorted) > 1 else sizes_sorted[0] - 2,
        'h3': sizes_sorted[2] if len(sizes_sorted) > 2 else sizes_sorted[0] - 4,
    }

def process_pdf(input_path, output_path=None):
    with pdfplumber.open(input_path) as pdf:
        outline = []
        all_words = []
        for i, page in enumerate(pdf.pages, 1):
            words = page.extract_words(extra_attrs=['size', 'fontname'])
            for w in words:
                all_words.append({'text': w['text'], 'size': float(w['size']),
                                  'bold': "Bold" in w['fontname'], 'page_num': i,
                                  'bbox': (w['x0'], w['top'], w['x1'], w['bottom'])})

        font_stats = stats_from_fonts(all_words)
        outline += detect_headings(all_words, font_stats)
        tables = extract_tables(pdf)
        outline += tables

        title = extract_title(pdf)
        res = {'title': title, 'outline': outline}
        if output_path:
            with open(output_path, 'w', encoding='utf-8') as f:
                json.dump(res, f, ensure_ascii=False, indent=2)
        return res

def batch_process_pdfs(input_dir, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    for fn in os.listdir(input_dir):
        if not fn.lower().endswith('.pdf'):
            continue
        input_path = os.path.join(input_dir, fn)
        output_path = os.path.join(output_dir, os.path.splitext(fn)[0] + '.json')
        process_pdf(input_path, output_path)

import argparse
import os
from extractor import process_pdf, batch_process_pdfs
from webapp import start_web

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--web', action='store_true', help='Run in web server mode')
    args = parser.parse_args()

    if args.web:
        start_web()
    else:
        # Get the absolute path of the directory where this script is located
        script_dir = os.path.dirname(os.path.abspath(__file__))
        
        # Join the script's directory path with the input/output folder names
        # This makes sure the script finds folders in the right place (e.g., ps-1a/app/input)
        in_dir = os.path.join(script_dir, 'input')
        out_dir = os.path.join(script_dir, 'output')
        
        # Check if the input directory exists before processing
        if not os.path.isdir(in_dir):
            print(f"Error: Input directory '{in_dir}' not found.")
            print(f"Please make sure the 'input' folder is in the same directory as the script.")
        else:
            print(f"Processing PDFs from '{in_dir}'...")
            batch_process_pdfs(in_dir, out_dir)
            print(f"Processing complete. Check the '{out_dir}' folder for results.")

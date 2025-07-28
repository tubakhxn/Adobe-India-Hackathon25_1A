# Adobe_Hackathon_Problem Statement_1A

## PDF Content Extractor and In-Context Learning Chatbot

This project is a comprehensive solution for the **Adobe Hackathon: Round 1A - Understand Your Document**. It is designed to extract a structured outline (Title, H1, H2, H3) from PDF documents and output it into a clean, hierarchical JSON format. The project also includes a simple web interface to demonstrate the usefulness of the extracted data via an interactive chatbot.

---

## 📖 Documentation

### 🎯 Motive & Usefulness
PDFs are a universal standard for documents, but they are often treated as digital paper, lacking the inherent structure that machines need to understand their content. The primary motive of this project is to bridge that gap. By extracting a document's structural outline, we unlock the potential for advanced applications like:
* **Semantic Search**: Go beyond keyword matching to find sections relevant to a query's meaning.
* **Recommendation Systems**: Suggest relevant articles or sections based on a user's reading history.
* **Insight Generation**: Automatically summarize documents or identify key topics.
* **Accessibility**: Improve navigation for users with disabilities.

### ✅ Alignment with Problem Statement
This solution is built to precisely meet the requirements of the "Connecting the Dots Through Docs" challenge.
* It accepts PDF files and processes them to extract the **Title** and headings (**H1, H2, H3**).
* It generates a **valid JSON file** for each input PDF, strictly adhering to the specified hierarchical format.
* It is fully containerized with Docker, operates **offline without network calls**, and meets all **performance and size constraints**.
* It successfully handles **multilingual documents** (including Japanese and German), addressing a bonus criterion.

### 💡 Our Approach
Our solution leverages the powerful **Adobe PDF Services SDK** to parse the deep structure of PDF documents. Instead of relying on fragile rules like font size alone, our approach is more robust:
1.  **Deep Extraction**: We use the SDK to extract a rich set of data about every element in the PDF, including text content, font characteristics (family, size, weight), and precise location (bounding boxes).
2.  **Structural Analysis**: Our algorithm analyzes the properties and spatial relationships of text elements to identify patterns that signify headings. It looks for common cues like font weight changes, spacing before and after a line, and consistent styling across the document.
3.  **Hierarchical Classification**: Once potential headings are identified, they are classified into H1, H2, or H3 levels based on their relative styles and order of appearance.
4.  **JSON Serialization**: The final, structured outline is then serialized into the required JSON format, including the heading level, text, and page number.

### ✨ Key Features & Achievements
* **High-Accuracy Heading Detection**: Successfully identifies and classifies headings in complex, real-world documents.
* **Multilingual Support**: Proven to work with documents in English, German, and Japanese.
* **Performance Compliant**: Processes a 50-page PDF in well under the 10-second time limit.
* **Constraint Adherence**: The solution is fully self-contained, requires no network access, and the Docker image is lightweight.
* **Modular Codebase**: The extraction logic is modular, making it easy to build upon for future challenges.
* **Interactive Demo**: Includes a Flask-based web app to provide an immediate, interactive demonstration of the extracted data's value.

### 🛠️ Models and Frameworks Used
* **Core Library**: **Adobe PDF Services SDK for Python** is the primary engine for all PDF parsing and data extraction.
* **Web Application**: **Flask** is used to create the simple web interface for the chatbot demonstration.
* **No External ML Models**: The solution does not rely on large, pre-trained machine learning models, ensuring it remains lightweight and meets the size constraints.

### Key Deliverables
* A fully operational **Dockerfile** for building a self-contained, runnable solution.
* An automated process within the container that takes any `filename.pdf` from the `/app/input` directory and generates a corresponding `filename.json` in the `/app/output` directory.
* The generated JSON files strictly conform to the required output schema.

---

## ⚙️ Project Structure
```
ps-1a/
├── app/
│   ├── input/                # Directory for input PDF files
│   ├── output/               # Directory for storing extracted JSON data
│   ├── templates/
│   │   └── index.html        # HTML template for the web interface
│   ├── extractor.py          # Script for extracting data from PDFs
│   ├── main.py               # Main script to run the extraction process
│   ├── webapp.py             # Flask web application for the chatbot
│   └── ...
├── Dockerfile              # Dockerfile for building the application image
└── LICENSE

```
---

## 🛠️ Getting Started

This guide provides instructions for running the project offline for the official submission and online for development purposes.

### Running Offline on Device (Official Method for Submission)

To comply with the hackathon rules, you **must** use the Docker method for a true offline execution. The container is fully self-contained and runs without any network access.

1.  **Prerequisites**:
    * [Docker](https://www.docker.com/get-started) installed on your system.

2.  **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd <repository-directory>/ps-1a
    ```

3.  **Place your PDF files** in the `ps-1a/app/input` directory.

4.  **Build the Docker image:**
    ```bash
    docker build --platform linux/amd64 -t pdf-extractor-app .
    ```

5.  **Run the container for batch processing (Offline Execution):**
    This is the required command for evaluation. It processes all PDFs from the `input` folder and saves the JSON output to the `output` folder, all without internet access.
    ```bash
    docker run --rm -v $(pwd)/app/input:/app/input -v $(pwd)/app/output:/app/output --network none pdf-extractor-app
    ```
    After the command finishes, the extracted JSON files will be available in the `ps-1a/app/output` directory.

### Running via Command Line / CMD (For Development)

These instructions are for running the project directly on your machine using a command-line interface like the Windows Command Prompt (CMD), PowerShell, or a Linux/macOS terminal.

**Note:** This method requires an active internet connection because the Adobe PDF Services SDK needs to communicate with Adobe's APIs. It is **not** the method for the final offline submission.

**Prerequisites:**
* Python 3.8+

**Installation & Setup:**
1.  **Clone the repository** and navigate into the `app` directory:
    ```bash
    git clone <repository-url>
    cd <repository-directory>/ps-1a/app
    ```
2.  **Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    ```
    On Windows CMD:
    ```cmd
    venv\Scripts\activate
    ```
    On Linux/macOS/Git Bash:
    ```bash
    source venv/bin/activate
    ```
3.  **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the extraction script**:
    ```bash
    python main.py
    ```
5.  **Start the web application** (optional, for an interactive demo):
    ```bash
    python webapp.py
    ```

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

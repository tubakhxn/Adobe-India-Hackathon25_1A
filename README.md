# Adobe_Hackathon_Problem Statement_1A

## PDF Content Extractor and In-Context Learning Chatbot

This project is designed to extract text and table data from PDF documents and provide a user-friendly web interface to interact with the extracted information using an in-context learning chatbot. The application supports processing multiple PDF files, including those in different languages like German and Japanese.

## 🚀 Features

* **PDF Data Extraction**: Extracts text and tables from PDF files using Adobe PDF Services.
* **Multi-language Support**: Can process PDFs in various languages (tested with English, German, and Japanese).
* **In-Context Learning Chatbot**: A web-based chatbot that allows users to ask questions about the content of the processed PDFs.
* **Simple Web Interface**: An intuitive and easy-to-use web interface for uploading PDFs and interacting with the chatbot.
* **Flexible Deployment**: Can be run easily using Docker or directly from the command line.

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
## 🛠️ Getting Started

You can run this project either using Docker (recommended for ease of use) or by setting it up locally on the command line.

### Option 1: Running with Docker

This is the simplest way to get the application running.

**Prerequisites:**
* [Docker](https://www.docker.com/get-started) installed on your system.

**Installation & Running:**
1.  **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd <repository-directory>/ps-1a
    ```
2.  **Place your PDF files** in the `ps-1a/app/input` directory.
3.  **Build the Docker image:**
    ```bash
    docker build -t pdf-extractor-app .
    ```
4.  **Run the Docker container:**
    ```bash
    docker run -p 5000:5000 pdf-extractor-app
    ```
    This command will automatically run the extraction script and then start the web server. The application will be accessible at `http://localhost:5000`.

### Option 2: Running from the Command Line (CLI)

This method gives you more control over the individual components.

**Prerequisites:**
* Python 3.8+
* Adobe PDF Services API credentials. You can get free credentials [here](https://developer.adobe.com/document-services/docs/overview/pdf-services-api/credentials/).

**Installation & Setup:**
1.  **Clone the repository** and navigate into the `app` directory:
    ```bash
    git clone <repository-url>
    cd <repository-directory>/ps-1a/app
    ```
2.  **Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```
3.  **Create a `requirements.txt` file** with the following content:
    ```
    adobe-pdfservices-sdk
    flask
    openai
    python-dotenv
    ```
4.  **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
5.  **Set up your credentials.** Create a file named `.env` in the `ps-1a/app` directory and add your Adobe PDF Services credentials:
    ```
    PDF_SERVICES_CLIENT_ID=<YOUR_CLIENT_ID>
    PDF_SERVICES_CLIENT_SECRET=<YOUR_CLIENT_SECRET>
    ```

## 🖥️ How to Use

The usage depends on whether you are running via Docker or CLI.

### If using Docker:
Simply navigate to `http://localhost:5000` in your browser after running the container. The PDFs in the `input` folder will be processed automatically.

### If using the CLI:
You need to run the extraction and the web app in two separate steps from inside the `ps-1a/app` directory.

1.  **Place your PDF files** in the `ps-1a/app/input` directory.

2.  **Run the extraction script**:
    ```bash
    python main.py
    ```
    This will process the PDFs and create JSON files in the `ps-1a/app/output` directory.

3.  **Start the web application**:
    ```bash
    python webapp.py
    ```
    The application will now be accessible at `http://localhost:5000`.

4.  **Interact with the Chatbot**:
    * Open your browser and go to `http://localhost:5000`.
    * Ask questions related to the content of the processed PDFs. The chatbot uses the generated JSON files as its knowledge base.

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.



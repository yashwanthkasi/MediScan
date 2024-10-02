# Medical Report Analyzer

Medical Report Analyzer is a web-based application that allows users to upload medical reports (PDFs or images) and provides detailed analysis using AI. The system extracts text from the reports and analyzes them via a Large Language Model (LLM) powered by Langchain-Grop, offering insights, explanations, and answers to follow-up questions.

## Features

- **File Upload**: Upload medical reports in PDF or image formats for analysis.
- **Text Extraction**: Extracts text from medical reports using `PyPDF2` for PDFs and `pytesseract` for images.
- **AI-Powered Analysis**: Uses Langchain-Grop to analyze the extracted text and provide detailed explanations.
- **Interactive Q&A**: Ask follow-up questions about the medical report, and the AI will provide relevant answers.
- **User-Friendly Interface**: Built with Streamlit for a smooth and simple user experience.

## Technologies Used

- **Streamlit**: Frontend framework for building web applications.
- **Langchain-Grop**: Backend for AI language model interactions.
- **PyPDF2**: For PDF text extraction.
- **pytesseract**: For extracting text from images.
- **Python**: The main programming language for backend logic.

## Setup Instructions

### 1. Clone the Repository

First, clone the repository to your local machine:

```bash
git clone https://github.com/yourusername/medical-report-analyzer.git
cd medical-report-analyzer
```

### 2. Set Up a Virtual Environment (Optional but Recommended)

It's a good practice to use a virtual environment to manage your dependencies.

```bash
# Create a virtual environment
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate  # On macOS/Linux
# .\venv\Scripts\activate  # On Windows
```

### 3. Install Dependencies

Install the required dependencies listed in the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

### 4. Create a `.env` File

Create a `.env` file in the root directory of the project and add your **Langchain-Grop** API key:

```bash
touch .env
```

Inside the `.env` file, add the following line:

```bash
GROP_API_KEY=your-api-key-here
```

Replace `your-api-key-here` with your actual API key for Langchain-Grop.

### 5. Run the Application

To start the application, run the following command:

```bash
streamlit run app.py
```

Once the server starts, open your browser and navigate to `http://localhost:8501` to interact with the application.

## Usage

1. **Upload a File**: Click on the "Upload" button and select a medical report (PDF or image).
2. **View Analysis**: After uploading, the system will automatically extract the text and provide a detailed analysis.
3. **Ask Questions**: Use the input box to ask follow-up questions related to the report, and the AI will provide detailed responses.

## Project Structure

```
/medical-report-analyzer
├── /core              # Core logic
├── /models            # Data models
├── /services          # LLM and file processing services
├── app.py             # Streamlit app entry point
├── requirements.txt   # List of dependencies
├── .env               # Environment variables (not in repo)
├── .gitignore         # Git ignore file
├── README.md          # Project documentation
```

## Contributing

If you’d like to contribute to this project, please fork the repository and submit a pull request. For any issues or suggestions, feel free to open an issue on GitHub.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

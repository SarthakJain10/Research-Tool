# Research Paper Summarizer

A **Streamlit web app** for summarizing and explaining key AI research papers using the power of LangChain and Google Gemini models. Select a paper, choose your explanation style and length, and get concise, tailored summaries perfect for all audiences.

## Features

- **User-friendly interface:** Built with Streamlit for easy interaction.
- **Multiple explanation styles:** Choose from Beginner-Friendly, Technical, Code-Oriented, or Mathematical.
- **Custom summary lengths:** Pick short, medium, or detailed explanations.
- **Powered by Gemini:** Utilizes Google Gemini models via LangChain for high-quality AI-generated content.
- **Secure API key management:** Uses Streamlit secrets for sensitive credentials.

## Getting Started

### Prerequisites

- Python 3.8 or above
- Google Gemini API access

### Installation

1. **Clone the repository:**
    ```bash
    git clone 
    cd 
    ```

2. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3. **Configure secrets:**
    - Create a file at `.streamlit/secrets.toml` and add your Google API key:
      ```
      GOOGLE_API_KEY = "your-google-api-key-here"
      ```

### Running the App

```bash
streamlit run .py
```
Replace `.py` with the filename containing your Streamlit code.

## Usage

1. **Select a research paper** from the dropdown.
2. **Choose your preferred explanation style** (e.g., Beginner-Friendly).
3. **Set the explanation length** (Short, Medium, Long).
4. **Click "Summarize"** to generate your custom summary.

## File Structure

| File/Folder               | Description                                  |
|---------------------------|----------------------------------------------|
| `main.py`                 | Main Streamlit application script            |
| `requirements.txt`        | Python dependencies                          |
| `.gitignore`              | Files and folders to exclude from Git        |
| `.streamlit/secrets.toml` | API keys and secrets (not committed)         |
| `template.json`           | Prompt template for LangChain (customizable) |

## Customization

- **Add more papers:** Edit the list in the `paper_input` dropdown.
- **Modify explanation styles:** Update the `style_input` options.
- **Change prompt templates:** Edit `template.json` to fit your needs.

## License

This project is licensed under the **MIT License**. You are free to use, modify, and distribute this software, provided you include the original copyright and license.

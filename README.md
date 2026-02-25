# UPSC Agentic Question Generator

## Project Purpose
This project is a multi-agent system designed to generate high-quality, exam-oriented questions (specifically for UPSC/State PSC exams) from raw news articles. It leverages **CrewAI** to orchestrate four specialized agents that analyze the article, mine patterns from Previous Year Questions (PYQs), generate questions, and perform quality control.

## Features
- **Sequential Workflow**: Ensures a logical flow from analysis to generation to validation.
- **PYQ Pattern Mining**: Uses RAG (Retrieval Augmented Generation) to learn from actual past papers (PDFs).
- **Custom Agents**:
  - **Article Analyzer**: Extracts facts and themes.
  - **PYQ Pattern Miner**: Identifies question styles and directive verbs.
  - **Question Generator**: Creates questions combining article content and PYQ styles.
  - **Quality Controller**: Filters and polishes the final output.

## Folder Structure
```
crewai_exam_generator/
├── data/                   # Place your PYQ PDFs here
│   ├── pyq_1.pdf
│   ├── pyq_2.pdf
│   └── ...
├── src/
│   ├── agents.py           # Agent definitions
│   ├── tasks.py            # Task definitions
│   └── __init__.py
├── main.py                 # Entry point script
├── requirements.txt        # Python dependencies
├── .env.example            # Environment variables template
└── README.md               # This file
```

## How to Run

1.  **Prerequisites**:
    - Python 3.10+ installed.
    - [Ollama](https://ollama.com/) installed and running.
    - Pull the model: `ollama pull llama3.2`

2.  **Setup**:
    ```bash
    # Clone or navigate to the project directory
    cd crewai_exam_generator

    # Install dependencies
    pip install -r requirements.txt
    ```

3.  **Configuration**:
    - Ensure Ollama is running (`ollama serve`).
    - The system is pre-configured to use `llama3.2`.


4.  **Execution**:
    ```bash
    python main.py

    #For interface
    streamlit run streamlit_app.py
    ```
    - The script will prompt you to paste a news article.
    - Press Enter twice to submit the text.
    - The agents will start working and print their progress.

## Input/Output Format

- **Input**: Raw text of a news article (e.g., from The Hindu, Indian Express).
- **Output**: A list of 5-8 numbered questions, formatted for an exam paper.

## Technical Details
- **Framework**: CrewAI
- **Embeddings**: Uses OpenAI Embeddings (via CrewAI's default) or FAISS/Chroma for the PDF search tool.
- **PDF Processing**: Uses `crewai_tools.PDFSearchTool` to read and index PYQs.

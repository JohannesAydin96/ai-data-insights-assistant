# AI Data Insights Assistant

An AI-powered data analysis application that allows users to upload a CSV file, explore the dataset, generate insights, and ask questions about the data.

The system combines data processing, SQL-based analysis, and language models to produce structured insights and natural language answers.

---

## Project Overview

This project demonstrates how to build an AI-assisted data analysis tool that integrates traditional data processing with modern language models.

Instead of relying solely on manual analysis, the application processes structured data using Pandas and SQL (DuckDB), then uses a language model to generate insights and answer questions based on the dataset.

The system follows a pipeline where raw data is transformed into structured summaries, which are then used as context for AI-generated insights.

---

## Features

- Upload and analyze CSV datasets  
- Automatic data profiling (rows, columns, missing values)  
- SQL-based aggregations using DuckDB  
- AI-generated insights based on dataset statistics  
- Natural language question answering over the dataset  
- Interactive web interface built with Streamlit  

---

## Tech Stack

- Python  
- Pandas  
- DuckDB  
- OpenAI API  
- Streamlit  
- python-dotenv  

---

## How It Works (Architecture)

The application follows a structured data analysis pipeline:

1. The user uploads a CSV file  
2. The dataset is loaded into Pandas  
3. Data profiling generates summary statistics  
4. SQL queries (DuckDB) perform aggregations  
5. Structured summaries are combined  
6. The language model generates insights or answers  
7. Results are displayed in the Streamlit interface  

```markdown
### Pipeline Overview

CSV → Pandas Processing → SQL (DuckDB) → Combined Summary → LLM → Insights / Answers
Project Structure
ai-data-insights-assistant/
│
├── app.py                 # Streamlit UI (entry point)
├── README.md              # Project documentation
├── requirements.txt       # Project dependencies
├── .env                   # API key (not committed)
│
├── data/
│   └── raw/
│       └── superstore.csv # Example dataset
│
└── src/
    ├── data_loader.py         # Loads CSV into Pandas
    ├── data_profiler.py       # Generates dataset summaries
    ├── sql_engine.py          # Executes SQL queries (DuckDB)
    ├── ai_insights.py         # Generates AI insights
    └── question_answering.py  # Handles Q&A over data
File Responsibilities
app.py
Handles the user interface, file upload, and result display.
data_loader.py
Loads CSV data into a Pandas DataFrame.
data_profiler.py
Generates dataset statistics such as rows, columns, missing values, and summaries.
sql_engine.py
Executes SQL queries on the dataset using DuckDB.
ai_insights.py
Generates insights based on structured summaries using the OpenAI API.
question_answering.py
Handles natural language questions over the dataset.
How to Run
1. Clone the repository
git clone https://github.com/your-username/ai-data-insights-assistant.git
cd ai-data-insights-assistant
2. Create and activate a virtual environment

Windows:

python -m venv .venv
.venv\Scripts\activate
3. Install dependencies
pip install -r requirements.txt
4. Add your OpenAI API key

Create a .env file in the root directory and add:

OPENAI_API_KEY=your_api_key_here
5. Run the app
streamlit run app.py
Example Usage
Upload a CSV dataset (e.g., sales data).
Wait for the dataset to be processed.
Ask questions such as:
"Which category has the highest sales?"
"Which region performs best?"
"Are there missing values in the dataset?"
The system will:
Analyze the dataset
Generate insights
Provide answers based on the data

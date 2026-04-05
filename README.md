# AI Data Insights Assistant

An interactive data analysis tool that allows users to upload a CSV file, explore the dataset, generate AI-powered insights, and ask questions about the data.

Built with Python, Pandas, SQL (DuckDB), OpenAI, and Streamlit.

---

## Features

- Upload and analyze CSV datasets
- Automatic data profiling (rows, columns, missing values)
- SQL-based aggregation using DuckDB
- AI-generated insights based on dataset statistics
- Natural language Q&A over your data
- Interactive web interface with Streamlit

---

## Tech Stack

- Python
- Pandas
- DuckDB
- OpenAI API
- Streamlit
- python-dotenv

---

## How It Works

1. Upload CSV file  
2. Data is processed using Pandas  
3. SQL queries run via DuckDB  
4. AI generates insights  
5. Users can ask questions about the dataset  

---

## How It Works (Architecture)

The application follows a structured data analysis pipeline:

1. The user uploads a CSV file  
2. The dataset is loaded into Pandas for processing  
3. Basic statistics and summaries are generated  
4. SQL queries (DuckDB) are executed for aggregations  
5. AI receives both Pandas and SQL summaries  
6. The model generates insights or answers based on the data  
7. Results are displayed in the Streamlit interface  

### Pipeline Overview


CSV File
↓
Pandas Processing (Profiling)
↓
SQL Aggregation (DuckDB)
↓
Combined Summary
↓
LLM (OpenAI API)
↓
Insights / Answers


---

## Project Structure


ai-data-insights-assistant/
│
├── app.py # Streamlit UI (entry point)
├── README.md # Project documentation
├── requirements.txt # Project dependencies
├── .env # API key (not committed)
│
├── data/
│ └── raw/
│ └── superstore.csv # Example dataset
│
├── src/
│ ├── data_loader.py # Loads CSV into Pandas
│ ├── data_profiler.py # Generates dataset summaries
│ ├── sql_engine.py # Runs SQL queries with DuckDB
│ ├── ai_insights.py # Generates AI insights
│ └── question_answering.py # Handles Q&A over data


---

## File Responsibilities

- app.py  
  Handles the user interface, file upload, and displaying results  

- data_loader.py  
  Loads CSV data into a Pandas DataFrame  

- data_profiler.py  
  Generates dataset statistics (rows, columns, missing values, aggregations)  

- sql_engine.py  
  Executes SQL queries using DuckDB  

- ai_insights.py  
  Generates AI insights based on structured summaries  

- question_answering.py  
  Handles natural language questions over the dataset  

---

## Installation

```bash
git clone https://github.com/YOUR_USERNAME/ai-data-insights-assistant.git
cd ai-data-insights-assistant

python -m venv .venv
.venv\Scripts\activate

pip install -r requirements.txt
Setup

Create a .env file in the root directory:

OPENAI_API_KEY=your_api_key_here
Run the App
streamlit run app.py
Example Questions
Which category has the highest sales?
Which region performs best?
Are there missing values?
Language Support

Default language is English.

You can modify prompts in:

src/ai_insights.py
src/question_answering.py
Author

Johannes Aydin
GitHub: https://github.com/JohannesAydin96

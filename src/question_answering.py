import os
from dotenv import load_dotenv
from openai import OpenAI

from src.data_loader import load_data
from src.data_profiler import generate_basic_summary
from src.sql_engine import run_basic_queries

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def answer_question_about_data(question, pandas_summary, sql_summary):
    prompt = f"""
You are a helpful data analyst.

You are given two summaries of the same sales dataset.

Pandas summary:
{pandas_summary}

SQL summary:
{sql_summary}

User question:
{question}

Answer the question using only the information provided above.
If the summaries do not contain enough information to answer fully, say that clearly.
Keep the answer concise, clear, and grounded in the data.
Write in plain text only.
Do not use markdown, italics, or bold formatting.
"""

    response = client.responses.create(
        model="gpt-4.1-mini",
        input=prompt
    )

    return response.output_text


if __name__ == "__main__":
    file_path = "data/raw/superstore.csv"

    df = load_data(file_path)
    pandas_summary = generate_basic_summary(df)
    sql_summary = run_basic_queries(file_path)

    question = "Are there any missing values in the dataset?"
    answer = answer_question_about_data(question, pandas_summary, sql_summary)

    print("Question:")
    print(question)
    print("\nAnswer:")
    print(answer)
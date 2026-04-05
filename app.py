import streamlit as st
import tempfile

from src.data_loader import load_data
from src.data_profiler import generate_basic_summary
from src.sql_engine import run_basic_queries
from src.ai_insights import generate_ai_insights
from src.question_answering import answer_question_about_data


st.set_page_config(page_title="AI Data Insights Assistant", layout="wide")

st.title("AI Data Insights Assistant")
st.write("Upload a CSV file, generate AI insights, and ask questions about your data.")

# Session state
if "insights" not in st.session_state:
    st.session_state.insights = None

if "answer" not in st.session_state:
    st.session_state.answer = None

uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file is not None:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".csv") as tmp_file:
        tmp_file.write(uploaded_file.getvalue())
        temp_file_path = tmp_file.name

    df = load_data(temp_file_path)
    pandas_summary = generate_basic_summary(df)
    sql_summary = run_basic_queries(temp_file_path)

    # Preview
    st.subheader("Dataset Preview")
    st.dataframe(df.head(), use_container_width=True)

    # KPI overview
    st.subheader("Dataset Overview")

    col1, col2, col3 = st.columns(3)
    col1.metric("Rows", pandas_summary["num_rows"])
    col2.metric("Columns", pandas_summary["num_columns"])
    col3.metric("Average Sales", f"${pandas_summary['avg_sales']:.2f}")

    col4, col5 = st.columns(2)
    col4.metric("Total Sales", f"${pandas_summary['total_sales']:.2f}")
    col5.metric("Total Profit", f"${pandas_summary['total_profit']:.2f}")

    # Missing values
    st.subheader("Missing Values")
    if sum(pandas_summary["missing_values"].values()) == 0:
        st.success("No missing values found in the dataset.")
    else:
        with st.expander("Show missing values details"):
            st.write(pandas_summary["missing_values"])

    # Columns (hidden)
    with st.expander("Show column names"):
        for column in pandas_summary["columns"]:
            st.write(f"- {column}")

    # Generate insights
    if st.button("Generate AI Insights"):
        with st.spinner("Generating insights..."):
            st.session_state.insights = generate_ai_insights(
                pandas_summary,
                sql_summary
            )

    # Show insights (bullet format + safe)
    if st.session_state.insights is not None:
        st.subheader("AI Insights")

        insights = st.session_state.insights

        sentences = insights.split(". ")

        bullet_lines = []
        for sentence in sentences:
            cleaned = sentence.strip()

            if cleaned:
                if not cleaned.endswith("."):
                    cleaned += "."

                bullet_lines.append(f"• {cleaned}")

        st.text("\n".join(bullet_lines))

    # Q&A
    st.subheader("Ask a Question About the Data")
    user_question = st.text_input("Enter your question")

    if st.button("Get Answer"):
        if user_question.strip():
            with st.spinner("Generating answer..."):
                st.session_state.answer = answer_question_about_data(
                    user_question,
                    pandas_summary,
                    sql_summary
                )
        else:
            st.warning("Please enter a question first.")

    # Show answer
    if st.session_state.answer is not None:
        st.subheader("Answer")
        st.text(st.session_state.answer)
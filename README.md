# AI Data Insights Assistant

An interactive data analysis tool that allows users to upload a CSV file, explore the dataset, generate AI-powered insights, and ask questions about the data.

Built with Python, Pandas, SQL (DuckDB), OpenAI, and Streamlit.

---

## 🚀 Features

* Upload and analyze CSV datasets
* Automatic data profiling (rows, columns, missing values)
* SQL-based aggregation using DuckDB
* AI-generated insights based on dataset statistics
* Natural language Q&A over your data
* Interactive web interface with Streamlit

---

## 🛠️ Tech Stack

* Python
* Pandas
* DuckDB
* OpenAI API
* Streamlit
* python-dotenv

---

## 📊 How It Works

1. Upload CSV file
2. Data is processed using Pandas
3. SQL queries run via DuckDB
4. AI generates insights
5. Users can ask questions about the dataset

---

## ⚙️ Installation

```bash
git clone https://github.com/YOUR_USERNAME/ai-data-insights-assistant.git
cd ai-data-insights-assistant

python -m venv .venv
.venv\Scripts\activate

pip install -r requirements.txt
```

---

## 🔑 Setup

Create a `.env` file in the root directory:

```env
OPENAI_API_KEY=your_api_key_here
```

---

## ▶️ Run the App

```bash
streamlit run app.py
```

---

## 💡 Example Questions

* Which category has the highest sales?
* Which region performs best?
* Are there missing values?

---

## 🌍 Language Support

Default language is English.

You can modify prompts in:

* `src/ai_insights.py`
* `src/question_answering.py`

---

## 🔮 Future Improvements

* Data visualizations (charts)
* Export insights to PDF
* Multi-language UI toggle
* Better prompt customization

---

## 👤 Author

Johannes Aydin
GitHub: https://github.com/JohannesAydin96

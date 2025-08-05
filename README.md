# 📄 PDF Text Summarizer

This is a simple but powerful tool I built to quickly summarize lengthy PDFs using AI. Whether you're a student going through research papers or just someone who wants to get the gist of a document fast — this app can help.


## 👩‍💻 About the Project

I built this project as a way to explore text summarization and make something practically useful. It uses Python, Streamlit for the UI, Hugging Face Transformers for Summarization and KeyBERT for extracting keywords.

Just upload a PDF, and you’ll get:
- A clean summary (short or detailed based on your choice)
- Keywords extracted from the content

It’s fast, easy, and works efficiently.


## ⚙️ How It Works

- **PyPDF2** is used to read PDF text
- **Hugging Face Transformers** generate summaries
- **KeyBERT** is used to extract keywords
- Everything is wrapped inside a **Streamlit app** for a smooth UI experience


## 🚀 How to Run It


##### 1. Clone this repo
git clone https://github.com/purvaparmar/project_pdf_text_summarizer.git

##### 2. Go to the project folder
cd project_pdf_text_summarizer

##### 3. Install dependencies
pip install -r requirements.txt

##### 4. Launch the app
streamlit run app.py


> Python 3.8+ is recommended



## 🗂️ Project Structure


## project_pdf_text_summarizer/
##### ├── app.py               # Main Streamlit app
##### ├── summarizer.py        # Contains logic for summarizing and keyword extraction
##### ├── requirements.txt     # Python dependencies
##### ├── .gitignore
##### └── README.md




## 🌟 Why I Made This

I was tired of manually going through 30-page documents just to find key points. So I thought — why not build something that does it for me?

This started as a small side project but became something I now use regularly. Hope it’s helpful for you too!


## 🙋‍♀️ Author

**Purva Parmar**  
Student | Developer | AI Enthusiast_  
GitHub: [purvaparmar](https://github.com/purvaparmar)



If you found this project helpful, feel free to give it a ⭐️ or share it with others.Thank you.


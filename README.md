# 📄 Chat with PDF using Groq + LLaMA3 + Streamlit


This is a **PDF chatbot app** powered by LLaMA3 (via Groq) that lets you:

- Upload a PDF
- Ask questions about its content
- Chat naturally with memory
- Use open-source embeddings and fast inference!

---

## ✨ Features

- 📤 Upload PDF documents
- 🧠 Vector-based Q&A from content
- 💬 Memory-based conversational responses
- ⚡ Uses Groq’s blazing fast LLaMA3
- 🧾 Drag-and-drop or file select for PDF
- ✅ Works locally in browser (Streamlit)

---

## 🚀 Demo



![Upload PDF](<img width="1891" height="966" alt="image" src="https://github.com/user-attachments/assets/b4642a4b-2a14-4176-8728-b871e5031ae0" />)


---

## 🧰 Tech Stack

| Tool           | Use                         |
|----------------|------------------------------|
| Streamlit      | Frontend/UI                 |
| Groq           | LLM (LLaMA3-8B) API         |
| LangChain      | Chaining & Memory           |
| FAISS          | Vector database (in-memory) |
| HuggingFace    | Sentence Embeddings         |
| dotenv         | Secret management           |

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

groq_pdf_chatbot/
├── app.py                # Main Streamlit app
├── requirements.txt      # Python dependencies
├── .env                  # Your Groq API Key (not tracked by Git)
└── screenshots/          # Demo images (optional)

Steps:
# 1. Clone the project
git clone https://github.com/your-username/groq-pdf-chatbot.git
cd groq-pdf-chatbot

# 2. Create and activate a virtual environment
# For Windows:
python -m venv venv
venv\Scripts\activate

# For macOS/Linux:
# python3 -m venv venv
# source venv/bin/activate

# 3. Create requirements.txt with this content:
# (skip this if already present)
echo streamlit > requirements.txt
echo langchain==0.1.14 >> requirements.txt
echo langchain-community==0.0.30 >> requirements.txt
echo langchain-groq==0.0.1 >> requirements.txt
echo pypdf >> requirements.txt
echo faiss-cpu >> requirements.txt
echo sentence-transformers >> requirements.txt
echo python-dotenv >> requirements.txt
echo "pydantic<2" >> requirements.txt

# 4. Install dependencies
pip install -r requirements.txt

# 5. Get your Groq API Key
# 👉 Go to https://console.groq.com/keys
# 👉 Copy your API key

# 6. Create .env file and add your Groq key
echo GROQ_API_KEY=your_groq_api_key_here > .env

# 7. Run the Streamlit app
streamlit run app.py




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



<img width="1891" height="966" alt="image" src="https://github.com/user-attachments/assets/b4642a4b-2a14-4176-8728-b871e5031ae0" />


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
          

Steps:
1. Clone the project
git clone https://github.com/your-username/groq-pdf-chatbot.git
cd groq-pdf-chatbot

2. Create and activate a virtual environment
For Windows:
python -m venv venv
venv\Scripts\activate

3. Install dependencies
pip install -r requirements.txt

4. Get your Groq API Key
 👉 Go to https://console.groq.com/keys
 👉 Copy your API key

5. Create .env file and add your Groq key
echo GROQ_API_KEY=your_groq_api_key_here > .env

6. Run the Streamlit app
streamlit run app.py




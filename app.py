import os
import streamlit as st
from PyPDF2 import PdfReader
from dotenv import load_dotenv
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_groq import ChatGroq
from langchain.chains.question_answering import load_qa_chain
from datetime import datetime

# Load environment variables
load_dotenv()
groq_api_key= os.getenv("GROQ_API_KEY")

# LLM and Embeddings
llm= ChatGroq(api_key=groq_api_key, model_name="llama3-8b-8192")
embeddings= HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

# Initialize session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

def read_pdf(pdf_docs):
    text= ""
    for pdf in pdf_docs:
        reader= PdfReader(pdf)
        for page in reader.pages:
            text+= page.extract_text() or ""
    return text

def split_text(text):
    splitter= RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    return splitter.split_text(text)

def create_vectorstore(chunks):
    vectorstore= FAISS.from_texts(chunks, embedding=embeddings)
    vectorstore.save_local("faiss_db")

def answer_question(question):
    if not os.path.exists("faiss_db/index.faiss"):
        st.error("❌ Please upload and process a PDF first.")
        return

    db= FAISS.load_local("faiss_db", embeddings, allow_dangerous_deserialization=True)
    retriever= db.as_retriever()
    docs= retriever.get_relevant_documents(question)

    chain= load_qa_chain(llm, chain_type="stuff")
    response= chain.run(input_documents=docs, question=question)

    # Save to session history
    st.session_state.chat_history.append(("🧑 You", question))
    st.session_state.chat_history.append(("🤖 Bot", response))

    return response

def save_chat_to_file():
    filename= f"chat_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    with open(filename, "w", encoding="utf-8") as f:
        for sender, message in st.session_state.chat_history:
            f.write(f"{sender}: {message}\n")
    return filename

def main():
    st.set_page_config(page_title="Groq PDF Chatbot with Memory")
    st.title("🦙 Chat with PDF - Powered by LLaMA3")

    # Display previous chat history
    if st.session_state.chat_history:
        st.markdown("### 💬 Chat History")
        for sender, msg in st.session_state.chat_history:
            st.markdown(f"**{sender}:** {msg}")

    # Question input
    question= st.text_input("Ask a question about your PDF:")

    if question:
        response= answer_question(question)
        if response:
            st.markdown("### ✅ Response:")
            st.write(response)

    # Sidebar for PDF upload
    with st.sidebar:
        st.title("📂 Upload & Process")
        pdf_docs= st.file_uploader("Upload PDF(s)", accept_multiple_files=True)
        if st.button("Submit & Process"):
            with st.spinner("Reading & Indexing PDFs..."):
                raw_text= read_pdf(pdf_docs)
                chunks= split_text(raw_text)
                create_vectorstore(chunks)
                st.success("✅ PDF processed!")

        if st.button("💾 Save Chat to File"):
            filename= save_chat_to_file()
            st.success(f"Chat saved to `{filename}`")

if __name__ == "__main__":
    main()



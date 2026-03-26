🚀 AI-Powered Smart Tutor (EduMentor)

An intelligent AI tutoring system that combines LLM-based chat with PDF-based Retrieval-Augmented Generation (RAG) to deliver context-aware, accurate answers from your own study materials.

🧠 Features

💬 AI Chat Tutor
Ask any question and get clear, concise answers
Powered by fast and free LLM (Groq)

📄 PDF-Based Learning (RAG)
Upload study materials (PDFs)
Ask questions directly from your documents
Context-aware answers using semantic search

🔍 Smart Retrieval
Uses FAISS for efficient similarity search
Retrieves relevant chunks before answering

📥 Chat History Export
Download conversations as HTML
Useful for revision and notes

🎨 Interactive UI
Built with Streamlit
Clean and user-friendly interface

🏗️ Architecture

User Query

   ↓
   
FAISS Vector Search (if PDF mode ON)

   ↓

Relevant Context Retrieved

   ↓

Groq LLM (LLaMA Model)

   ↓

Final Answer

🛠️ Tech Stack

Frontend: Streamlit

LLM: Groq (LLaMA 3 models)

Embeddings: HuggingFace (MiniLM)

Vector DB: FAISS

Framework: LangChain

Language: Python

📦 Installation

1. Clone the repository

git clone https://github.com/YOUR_USERNAME/ai-powered-smart-tutor.git

cd ai-powered-smart-tutor

2. Create virtual environment

python -m venv venv

venv\Scripts\activate   # Windows

3. Install dependencies

pip install -r requirements.txt

4. Run the app

streamlit run app.py

🔑 API Key Setup

Get your free API key from Groq:

👉 https://console.groq.com/

Enter it in the app when prompted.

📄 How to Use

Launch the app

Enter your Groq API key

Upload PDF files (optional)

Click "Process PDFs"

Enable "Use PDF Knowledge"

Start asking questions

📁 Project Structure

ai-powered-smart-tutor/

│

├── app.py                # Main Streamlit app

├── pdf_handler.py        # PDF processing + FAISS

├── chat_gen.py           # Chat export logic

├── requirements.txt

├── logo.png

├── .gitignore

🚀 Future Improvements

📌 Show source page numbers in answers

🎯 Highlight extracted content

⚡ Streaming responses (real-time typing)

🌐 Deploy on cloud (Streamlit Cloud / AWS)

🎤 Voice-based tutor

🧠 Key Learning Outcomes

Built a RAG pipeline from scratch

Integrated LLMs with vector databases

Designed a full-stack AI application

Handled real-world API + dependency issues

📜 License

This project is for educational and demonstration purposes.

🙌 Acknowledgements

Groq for fast LLM inference

Hugging Face for embeddings

Streamlit for UI framework

⭐ If you like this project

Give it a star ⭐ on GitHub!

from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings


# Load embedding model (free)
embeddings = HuggingFaceEmbeddings(
    model_name="all-MiniLM-L6-v2"
)


def process_pdfs(uploaded_files):
    documents = []

    for file in uploaded_files:
        with open(file.name, "wb") as f:
            f.write(file.getbuffer())

        loader = PyPDFLoader(file.name)
        pages = loader.load()
        documents.extend(pages)

    vector_db = FAISS.from_documents(documents, embeddings)
    vector_db.save_local("faiss_index")

    return vector_db


def load_vector_db():
    return FAISS.load_local(
        "faiss_index",
        embeddings,
        allow_dangerous_deserialization=True
    )   
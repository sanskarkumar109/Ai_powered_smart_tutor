# Built-in modules
import os

# Third-party modules
import streamlit as st
from PIL import Image
from groq import Groq

# Local modules
from chat_gen import generate_html
from pdf_handler import process_pdfs, load_vector_db


# -------------------- UI SETUP --------------------
logo = Image.open('logo.png')
sb_logo = Image.open('sb_logo.png')

c1, c2 = st.columns([0.9, 3.2])

with c1:
    st.caption('')
    st.caption('')
    st.image(logo, width=120)

with c2:
    st.title('EduMentor : An AI-Enhanced Tutoring System')

# -------------------- DESCRIPTION --------------------
st.markdown("## AI Tutor Description")
st.markdown(
    "EduMentor leverages AI to provide clear, contextual answers to educational queries."
)

# -------------------- API KEY --------------------
api_key = st.text_input(label='Enter your Groq API Key', type='password')

# -------------------- MAIN LOGIC --------------------
if api_key:
    client = Groq(api_key=api_key)

    # -------------------- SIDEBAR --------------------
    st.sidebar.header('EduMentor: AI-Tutor')
    st.sidebar.image(logo, width=120)
    st.sidebar.caption('Made by D')

    # 📄 PDF Upload Section
    st.sidebar.subheader("📄 Upload Study Material")

    uploaded_files = st.sidebar.file_uploader(
        "Upload PDFs",
        type="pdf",
        accept_multiple_files=True
    )

    if st.sidebar.button("Process PDFs"):
        if uploaded_files:
            with st.spinner("Processing PDFs..."):
                process_pdfs(uploaded_files)
            st.sidebar.success("PDFs processed successfully!")
        else:
            st.sidebar.warning("Please upload files first.")

    # Toggle for PDF mode
    use_pdf = st.sidebar.checkbox("Use PDF Knowledge")

    # 📥 Chat history export
    if st.sidebar.button('Generate Chat History'):
        if "messages" in st.session_state:
            html_data = generate_html(st.session_state.messages)
            st.sidebar.download_button(
                label="Download Chat History as HTML",
                data=html_data,
                file_name="chat_history.html",
                mime="text/html"
            )

    # -------------------- CHAT UI --------------------
    st.subheader('Q&A with AI Tutor 📜')

    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display chat history
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # -------------------- CHAT INPUT --------------------
    if prompt := st.chat_input("Ask your question..."):
        st.session_state.messages.append({"role": "user", "content": prompt})

        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant", avatar='👨🏻‍🏫'):
            message_placeholder = st.empty()

            with st.spinner('Thinking...'):
                try:
                    # 🧠 If PDF mode is ON
                    if use_pdf:
                        vector_db = load_vector_db()
                        docs = vector_db.similarity_search(prompt, k=3)

                        context = "\n\n".join(
                            [doc.page_content for doc in docs]
                        )

                        final_prompt = f"""
                        Answer based on the following content:

                        {context}

                        Question: {prompt}
                        """

                    else:
                        final_prompt = prompt

                    # 🔥 Groq LLM call
                    response = client.chat.completions.create(
                        model="llama-3.3-70b-versatile",
                        messages=[
                            {
                                "role": "system",
                                "content": "You are a helpful AI tutor."
                            },
                            {
                                "role": "user",
                                "content": final_prompt
                            }
                        ],
                        temperature=0.7,
                        max_tokens=500
                    )

                    answer = response.choices[0].message.content

                except Exception as e:
                    answer = f"Error: {str(e)}"

            message_placeholder.markdown(answer)
            st.session_state.messages.append(
                {"role": "assistant", "content": answer}
            )

else:
    st.warning("Please enter your Groq API Key to use EduMentor.")
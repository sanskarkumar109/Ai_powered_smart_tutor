import streamlit as st
import os


# -------------------- UPLOAD FILES --------------------
def upload_files(client, uploaded_files):
    file_ids = []

    for uploaded_file in uploaded_files:
        if uploaded_file is not None:
            response = client.files.create(
                file=uploaded_file,
                purpose="assistants"
            )
            file_ids.append(response.id)

    return file_ids


# -------------------- CREATE VECTOR STORE --------------------
def create_vector_store(client, assistant_id, file_ids):
    # Create vector store
    vector_store = client.beta.vector_stores.create(
        name="edu-mentor-store"
    )

    # Attach files to vector store
    for file_id in file_ids:
        client.beta.vector_stores.files.create(
            vector_store_id=vector_store.id,
            file_id=file_id
        )

    # Attach vector store to assistant
    client.beta.assistants.update(
        assistant_id=assistant_id,
        tool_resources={
            "file_search": {
                "vector_store_ids": [vector_store.id]
            }
        }
    )

    return vector_store.id


# -------------------- MAIN FUNCTION --------------------
def check_and_upload_files(client, assistant_id):

    st.warning("Upload Educational PDF Material")

    uploaded_files = st.file_uploader(
        "Choose PDF files",
        type="pdf",
        accept_multiple_files=True
    )

    if st.button("Upload and Process Files"):
        if uploaded_files:
            try:
                # Upload files
                file_ids = upload_files(client, uploaded_files)

                # Create vector store + attach
                vector_store_id = create_vector_store(
                    client,
                    assistant_id,
                    file_ids
                )

                st.success(f"{len(file_ids)} files uploaded and indexed successfully!")

                return file_ids

            except Exception as e:
                st.error(f"Error while processing files: {e}")
        else:
            st.warning("Please select at least one file.")

    return []
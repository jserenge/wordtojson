import streamlit as st
import docx
import json
from io import BytesIO

def docx_to_json(docx_file):
    doc = docx.Document(docx_file)
    content = "\n".join([para.text for para in doc.paragraphs])
    return {"content": content}

def main():
    st.title("Word to JSON Converter")

    uploaded_file = st.file_uploader("Choose a Word document", type="docx")

    if uploaded_file is not None:
        # Convert the uploaded Word document to JSON
        json_data = docx_to_json(uploaded_file)
        
        # Display the JSON data
        st.json(json_data)
        
        # Convert JSON data to a downloadable file
        json_str = json.dumps(json_data, indent=4)
        b = BytesIO(json_str.encode())
        b.seek(0)
        
        # Provide a download link
        st.download_button(
            label="Download JSON",
            data=b,
            file_name="converted.json",
            mime="application/json"
        )

if __name__ == "__main__":
    main()

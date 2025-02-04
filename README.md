# 📄 Word to JSON Converter

## 🚀 Overview
The **Word to JSON Converter** is a simple web application built with **Streamlit** that allows users to upload a Word document (`.docx`) and convert its contents into a structured **JSON format**.

## ✨ Features
- 📂 **Upload** a `.docx` file.
- 🔄 **Convert** Word document content into a JSON object.
- 👀 **View** the extracted text in JSON format.
- 📥 **Download** the converted JSON file.

## 🛠 Installation
### Prerequisites
Ensure you have Python installed along with the required dependencies:

```bash
pip install streamlit python-docx
```

## ▶ How to Use
1. **Run the application:**
   ```bash
   streamlit run app.py
   ```
2. **Upload** a Word document using the provided file uploader.
3. **View** the extracted text as a JSON object.
4. **Download** the JSON file for further use.

## 📜 File Format Requirements
- The uploaded file **must** be a `.docx` file.
- The content is extracted **line by line** and stored as a JSON object.

## 🏗 Code Structure
- **`docx_to_json(docx_file)`** → Converts the uploaded `.docx` file into JSON format.
- **`main()`** → Streamlit UI logic to interact with users.

## 🛠 Future Enhancements
- 📊 Add support for **tables and formatting** extraction.
- 🔍 Implement **text summarization** for long documents.
- 🌐 Allow **multiple file conversions** at once.

## 📜 Example JSON Output
```json
{
    "content": "This is the extracted text from the Word document."
}
```

## 📜 License
This project is **open-source** and available for modification and use.

🚀 Happy Converting! 🎉


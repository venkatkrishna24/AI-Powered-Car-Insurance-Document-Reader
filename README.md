# AI-Powered-Car-Insurance-Document-Reader
# 🚗 AutoClaim Insight: AI-Powered Car Insurance PDF Analyzer

AutoClaim Insight is a Flask-based web application that uses LLM APIs (like GROQ or Gemini) to extract important information from car insurance claim PDFs. Upload a PDF and get instant details like Policy Holder, License Plate, Damage Location, and Claim Purpose.

## 🔧 Features

- 📄 Upload car insurance claim PDFs
- 🤖 AI-powered data extraction (via GROQ/Gemini APIs)
- 🧠 Extracts:
  - Policy Holder Name
  - License Plate Number
  - Damage Location
  - Purpose of Claim
- 🌐 Simple, user-friendly web interface
- 📦 Clean folder structure and modular code

pip install -r requirements.txt

export GROQ_API_KEY=your_groq_key_here
# OR
export GEMINI_API_KEY=your_gemini_key_here

python app.py

🧠 How It Works
User uploads a car insurance claim PDF.

The backend extracts text using PyMuPDF or pdfplumber.

Text is sent to an LLM (GROQ/Gemini) with a well-crafted prompt.

Extracted info is displayed clearly on the web page.

✅ Requirements
Python 3.8+

Flask

Requests

PyMuPDF (fitz) or pdfplumber

🧪 Future Improvements
Add file history dashboard

Support for scanned image-based PDFs (OCR)

Multi-language PDF support

Admin panel for managing uploads



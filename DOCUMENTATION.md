# Vision AI Assistant - Quick Guide

## 🚀 Quick Start

### Prerequisites
- Python 3.7+
- pip (Python package manager)

### Installation
```bash
# 1. Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # Windows: .\venv\Scripts\activate

# 2. Install requirements
pip install -r requirements.txt
```

### Running the App
```bash
streamlit run app.py
```
Open browser: http://localhost:8501

## 📖 Learning Log

### Key Features
- Image upload and display
- AI-powered image analysis
- Simple web interface

### Challenges & Solutions
1. **Layout Issues**
   - Problem: Image and text not aligned
   - Fix: Used `st.columns()` for side-by-side layout

2. **Image Upload**
   - Problem: Only certain image formats worked
   - Fix: Added support for JPG, JPEG, PNG

3. **API Key Security**
   - Problem: Hardcoded API key
   - Note: For production, use environment variables

### Dependencies
- streamlit: Web interface
- google-generativeai: AI model
- Pillow: Image processing

## 💡 Tips
- Keep images under 4MB for best performance
- Be specific in your prompts for better results
- Check console for any error messages

## 🤝 Support
For issues, please check the [GitHub repository](your-repo-link) or contact support.

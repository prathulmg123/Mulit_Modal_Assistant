# Multi-Modal Vision AI Assistant

A Streamlit-based web application that leverages Google's Gemini 1.5 Flash model to provide intelligent image analysis and description. Upload an image and ask questions about its content to get detailed insights.

## 🚀 Features

- **Image Analysis**: Upload and analyze images in various formats (JPG, JPEG, PNG)
- **Interactive Interface**: User-friendly web interface built with Streamlit
- **Contextual Understanding**: Ask questions about the image content in natural language
- **Responsive Design**: Clean, card-based layout for better visualization
- **Quick Setup**: Easy installation and deployment

## 🛠️ Prerequisites

- Python 3.8 or higher
- Google API key for Gemini (get it from [Google AI Studio](https://makersuite.google.com/))

## 🚀 Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/multi-modal-assistant.git
   cd multi-modal-assistant
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up your Google API key:
   - Replace the API key in `app.py` or set it as an environment variable
   ```python
   genai.configure(api_key="YOUR_API_KEY_HERE")
   ```

## 🏃‍♂️ Running the Application

1. Start the Streamlit server:
   ```bash
   streamlit run app.py
   ```

2. Open your web browser and navigate to `http://localhost:8501`

3. Upload an image and start asking questions!

## 🖼️ Usage

1. Click on "Choose an image" to upload an image file
2. (Optional) Enter a question about the image in the input field
3. Click "Analyze Image" to process the image
4. View the analysis results in the right panel

## 📦 Dependencies

- `streamlit` - Web application framework
- `google-generativeai` - Google's Generative AI SDK
- `Pillow` - Python Imaging Library

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Built with [Google's Gemini](https://ai.google.dev/) AI
- Powered by [Streamlit](https://streamlit.io/)

## 📬 Contact

For any questions or feedback, please reach out to [your.email@example.com](mailto:your.email@example.com)
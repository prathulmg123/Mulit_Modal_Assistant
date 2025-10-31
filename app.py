import streamlit as st
import google.generativeai as genai
from PIL import Image
import time
import io

# Cache the Gemini response to prevent re-computation
@st.cache_data(ttl=3600, show_spinner=False)
def get_gemini_response(input_text, image_bytes):
    model = genai.GenerativeModel("gemini-2.5-flash")
    try:
        # Convert bytes to PIL Image
        image = Image.open(io.BytesIO(image_bytes))
        
        # Prepare the content parts
        parts = [{"mime_type": "image/jpeg", "data": image_bytes}]
        if input_text:
            parts.insert(0, {"text": input_text})
            
        # Generate content
        response = model.generate_content({"parts": parts})
        return response.text
    except Exception as e:
        return f"Error processing image: {str(e)}"

# Initialize session state
def init_session_state():
    if 'last_analysis' not in st.session_state:
        st.session_state.last_analysis = None
    if 'cached_image' not in st.session_state:
        st.session_state.cached_image = None

# Page config and styling
st.set_page_config(
    page_title="Vision AI Assistant",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Load custom CSS
def load_css():
    with open("style.css") as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Configure Gemini
genai.configure(api_key="AIzaSyCSd1Jn3DH1upHup6qrt05EqMlbi1vH2yY")

# Initialize app
def main():
    init_session_state()
    load_css()
    
    # Sidebar
    with st.sidebar:
        st.title("Vision AI Assistant")
        st.markdown("Upload an image and ask a question about it.")
        
        # Form to group inputs and button
        with st.form("image_analysis_form"):
            input_prompt = st.text_input("Input Prompt:", key="input_prompt")
            uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
            analyze_clicked = st.form_submit_button("Analyze Image")
    
    # Main content
    st.title("Image Analysis with Gemini")
    
    # Create placeholders for dynamic content
    image_placeholder = st.empty()
    result_placeholder = st.empty()
    
    # Process form submission
    if analyze_clicked and uploaded_file is not None:
        # Create a container for the loading spinner
        with st.spinner(""):
            # Add a custom loading message with some space
            loading_placeholder = st.empty()
            loading_placeholder.markdown(
                "<div style='text-align: center; margin: 2rem 0;'>"
                "<h3>Analyzing your image...</h3>"
                "<p>This may take a moment. Please wait.</p>"
                "</div>",
                unsafe_allow_html=True
            )
            
            # Read and cache the image
            image_bytes = uploaded_file.read()
            st.session_state.cached_image = image_bytes
            
            try:
                # Process with Gemini
                start_time = time.time()
                response = get_gemini_response(input_prompt, image_bytes)
                processing_time = time.time() - start_time
                
                # Cache the result
                st.session_state.last_analysis = {
                    'response': response,
                    'processing_time': f"{processing_time:.2f} seconds",
                    'timestamp': time.time()
                }
            except Exception as e:
                st.error(f"An error occurred: {str(e)}")
            finally:
                # Clear the loading message
                loading_placeholder.empty()
    
    # Display the image (if available)
    with image_placeholder.container():
        col1, col2 = st.columns([1, 1])
        with col1:
            st.markdown('<div class="card">', unsafe_allow_html=True)
            st.subheader("Your Image")
            if st.session_state.cached_image:
                st.image(st.session_state.cached_image, use_column_width=True)
            else:
                st.info("Upload an image to get started")
            st.markdown('</div>', unsafe_allow_html=True)
    
    # Display results (if available)
    if st.session_state.last_analysis:
        with result_placeholder.container():
            with col2:
                st.markdown('<div class="card" style="color: black !important;">', unsafe_allow_html=True)
                st.markdown('<h3 style="color: #1a1a1a;">Analysis Result</h3>', unsafe_allow_html=True)
                response_html = f'''
                <div style="color: #000000; max-height: 500px; overflow-y: auto;">
                    {st.session_state.last_analysis["response"]}
                    <p style="color: #666; font-size: 0.8em; margin-top: 1em;">
                        Processed in {st.session_state.last_analysis["processing_time"]}
                    </p>
                </div>
                '''
                st.markdown(response_html, unsafe_allow_html=True)
                st.markdown('</div>', unsafe_allow_html=True)
    
    # Footer
    footer_html = f'''
    <div class="footer">
        <p>Developed with ❤️ using Gemini AI</p>
        <p style="font-size: 0.8em; color: #666;">
            Last analyzed: {time.strftime("%Y-%m-%d %H:%M:%S")}
        </p>
    </div>
    '''
    st.markdown(footer_html, unsafe_allow_html=True)

if __name__ == "__main__":
    main()

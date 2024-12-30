#Disaster Management
import os
import streamlit as st
from groq import Groq
from PIL import Image
import io
import base64

# API Configuration
api_key = st.secrets["GROQ_API_KEY"]
client = Groq(api_key=api_key)

def encode_image_to_base64(image):
    buffered = io.BytesIO()
    image.save(buffered, format="PNG")
    return base64.b64encode(buffered.getvalue()).decode('utf-8')

def analyze_with_groq(image, prompt):
    try:
        base64_image = encode_image_to_base64(image)
        response = client.chat.completions.create(
            model="llama-3.2-11b-vision-preview",
            messages=[
                {
                    "role": "user", 
                    "content": [
                        {
                            "type": "image_url", 
                            "image_url": {
                                "url": f"data:image/png;base64,{base64_image}"
                            }
                        },
                        {
                            "type": "text", 
                            "text": prompt
                        }
                    ]
                }
            ],
            max_tokens=1024
        )
        return response.choices[0].message.content
    except Exception as e:
        st.error(f"Analysis error: {e}")
        return "Unable to analyze. Please try again."

def main():
    st.title("🌟 Disaster Management Vision Chat")
    st.markdown("### Upload images and chat about disaster situations")

    # Initialize session state for chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display chat history
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            if "image" in message:
                st.image(message["image"], caption="Uploaded Image")
            st.markdown(message["content"])

    # File uploader
    uploaded_file = st.file_uploader("Upload disaster-related image", type=['png', 'jpg', 'jpeg'])
    
    # Chat input
    prompt = st.chat_input("Ask about the disaster situation...")

    if uploaded_file and prompt:
        # Display user message
        with st.chat_message("user"):
            image = Image.open(uploaded_file)
            st.image(image, caption="Uploaded Image")
            st.markdown(prompt)
            
        # Add user message to history
        st.session_state.messages.append({
            "role": "user",
            "content": prompt,
            "image": image
        })

        # Generate and display assistant response
        with st.chat_message("assistant"):
            with st.spinner("Analyzing..."):
                disaster_prompt = f"""Analyze this disaster-related image and respond to: {prompt}
                Focus on:
                1. Type and severity of disaster
                2. Visible damage assessment
                3. Potential risks and hazards
                4. Recommended immediate actions"""
                
                response = analyze_with_groq(image, disaster_prompt)
                st.markdown(response)
        
        # Add assistant response to history
        st.session_state.messages.append({
            "role": "assistant",
            "content": response
        })

    # Sidebar with additional controls
    with st.sidebar:
        st.header("Settings")
        if st.button("Clear Chat History"):
            st.session_state.messages = []
            st.rerun()

if __name__ == "__main__":
    main()

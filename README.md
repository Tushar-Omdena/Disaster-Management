# Disaster Management Vision Chat

A powerful Streamlit application that combines Groq's LLaMA 3.2 Vision model with interactive chat capabilities for real-time disaster analysis and management.

## Features

**Core Capabilities**
- Real-time image analysis using LLaMA 3.2 Vision model
- Interactive chat interface with image upload functionality
- Persistent conversation history
- Specialized disaster analysis prompts
- Comprehensive visual assessment system

**Analysis Components**
- Disaster type identification
- Damage assessment
- Risk evaluation
- Action recommendations

## Installation

```bash
# Clone the repository
git clone https://github.com/tushar-omdena/disaster-management.git
cd disaster-vision-chat

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

## Requirements

```txt
streamlit>=1.28.0
groq>=0.4.0
Pillow>=10.0.0
python-dotenv>=1.0.0
```

## Environment Setup

1. Create a `.env` file in the project root
2. Add your Groq API key:
```env
GROQ_API_KEY=your_api_key_here
```

## Usage

```bash
streamlit run app.py
```

## Project Structure

```
disaster-vision-chat/
├── app.py
├── requirements.txt
├── .env
├── README.md
└── src/
    ├── components/
    │   └── navigation.py
    └── utils/
        ├── image_analysis.py
        └── capture.py
```

## How to Use

1. Launch the application
2. Upload a disaster-related image
3. Enter your query about the situation
4. Review the AI-powered analysis
5. Continue the conversation with follow-up questions

## Features in Detail

**Image Analysis**
- Supports PNG, JPG, and JPEG formats
- Real-time processing using Groq API
- Detailed visual assessment capabilities

**Chat Interface**
- Persistent chat history
- Context-aware responses
- Clear chat functionality
- Image-text integrated conversations

**Disaster Management Focus**
- Specialized analysis templates
- Structured response format
- Action-oriented recommendations
- Risk assessment capabilities

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Groq API for providing the LLaMA 3.2 Vision model
- Streamlit for the interactive web framework
- The open-source community for various dependencies

## Support

For support, please open an issue in the GitHub repository or contact the maintainers.
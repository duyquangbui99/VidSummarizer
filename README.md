

# Project Name:  VidSummarizer

## Description
SummariAI is an AI-driven web application designed to automatically generate concise summaries from YouTube video transcripts. Leveraging OpenAI's GPT models and a robust Flask backend, this tool enhances content accessibility and digestibility, making it easier for users to grasp the essence of lengthy videos quickly.

## Features
- **AI Summarization**: Utilizes advanced GPT models to transform video transcripts into informative summaries.
- **User-Friendly Interface**: Provides a simple and intuitive web interface where users can input YouTube URLs and receive summaries instantly.
- **Responsive Design**: Ensures a seamless user experience across various devices and screen sizes.
- **Security and Performance**: Integrates CORS policy for secure cross-origin resource sharing and is deployed on a scalable cloud platform.

## Technologies Used
- Flask
- HTML, CSS, JavaScript
- OpenAI's GPT Models
- LangChain library

### Prerequisites
- Python 3.8 or later
- pip and virtualenv
- A valid OpenAI API key


## Installation
To set up the project locally, follow these steps:

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/VidSummarizer.git
   cd VidSummarizer
   
2. **Create and Activate Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate
   On Windows, use `venv\Scripts\activate`

3. **Install dependencies **
   ```bash
   pip install -r requirements.txt
   
3. **Have a valid OpenAI API key to your .env  **
   ```bash
   OPENAI_API_KEY=""

5. **Start the Flask Server**
   ```bash
   flask run



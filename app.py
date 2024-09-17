from flask import Flask, render_template, request, jsonify
from langchain.chains import LLMChain
from flask_cors import CORS
from langchain_openai import ChatOpenAI
from langchain.document_loaders import YoutubeLoader
from dotenv import load_dotenv
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
import os

# Load environment variables
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

app = Flask(__name__)
CORS(app)  # Enable CORS for all domains on all routes

@app.route('/')
def index():
    return render_template('index.html')

def create_transcript_from_youtube_url(video_url):
    try:
        loader = YoutubeLoader.from_youtube_url(video_url)
        transcript = loader.load()
        return transcript
    except Exception as e:
        print(f"Error loading transcript: {e}")
        return None

def get_response_from_transcript(transcript, query):
    try:
        chat = ChatOpenAI(model_name="gpt-4o-mini",
                          temperature=0.2, openai_api_key=openai_api_key)
        template = """
    You are a helpful assistant that can answer questions about YouTube videos 
    based on the video's transcript: {transcript}
    Only use the factual information from the transcript to answer the question
    If you feel like you don't have enough information to answer the question, say "I don't know"."""

        system_message_prompt = SystemMessagePromptTemplate.from_template(template)

        human_template = "Answer the following question: {question}"
        human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)

        chat_prompt = ChatPromptTemplate.from_messages(
            [system_message_prompt, human_message_prompt]
        )

        chain = LLMChain(llm=chat, prompt=chat_prompt)

        response = chain.run(question=query, transcript=transcript)
        response = response.replace("\n", "")
        return response
    except Exception as e:
        print(f"Failed to initialize or query the model: {str(e)}")
        return "Error generating response."

@app.route('/process', methods=['POST'])
def process_request():
    data = request.get_json()
    video_url = data.get('video_url')
    query = data.get('query')

    if not video_url or not query:
        return jsonify({'response': 'Invalid input.'}), 400

    transcript = create_transcript_from_youtube_url(video_url)
    if transcript is None:
        return jsonify({'response': 'Failed to load transcript.'}), 500

    response = get_response_from_transcript(transcript, query)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)

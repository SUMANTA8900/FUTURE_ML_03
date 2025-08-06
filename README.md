# Smart Customer Support Chatbot 🤖

A real-time chatbot for handling many customer support questions using vector search and GPT fallback.

## Features
- FAQ matching with vector search (100+ questions supported)
- GPT fallback for unmatched queries
- Streamlit UI
- Easy deployment

## Run Instructions
1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Add your OpenAI key to chatbot_engine.py
```python
openai.api_key = "your-openai-key"
```

3. Run the app:
```bash
streamlit run app/streamlit_app.py
```

## Dataset
Stored in `data/faq_data.csv` with sample questions.
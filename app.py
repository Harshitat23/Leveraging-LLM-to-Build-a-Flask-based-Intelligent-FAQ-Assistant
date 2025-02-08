from flask import Flask, render_template, request, jsonify
from transformers import pipeline, T5ForConditionalGeneration, AutoTokenizer
import json
import os
from models.interaction_log import log_interaction

app = Flask(__name__)

def load_knowledge_base():
    try:
        with open('knowledge_base/knowledge.json', 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error loading knowledge base: {e}")
        return {}

knowledge_base = load_knowledge_base()

try:
    model_name = "google/flan-t5-base"
    model = T5ForConditionalGeneration.from_pretrained(
        model_name,
        resume_download=True,
        use_safetensors=True
    )
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    qa_pipeline = pipeline(
        "text2text-generation",
        model=model,
        tokenizer=tokenizer,
        device=-1
    )
except Exception as e:
    print(f"Model loading failed: {e}")
    qa_pipeline = None

def get_answer(query, knowledge_base):
    # Search for an exact match in the knowledge base
    for entry in knowledge_base['faq']:
        if query.lower() in entry['question'].lower():
            return entry['answer']
    
    # If no match found, fall back to model-based generation
    if not qa_pipeline:
        return "Error: model is not loaded"
    
    context = json.dumps(knowledge_base)
    prompt = f"Based on the knowledge base: {context} \nQuestion: {query} \nAnswer:"
    
    try:
        response = qa_pipeline(
            prompt,
            max_length=200,
            truncation=True,
            num_beams=5,
            early_stopping=True
        )
        return response[0]['generated_text'].strip()
    except Exception as e:
        print(f"Generation error: {e}")
        return "Error processing request."

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    try:
        query = request.form.get('query')
        if not query:
            return jsonify({'error': 'Missing query'}), 400
            
        response = get_answer(query, knowledge_base)
        
        try:
            log_interaction(query, response)
        except Exception as e:
            print(f"Logging error: {e}")

        return jsonify({'response': response})
        
    except Exception as e:
        print(f"Server error: {e}")
        return jsonify({'error': 'Internal server error'}), 500

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)
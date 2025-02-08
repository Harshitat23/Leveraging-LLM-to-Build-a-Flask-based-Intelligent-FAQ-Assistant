# Leveraging-LLM-to-Build-a-Flask-based-Intelligent-FAQ-Assistant
Flask-based intelligent FAQ assistant using LLM to generate contextually accurate answers. It leverages Flask for the web framework and a pre-trained language model for NLP. Users can interact via a simple UI to get quick answers from an FAQ dataset.

# Key Features

**Knowledge Base Integration:**
The assistant is pre-loaded with a knowledge base, which can be a structured file (JSON). The knowledge base can be updated periodically to keep the information current.

**Dynamic Query Handling:**
Using an LLM, the assistant processes and generates responses based on user queries. It can understand context, making it capable of delivering accurate and relevant answers.

**Flask Application:**
1) Frontend
2) API Endpoint
3) Admin Interface

**Interaction Logging:**
All the user queries and responses are logged to a database (MongoDB) for future analysis and improvement of the model’s performance.

**Fallback Mechanism:**
In cases where the assistant cannot answer a question, it provides a fallback response such as suggesting related topics for this we have use T5 Model.


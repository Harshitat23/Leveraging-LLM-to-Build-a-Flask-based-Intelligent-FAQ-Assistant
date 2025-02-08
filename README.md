# Leveraging-LLM-to-Build-a-Flask-based-Intelligent-FAQ-Assistant
Flask-based intelligent FAQ assistant using LLM to generate contextually accurate answers. It leverages Flask for the web framework and a pre-trained language model for NLP. Users can interact via a simple UI to get quick answers from an FAQ dataset.

# Key Features

**Knowledge Base Integration:**
The assistant is pre-loaded with a knowledge base, which can be a structured file (JSON). The knowledge base can be updated periodically to keep the information current.

**Dynamic Query Handling:**
Using an LLM, the assistant processes and generates responses based on user queries. It can understand context, making it capable of delivering accurate and relevant answers. Handling instances where the LLM cannot provide a clear answer by giving a polite fallback response or suggesting related topics.

**Flask Application:**
1) Frontend
2) API Endpoint
3) Admin Interface

**Interaction Logging:**
All the user queries and responses are logged to a database (MongoDB) for future analysis and improvement of the model’s performance.

**Fallback Mechanism:**
In cases where the assistant cannot answer a question, it provides a fallback response such as suggesting related topics for this we have use T5 Model.

**Setup and Installation**
•	Python 3.x
•	Flask
•	Flask-Cors
•	PyMongo
•	MongoDB (running locally or remotely)
•	Transformers (Hugging Face)
•	Torch

**Architecture**

**1) Frontend:**
The index.html file provides the user interface for interaction with the assistant. It includes a chat container where messages are exchanged between the user and the assistant.

**2) Flask Backend:**
Flask serves as the backend server, receiving user queries through the /ask endpoint.
The backend processes the query by passing it through the LLM model (T5 model) and responds with a generated message based on the knowledge base.

**3) LLM Integration:**
A Large Language Model (LLM), is used to process and generate responses to user queries. The assistant uses the model to generate context-aware answers based on the knowledge base.

**4) Interaction Logging:**
All interactions are logged into a database, like MongoDB, to track user behavior, monitor the quality of responses, and continuously improve the system.

This project provides a robust FAQ chatbot with advanced NLP-based responses and logging capabilities using Flask and MongoDB.

from pymongo import MongoClient
import datetime

client = MongoClient('mongodb://localhost:27017')
db = client.faq_assistant_db
log_collection = db.interaction_logs

def log_interaction(query, response):
    log_entry = {
        'query': query,
        'response': response,
        'timestamp': datetime.datetime.now()
    }
    log_collection.insert_one(log_entry)
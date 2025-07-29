from flask import Flask, request, jsonify
from pymongo import MongoClient
from bson.objectid import ObjectId
from flask_cors import CORS  # ✅ Add this
import os

app = Flask(__name__)
CORS(app)  # ✅ Add this to allow frontend to connect

# ✅ MongoDB URI with fallback
mongo_uri = os.environ.get(
    'MONGO_URI',
    'mongodb+srv://kunalborse1033:lFoG6xUtzl8e1yXb@cluster0.esxk1x.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0'
)
client = MongoClient(mongo_uri)

db = client['contactdb']
contacts = db['contacts']

@app.route('/contacts', methods=['GET'])
def get_contacts():
    data = []
    for contact in contacts.find():
        data.append({
            "id": str(contact["_id"]),
            "name": contact["name"],
            "email": contact["email"],
            "phone": contact["phone"]
        })
    return jsonify(data)

@app.route('/contacts', methods=['POST'])
def add_contact():
    data = request.get_json()
    new_contact = {
        "name": data["name"],
        "email": data["email"],
        "phone": data["phone"]
    }
    result = contacts.insert_one(new_contact)
    return jsonify({"id": str(result.inserted_id)}), 201

@app.route('/contacts/<id>', methods=['DELETE'])
def delete_contact(id):
    result = contacts.delete_one({"_id": ObjectId(id)})
    if result.deleted_count:
        return jsonify({"status": "Deleted"})
    return jsonify({"status": "Not Found"}), 404

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

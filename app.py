from llama_index import GPTSimpleVectorIndex, Document
from flask import Flask, request, jsonify
from llama_index import GPTSimpleVectorIndex, Document
import os

app = Flask(__name__)

# Load your Llama-Index documents (for example, from a file or database)
documents = [
    Document("กระโดดตบช่วยเพิ่มความแข็งแรงให้หัวใจและระบบไหลเวียนโลหิต."),
    Document("วิดพื้นช่วยฝึกกล้ามเนื้อแขนและหน้าอก."),
    Document("สควอทช่วยฝึกขาและสะโพก ทำให้ร่างกายแข็งแรง."),
    # Add more documents here...
]
index = GPTSimpleVectorIndex.from_documents(documents)

@app.route('/get_response', methods=['POST'])
def get_response():
    user_input = request.json['user_input']
    # Query the Llama-Index
    response = index.query(user_input)
    return jsonify({"response": response.response})

if __name__ == '__main__':
    app.run(debug=True)

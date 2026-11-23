from flask import Flask, jsonify, request

app = Flask(__name__)

books =  [
    {
        "id": 1,
        "book_name":"",
        "author":"",
        "publisher":""    
    }
]

@app.route('/books', methods=['POST'])
def create_book():
    new_book = {
        "id": len(books) + 1,
        "book_name": request.json("book_name"),
        "author": request.json("author"),
        "publisher": request.json("publisher")
    }
    books.append(new_book)
    return jsonify(new_book), 201

@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books), 200


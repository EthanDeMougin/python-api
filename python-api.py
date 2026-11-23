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

@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    book = next((book for book in books if book["id"] == book_id), None)
    if book is None:
        return jsonify({
            "error": "Book not found"
        }), 404

    data = request.get_json()
    book["book_name"] = data.get("book_name", book["book_name"])
    book["author"] = data.get("author", book["author"])
    book["publisher"] = data.get("publisher", book["publisher"])

    return jsonify(book), 200

@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    book = next((book for book in books if book["id"] == book_id), None)
    if book is None:
        return jsonify({
            "error": "Book not found"
        }), 404

    books.remove(book)

    return jsonify({
        "message": "Book deleted successfully"
    }), 200

if __name__ == '__main__':
    app.run(debug=True)

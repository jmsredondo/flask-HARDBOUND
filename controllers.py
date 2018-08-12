from flask import Flask
from flask import render_template
from models import get_book
from flask import jsonify
from app import app

def getbook():

    query_dict = []

    for book in get_book():
        book_as_dict = {
            'book_id': book[0],
            'book_name': book[1]
        }
        query_dict.append(book_as_dict)

    print (query_dict)

    return jsonify(query_dict)

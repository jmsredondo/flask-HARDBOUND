from flask import Flask
from flask import render_template
from models import get_book
from flask import jsonify
from app import app

#get list of books
def getbook():

    query_dict = []

    for book in get_book():
        book_as_dict = {
            'book_id': book[0],
            'book_name': book[1]
        }
        query_dict.append(book_as_dict)

    print (query_dict)

    return (query_dict)

#get list of categories
def getcategories():
    pass
#get book for each category
def getbook_per_cat():
    pass
def getusers():
    pass
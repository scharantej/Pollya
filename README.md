## Problem: 
Design a Flask application that allows users to search for books, add books to a reading list, and remove books from the reading list. The application should store the reading list in a database.

## Design:

### HTML Files:
- `index.html`: Main page of the application, contains the search bar and the reading list.
- `add_book.html`: Form for adding a book to the reading list.
- `remove_book.html`: Form for removing a book from the reading list.

### Routes:
- `@app.route('/')`: Main page, displays the search bar and the reading list.
- `@app.route('/search', methods=['GET'])`: Handles search queries and updates the reading list with search results.
- `@app.route('/add_book', methods=['POST'])`: Adds a book to the reading list.
- `@app.route('/remove_book', methods=['POST'])`: Removes a book from the reading list.
# Book API (Django REST Framework)

# Endpoints
GET /books — List all books (public)
GET /books/<id>/ — Get a single book (public)
POST /books/create/ — Create a book (authenticated)
PUT /books/<id>/update/ — Update a book (authenticated)
DELETE /books/<id>/delete/ — Delete a book (authenticated)

# Permissions
Read: Everyone
Create, Update, Delete: Authenticated users only

# Filters
Search by title, author
Order by title, published_date

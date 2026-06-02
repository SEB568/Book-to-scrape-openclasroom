def transform_data(books):

    cleaned_books = []

    for book in books:
        book[3] = book[3].replace("£", "")
        book[4] = book[4].replace("£", "")
        cleaned_books.append(book)

    return cleaned_books
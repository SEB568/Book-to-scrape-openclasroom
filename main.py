from extract import extract_book_data, get_books_urls
from transform import transform_data
from load import load_data


def main():

    category_url = "https://books.toscrape.com/catalogue/category/books/travel_2/index.html"

    book_urls = get_books_urls(category_url)

    books = []

    for url in book_urls:
        books.append(extract_book_data(url))

    books = transform_data(books)
    load_data(books)

    print("Done")


if __name__ == "__main__":
    main()
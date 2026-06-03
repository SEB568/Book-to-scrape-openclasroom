from extract import extract_book_data, get_books_urls, get_categories_urls
from transform import transform_data
from load import load_data


def main():

    categories = get_categories_urls()

    for category_name, category_url in categories.items():

        print(f"Scraping: {category_name}")

        book_urls = get_books_urls(category_url)

        books = []

        for url in book_urls:
            books.append(extract_book_data(url))

        books = transform_data(books)

        load_data(books, category_name)

        print(f"Done: {category_name}")


if __name__ == "__main__":
    main()
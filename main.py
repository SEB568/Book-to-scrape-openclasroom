"""
Entry point of the program.

Executes the full ETL pipeline:
- extracts categories from the website
- scrapes all books from each category
- cleans the data
- exports one CSV file per category
"""

from extract import extract_book_data, get_books_urls, get_categories_urls
from transform import transform_data
from load import load_data


def main():
    categories = get_categories_urls()

    print(f"Nombre de catégories: {len(categories)}")

    for category_name, category_url in categories.items():

        print(f"\nScraping: {category_name}")

        book_urls = get_books_urls(category_url)

        print(f"Nombre de livres trouvés: {len(book_urls)}")

        books = []

        for url in book_urls:
            try:
                books.append(extract_book_data(url))
            except Exception as e:
                print(f"Erreur sur {url}: {e}")

        print(f"Livres extraits: {len(books)}")

        books = transform_data(books)

        load_data(books, category_name)

        print(f"Done: {category_name}")


if __name__ == "__main__":
    main()
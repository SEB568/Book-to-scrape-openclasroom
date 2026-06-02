import csv
import os


def load_data(books):

    if not os.path.exists("data"):
        os.mkdir("data")

    file_path = "data/books.csv"

    with open(file_path, "w", newline="", encoding="utf-8") as file:

        writer = csv.writer(file)

        writer.writerow([
            "product_page_url",
            "upc",
            "title",
            "price_including_tax",
            "price_excluding_tax",
            "number_available",
            "product_description",
            "category",
            "review_rating",
            "image_url"
        ])

        for book in books:
            writer.writerow(book)
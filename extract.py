import requests
from bs4 import BeautifulSoup
import csv


def extract_and_save():

    print("Scraping started...")

    # Product page URL
    url = "https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"

    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    # Extract data
    product_page_url = url
    upc = soup.find("th", string="UPC").find_next("td").text
    title = soup.find("h1").text

    price_including_tax = soup.find("th", string="Price (incl. tax)").find_next("td").text
    price_excluding_tax = soup.find("th", string="Price (excl. tax)").find_next("td").text

    number_available = soup.find("th", string="Availability").find_next("td").text

    description_tag = soup.find("div", id="product_description")
    product_description = description_tag.find_next("p").text if description_tag else ""

    category = soup.select("ul.breadcrumb li")[2].text.strip()

    review_rating = soup.find("p", class_="star-rating")["class"][1]

    image_url = "https://books.toscrape.com/" + soup.find("img")["src"].replace("../../", "")

    # Create CSV file
    with open("book.csv", "w", newline="", encoding="utf-8") as file:

        writer = csv.writer(file)

        # Headers
        writer.writerow([
            "product_page_url",
            "universal_product_code",
            "title",
            "price_including_tax",
            "price_excluding_tax",
            "number_available",
            "product_description",
            "category",
            "review_rating",
            "image_url"
        ])

        # Data row
        writer.writerow([
            product_page_url,
            upc,
            title,
            price_including_tax,
            price_excluding_tax,
            number_available,
            product_description,
            category,
            review_rating,
            image_url
        ])

    print("CSV created successfully!")


# RUN SCRIPT
extract_and_save()
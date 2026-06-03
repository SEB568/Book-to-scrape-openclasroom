#EXTRACT MODULE

This module contains all web scraping functions:
- extract book data from a single book page
- retrieve all book URLs from a category (with pagination)
- retrieve all categories from the website #



import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

BASE_URL = "https://books.toscrape.com/"


def extract_book_data(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

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

    image_url = BASE_URL + soup.find("img")["src"].replace("../../", "")

    return [
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
    ]

#   Retrieves all book URLs from a category page,
    including pagination handling.

    Args:
        category_url (str): URL of the category page

    Returns:
        list: List of all book URLs in the category#

def get_books_urls(category_url):

    urls = []
    next_page = category_url

    while next_page:

        response = requests.get(next_page)
        soup = BeautifulSoup(response.text, "html.parser")

        books = soup.select("article.product_pod h3 a")

        for book in books:
            relative_url = book["href"].replace("../../../", "")
            full_url = BASE_URL + "catalogue/" + relative_url
            urls.append(full_url)

        next_btn = soup.select_one("li.next a")

        if next_btn:
            next_page = urljoin(next_page, next_btn["href"])
        else:
            next_page = None

    return urls

    #    Retrieves all categories from the website.

    Returns:
        dict: Dictionary where:
            - key = category name
            - value = category URL#

def get_categories_urls():

    base_url = BASE_URL

    response = requests.get(base_url)
    soup = BeautifulSoup(response.text, "html.parser")

    categories = {}

    category_links = soup.select(".side_categories ul li ul li a")

    for link in category_links:
        name = link.text.strip()
        url = urljoin(base_url, link["href"])
        categories[name] = url

    return categories
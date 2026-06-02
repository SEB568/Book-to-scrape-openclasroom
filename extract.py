import requests
from bs4 import BeautifulSoup


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


def get_books_urls(category_url):
    response = requests.get(category_url)
    soup = BeautifulSoup(response.text, "html.parser")

    books = soup.select("article.product_pod h3 a")

    urls = []

    for book in books:
        relative_url = book["href"].replace("../../../", "")
        full_url = BASE_URL + "catalogue/" + relative_url
        urls.append(full_url)

    return urls
import requests
from bs4 import BeautifulSoup
import os

BASE_URL = "https://books.toscrape.com/"


def download_image(image_url, category, title):

    folder = f"data/images/{category}"
    os.makedirs(folder, exist_ok=True)

    # clean filename (Windows safe)
    filename = (
        title
        .replace(":", "")
        .replace("/", "")
        .replace("\\", "")
        .replace("?", "")
        .replace("*", "")
        .replace("\"", "")
        .replace("<", "")
        .replace(">", "")
        .replace("|", "")
        + ".jpg"
    )

    filepath = folder + "/" + filename

    img = requests.get(image_url).content

    with open(filepath, "wb") as f:
        f.write(img)


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

    # download image (ADDED FEATURE)
    download_image(image_url, category, title)

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
            next_page = "/".join(next_page.split("/")[:-1]) + "/" + next_btn["href"]
        else:
            next_page = None

    return urls


def get_categories_urls():

    response = requests.get(BASE_URL)
    soup = BeautifulSoup(response.text, "html.parser")

    categories = {}

    category_links = soup.select(".side_categories ul li ul li a")

    for link in category_links:
        name = link.text.strip()
        url = BASE_URL + link["href"]
        categories[name] = url

    return categories

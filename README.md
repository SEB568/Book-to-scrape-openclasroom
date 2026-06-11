# Books to Scrape – ETL Project

## Description

This project is a Python web scraping application that extracts book data from the website **Books to Scrape**.

It implements a full ETL pipeline (Extract – Transform – Load):

- **Extract**: retrieve book data from all categories on the website
- **Transform**: clean and structure raw data into usable formats
- **Load**: save processed data into CSV files and download book images locally

The goal of this project is to simulate a price monitoring system for books, which could be extended for data analysis or market tracking.

---

## Technologies Used

- Python 3.14.2
- requests
- beautifulsoup4
- csv
- os

---

## ETL Pipeline

### 1. Extract
- Scrapes all categories from the website
- Handles pagination automatically
- Extracts product data such as:
  - product page URL
  - UPC
  - title
  - price (including/excluding tax)
  - availability
  - description
  - category
  - rating
  - image URL

### 2. Transform
- Cleans raw HTML data
- Formats text fields (titles, descriptions)
- Converts prices into usable formats
- Structures data into consistent Python objects

### 3. Load
- Saves data into CSV files (one per category)
- Downloads and stores book images locally
- Organizes images by category

---

## Project Structure

---

project/
│
├── main.py # ETL pipeline entry point
├── extract.py # scraping logic + image download
├── transform.py # data cleaning
├── load.py # CSV export
│
├── data/
│ ├── images/ # downloaded images
│ ├── *.csv # generated CSV files
│
├── requirements.txt
├── README.md
└── .gitignore












## Installation & Usage

### 1. Clone the repository
git clone <repo-url>
cd project

### 2. Create a virtual environment
python -m venv venv

### 3. Activate the virtual environment

Windows:
venv\Scripts\activate

Mac/Linux:
source venv/bin/activate

### 4. Install dependencies
pip install -r requirements.txt

### 5. Run the project
python main.py

---

## Output

After execution, the project generates:

- CSV files (one per category)
- Downloaded book images stored locally in `/data/images/`

---

## Notes

- The `data/` folder (CSV + images) is not included in the Git repository
- Only source code is versioned
- All generated data is produced after running the ETL pipeline

---

## Author

Python ETL scraping project developed as part of a training program.
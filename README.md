# Books to Scrape – ETL Project

## Description

This project is a Python web scraping application that extracts book data from the website Books to Scrape.

It follows a full ETL pipeline (Extract – Transform – Load):
- Extract: scrape book data from all categories
- Transform: clean and format raw data
- Load: save data into CSV files and download images

---

## Features

- Scrapes all book categories from the website
- Handles pagination automatically
- Extracts full product information:
  - product page URL
  - UPC
  - title
  - price including/excluding tax
  - availability
  - description
  - category
  - rating
  - image URL
- Creates one CSV file per category
- Downloads and stores all book images locally
- Organizes images by category

---

## Project Structure

```text
project/
│
├── main.py              # ETL pipeline entry point
├── extract.py           # scraping logic + image download
├── transform.py         # data cleaning
├── load.py              # CSV export
│
├── data/
│   ├── images/          # downloaded images
│   ├── *.csv            # generated CSV files
│
├── requirements.txt
├── README.md
└── .gitignore
from extract import extract_data
from transform import transform_data
from load import load_data


def main():
    books = extract_data()
    books = transform_data(books)
    load_data(books)

    print("Done")


if __name__ == "__main__":
    main()
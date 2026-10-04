import requests
from bs4 import BeautifulSoup
import pandas as pd
from urllib.parse import urljoin

base_url = "https://books.toscrape.com/"

books_data = []

for page in range(1, 51):

    if page == 1:
        url = base_url
    else:
        url = f"{base_url}catalogue/page-{page}.html"

    print(f"Scraping page {page}...")

    response = requests.get(url)

    if response.status_code != 200:
        print(f"Could not access page {page}")
        continue

    soup = BeautifulSoup(response.text, "html.parser")

    books = soup.select("article.product_pod")

    for book in books:

        title = book.h3.a["title"]

        price = book.select_one(".price_color").text.strip()
        price = price.replace("Â£", "£")

        rating = book.select_one("p.star-rating")["class"][1]

        availability = book.select_one(".availability").text.strip()

        relative_url = book.h3.a["href"]
        book_url = urljoin(url, relative_url)

        books_data.append({
            "Title": title,
            "Price": price,
            "Rating": rating,
            "Availability": availability,
            "URL": book_url
        })


df = pd.DataFrame(books_data)

output_path = "Dataset/books_data.csv"

df.to_csv(output_path, index=False, encoding="utf-8-sig")

print()
print("Scraping completed!")
print("Total books scraped:", len(df))
print("CSV saved to:", output_path)

import requests
from bs4 import BeautifulSoup


def get_product_details(url):
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(
        url,
        headers=headers,
        timeout=10
    )

    response.raise_for_status()

    soup = BeautifulSoup(response.text, "lxml")

    title = soup.find("title")

    if title:
        product_name = title.get_text(strip=True)
    else:
        product_name = "Unknown Product"

    return product_name


if __name__ == "__main__":
    url = input("Enter product URL: ")

    try:
        name = get_product_details(url)
        print("Product:", name)

    except Exception as e:
        print("Error:", e)

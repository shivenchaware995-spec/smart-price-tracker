# Smart Price Tracker

A Python-based price tracking application that allows users to track product prices, set a target price, and receive an alert when the current price reaches or falls below the target price.

## Features

* Add product using a URL
* Extract product name from the webpage
* Set a target price
* Store product information in SQLite
* Compare current price with target price
* Generate price-drop alerts
* View all tracked products
* Simple command-line interface

## Technologies Used

* Python
* Requests
* BeautifulSoup
* SQLite
* Schedule

## Project Structure

```text
smart-price-tracker/
│
├── app.py
├── scraper.py
├── database.py
├── notifier.py
├── requirements.txt
├── .gitignore
└── README.md
```

## How It Works

```text
Product URL
     ↓
Web Scraping
     ↓
Product Information
     ↓
Set Target Price
     ↓
Compare Prices
     ↓
Price Alert
```

## Installation

Clone the repository:

```bash
git clone https://github.com/shivenchaware995-spec/smart-price-tracker.git
```

Open the project folder:

```bash
cd smart-price-tracker
```

Install the required packages:

```bash
pip install -r requirements.txt
```

## Run the Project

```bash
python app.py
```

## Example

```text
========================================
       SMART PRICE TRACKER
========================================

1. Add Product
2. View Products
3. Exit

Enter your choice: 1

Enter product URL: https://example.com

Product found:
Example Product

Enter target price: ₹600
Enter current price: ₹500

🔔 PRICE ALERT!

Current Price: ₹500
Target Price: ₹600

Buy now! Price is below your target.
```

## Database

The project uses SQLite to store:

* Product ID
* Product name
* Product URL
* Target price
* Current price
* Last checked time

The database file is ignored by Git using `.gitignore`.

## Future Improvements

* Automatic current price extraction
* Automatic price checking
* Price history tracking
* Telegram notifications
* Email notifications
* Streamlit dashboard
* Price history graphs
* Multiple e-commerce website support
* Scheduled background price monitoring

## Author

**Shiven Chaware**

GitHub:
https://github.com/shivenchaware995-spec

## License

This project is created for educational and portfolio purposes.

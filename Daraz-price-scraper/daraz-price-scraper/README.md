# Daraz-Price-Scraper
Automated price scraper built with Playwright and Python. Scrapes product listings (title, price, image, location, URL) from Daraz.pk using browser automation. Includes structured project setup, async Playwright, CSV export, and reusable scraping functions.


Daraz Price Scraper (Playwright + Python)

A fully automated Daraz.pk product scraper built using Python, Playwright, and AsyncIO.
This script extracts:

📌 Product Title

📌 Product URL

📌 Price

📌 Location

📌 Image URL

📌 Multiple pages support

📌 Export to CSV

This project is perfect for data extraction, pricing intelligence, e-commerce research, and automation learning.

🚀 Features

Uses Playwright for fast, reliable browser automation

Works with dynamic content and lazy-loaded product cards

Extracts all 40 items per page

Reusable async scraping function

Saves output to /output/products.csv

Clean folder structure

Beginner-friendly

📂 Project Structure
daraz-scraper/
│
├── src/
│   ├── scraper.py
│   ├── utils.py (optional)
│
├── output/
│   └── products.csv (auto-generated)
│
├── requirements.txt
└── README.md

📦 Installation
1. Clone Repo
git clone https://github.com/<your-username>/daraz-price-scraper.git
cd daraz-price-scraper

2. Install Requirements
pip3 install -r requirements.txt

3. Install Playwright Browsers
python3 -m playwright install chromium

▶️ Run the Scraper
python3 src/scraper.py


Default search keyword = laptop
Default pages = 2

You can change inside the script:

asyncio.run(scrape_daraz(product="mobile", pages=5))

📝 Output Example (CSV)
title	price	location	url	image
Dell Laptop	Rs. 70,000	Punjab	...	...
🛠 Tech Stack

Python 3.10+

Playwright

AsyncIO

Pandas

🤝 Contributing

Pull requests are welcome.
For major changes, please open an issue first to discuss.

📄 License

MIT License
Free to use for commercial & personal projects

import asyncio
from playwright.async_api import async_playwright
import pandas as pd
import os

async def scrape_daraz(product="laptop", pages=2):
    search_url = f"https://www.daraz.pk/catalog/?q={product}"

    os.makedirs("output", exist_ok=True)
    items = []

    async with async_playwright() as pw:
        browser = await pw.chromium.launch(headless=False)
        page = await browser.new_page()

        print(f"Searching for: {product}")
        await page.goto(search_url)

        for p in range(1, pages + 1):
            print(f"➡️ Scraping Page {p}")

            # All product rows
            rows = page.locator("//div[@class='Bm3ON']")
            count = await rows.count()
            print(f"Found {count} products on page {p}")

            for i in range(count):
                row = rows.nth(i)

                # Title
                try:
                    title = await row.locator("div.RfADt a").get_attribute("title")
                except:
                    title = "N/A"

                # URL
                try:
                    url = await row.locator("div.RfADt a").get_attribute("href")
                    if url.startswith("//"):
                        url = "https:" + url
                except:
                    url = "N/A"

                # Price
                try:
                    price = await row.locator("span.ooOxS").inner_text()
                except:
                    price = "N/A"

                # Location
                try:
                    location = await row.locator("div._6uN7R span").get_attribute("title")
                except:
                    location = "N/A"

                # Image URL
                try:
                    image = await row.locator("div.picture-wrapper img").get_attribute("src")
                except:
                    image = "N/A"

                items.append({
                    "title": title.strip(),
                    "url": url.strip(),
                    "price": price.strip(),
                    "location": location.strip(),
                    "image": image.strip()
                })

            # # Go to next page
            # next_btn = page.locator("//li[@title='Next Page']//a")
            # if await next_btn.count() == 0:
            #     print("No more pages.")
            #     break
            #
            # await next_btn.click()
            # await page.wait_for_timeout(2000)

        await browser.close()

    # Save to CSV
    df = pd.DataFrame(items)
    output_path = "output/products.csv"
    df.to_csv(output_path, index=False)
    print(f"✅ Scraping completed! Saved to {output_path}")


if __name__ == "__main__":
    asyncio.run(scrape_daraz(product="laptop", pages=2))

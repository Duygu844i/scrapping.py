import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

# Base URL for iPhone search results with pagination
base_url = "https://www.trendyol.com"

# Headers to mimic a real browser
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

# List to store the scraped data
iphone_data = []

# Number of pages to scrape
max_pages = 6  

for page in range(1, max_pages + 1):
    print(f"Scraping page {page}...")
    url = base_url.format(page)
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        products = soup.find_all('div', class_='p-card-chldrn-cntnr card-border')

        if not products:
            print("No more products found.")
            break

        for product in products:
            # Extract product title
            title_tag = product.find('span', class_='prdct-desc-cntnr-name')
            title = title_tag.text.strip() if title_tag else 'N/A'

            # Extract product price
            price_tag = product.find('div', class_='prc-box-dscntd')
            price = price_tag.text.strip() if price_tag else 'N/A'

            # Extract product link
            link_tag = product.find('a', href=True)
            if link_tag:
                product_link = "https://www.trendyol.com" + link_tag['href']
            else:
                product_link = 'N/A'

            iphone_data.append({
                'Model': title,
                'Price': price,
                'Link': product_link
            })
    else:
        print(f"Failed to retrieve page {page}: Status code {response.status_code}")
        break

    time.sleep(1)  

# Save the data to an Excel file
df = pd.DataFrame(iphone_data)
df.to_excel('iphone_models.xlsx', index=False)

print("Scraping completed. Data saved to 'iphone_models.xlsx'.")
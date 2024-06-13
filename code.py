//Access an e-commerce site.
//Execute a search for "Hindi Books".
//Scrape details like name, price, and user rating.
//Save the scraped data in a structured format (JSON or CSV).

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import json
import csv

# Setup WebDriver (adjust the path to the location of your WebDriver)
driver = webdriver.Chrome(executable_path='/path/to/chromedriver')

# Access the e-commerce site
driver.get('https://www.example.com')  # Replace with the actual URL

# Search for "Hindi Books"
search_box = driver.find_element(By.NAME, 'search')  # Adjust the search box locator
search_box.send_keys('Hindi Books')
search_box.send_keys(Keys.RETURN)

time.sleep(3)  # Wait for the page to load

# Scrape book details
books = driver.find_elements(By.CSS_SELECTOR, 'div.book-item')  # Adjust the selector

book_data = []

for book in books:
    name = book.find_element(By.CSS_SELECTOR, 'h2.book-title').text  # Adjust the selector
    price = book.find_element(By.CSS_SELECTOR, 'span.book-price').text  # Adjust the selector
    rating = book.find_element(By.CSS_SELECTOR, 'div.book-rating').text  # Adjust the selector

    book_data.append({
        'name': name,
        'price': price,
        'rating': rating
    })

# Save data to JSON
with open('books.json', 'w', encoding='utf-8') as f:
    json.dump(book_data, f, ensure_ascii=False, indent=4)

# Save data to CSV
with open('books.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=['name', 'price', 'rating'])
    writer.writeheader()
    writer.writerows(book_data)

# Close the browser
driver.quit()

print("Scraping completed and data saved.")

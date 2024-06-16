def scrape_book_details():
    books_data = []
    books = driver.find_elements(By.CSS_SELECTOR, ".s-main-slot .s-result-item")
    
    for book in books:
        try:
            name = book.find_element(By.CSS_SELECTOR, "h2 a span").text
            try:
                price = book.find_element(By.CSS_SELECTOR, ".a-price-whole").text
            except:
                price = "Price not available"
            try:
                rating = book.find_element(By.CSS_SELECTOR, ".a-icon-alt").get_attribute("innerText")
            except:
                rating = "Rating not available"
            
            books_data.append({
                "name": name,
                "price": price,
                "rating": rating
            })
        except Exception as e:
            print(f"Could not retrieve book details: {e}")
    
    return books_data

# Function to save data as JSON
def save_as_json(data, filename="books.json"):
    with open(filename, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)

# Function to save data as CSV
def save_as_csv(data, filename="books.csv"):
    keys = data[0].keys()
    with open(filename, 'w', newline='', encoding='utf-8') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=keys)
        writer.writeheader()
        writer.writerows(data)

try:
    # Navigate to the e-commerce site (example: Amazon)
    driver.get("https://www.amazon.in")

    # Find the search bar and enter "Hindi Books"
    search_bar = driver.find_element(By.ID, "twotabsearchtextbox")
    search_bar.send_keys("Hindi Books")
    search_bar.send_keys(Keys.RETURN)

    # Wait for the search results to load
    time.sleep(5)

    # Scrape the book details
    books_data = scrape_book_details()

    # Save the data as JSON and CSV
    save_as_json(books_data)
    save_as_csv(books_data)

finally:
    # Close the browser
    driver.quit()

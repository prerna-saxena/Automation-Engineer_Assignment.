# Assuming 'scraped_data' is a list of dictionaries with keys 'name' and 'price'
# Example data structure of 'scraped_data':
# scraped_data = [{"name": "Product A", "price": "100.00"}, {"name": "Product B", "price": "50.00"}, ...]

# Split OCR text into lines to process each line
ocr_lines = ocr_text.splitlines()

# Initialize lists to store matched and unmatched data
matched_data = []
unmatched_data = []

# Compare OCR-derived data with Selenium-scraped data
for scraped_item in scraped_data:
    scraped_name = scraped_item['name']
    scraped_price = scraped_item['price']
    
    found = False
    
    # Search for scraped_name in OCR-derived text lines
    for line in ocr_lines:
        if scraped_name in line:
            # Extract price from OCR line (assuming it follows the format near the name)
            # Implement your logic to extract price from the OCR line based on your OCR text format
            # Here's a hypothetical example assuming the price follows the name directly
            ocr_price = line.split(scraped_name)[-1].strip()
            
            # Compare prices
            if scraped_price == ocr_price:
                matched_data.append({"name": scraped_name, "scraped_price": scraped_price, "ocr_price": ocr_price})
            else:
                unmatched_data.append({"name": scraped_name, "scraped_price": scraped_price, "ocr_price": ocr_price})
            
            found = True
            break
    
    # If scraped_name is not found in OCR text
    if not found:
        unmatched_data.append({"name": scraped_name, "scraped_price": scraped_price, "ocr_price": "Not found"})

# Print results
print("Matched Data:")
for item in matched_data:
    print(item)

print("\nUnmatched Data:")
for item in unmatched_data:
    print(item)

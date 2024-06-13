import pytesseract

def extract_text_from_image(image_path):
    # Load the screenshot
    img = Image.open(image_path)

    # Perform OCR on the image
    text = pytesseract.image_to_string(img, lang='eng')

    print("Extracted Text:")
    print(text)
    return text

def parse_ocr_text(ocr_text):
    # Assuming OCR text format is consistent and parsing it to extract product names and prices
    lines = ocr_text.split('\n')
    products = []
    for line in lines:
        parts = line.split()
        if len(parts) > 1:
            price = parts[-1]
            name = ' '.join(parts[:-1])
            products.append({'name': name, 'price': price})
    return products

def compare_data(web_data, ocr_data):
    discrepancies = []
    ocr_dict = {item['name']: item['price'] for item in ocr_data}

    for item in web_data:
        web_name = item['name']
        web_price = item['price']
        ocr_price = ocr_dict.get(web_name)
        
        if ocr_price and web_price != ocr_price:
            discrepancies.append({
                'name': web_name,
                'web_price': web_price,
                'ocr_price': ocr_price
            })
    
    return discrepancies

def generate_report(discrepancies):
    report_path = 'discrepancies_report.csv'
    with open(report_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=['name', 'web_price', 'ocr_price'])
        writer.writeheader()
        writer.writerows(discrepancies)
    print(f"Report generated at {report_path}")

# Uncomment to run the full workflow
# web_data = scrape_web_data()
# screenshot_path = capture_mobile_screenshot()
# ocr_text = extract_text_from_image(screenshot_path)
# ocr_data = parse_ocr_text(ocr_text)
# discrepancies = compare_data(web_data, ocr_data)
# generate_report(discrepancies)

product_divs = soup.find_all('div', class_='s-result-item')

# Loop through each product div and extract the title, rating, and price
for product in product_divs:
    # Get product title
    title_element = product.find('span', class_='a-size-medium a-color-base a-text-normal')
    title = title_element.get_text() if title_element else "N/A"
    
    # Get product rating
    rating_element = product.find('span', class_='a-icon-alt')
    rating = rating_element.get_text() if rating_element else "N/A"
    
    # Get product price (whole part and fraction)
    price_whole_element = product.find('span', class_='a-price-whole')
    price_fraction_element = product.find('span', class_='a-price-fraction')

    if price_whole_element and price_fraction_element:
        price = f"{price_whole_element.get_text()}.{price_fraction_element.get_text()}"
    else:
        price = "N/A"
    
    # Print the extracted data
    print(f"Product Title: {title}")
    print(f"Rating: {rating}")
    print(f"Price: {price}")
    print('---')



#outcome:
# Product Title: PlayStation®5 console (slim) with EA SPORTS College Football 25
# Rating: 4.8 out of 5 stars
# Price: 496.00
# ---
# Product Title: Xbox Series X
# Rating: 4.7 out of 5 stars
# Price: 499.00
# ---
# Product Title: Nintendo Switch OLED Model
# Rating: 4.9 out of 5 stars
# Price: 349.99
# ---

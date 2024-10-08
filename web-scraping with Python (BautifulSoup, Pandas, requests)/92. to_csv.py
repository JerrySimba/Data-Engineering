#convert data to csv
all_product_data = []

# Loop through pages 1 to 10
for page in range(1, 11):
    url = f"https://www.amazon.com/s?k=playstation+5&page={page}"
    headers = {"User-Agent": "Mozilla/5.0"}
    
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find product containers
    products = soup.select('.s-main-slot .s-result-item')

    for product in products:
        title = product.select_one('h2 .a-text-normal')
        release_date = product.select_one('.a-row .a-size-base.a-color-secondary')
        ratings = product.select_one('.a-icon-alt')
        price = product.select_one('.a-color-base')

        # Extract and clean data
        all_product_data.append({
            "Title": title.text.strip() if title else "Title not found",
            "Release Date": release_date.text.strip() if release_date else "Release Date not found",
            "Ratings": ratings.text.strip() if ratings else "Ratings not found",
            "Price": price.text.strip() if price else "Price not found"
        })

# Create DataFrame from collected data
df = pd.DataFrame(all_product_data)

# Export DataFrame to CSV
df.to_csv("playstation_5_products.csv", index=False)
df = pd.read_csv("playstation_5_products.csv")
display(df)

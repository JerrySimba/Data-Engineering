#loop through first ten pages 
for page in range(1, 11):  # Iterate through pages 1 to 10
    url = base_url.format(page)
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extract product information
    products = soup.select('.s-main-slot .s-result-item')

    for product in products:
        # Extract the product title
        title = product.select_one('.a-size-medium.a-color-base.a-text-normal')
        title_text = title.text.strip() if title else 'Title not found'

        # Extract the product release date
        release_date = 'Release date not found'
        for element in product.select('.a-size-base.a-color-secondary.a-text-normal'):
            date_text = element.text.strip()
            # Match date formats (e.g., Dec 10, 2023)
            if re.search(r'[A-Za-z]{3,9} \d{1,2}, \d{4}', date_text):
                release_date = date_text
                break

        # Extract the ratings
        ratings = product.select_one('.a-icon-alt')
        ratings_text = ratings.text.strip() if ratings else 'Ratings not found'
      # Print the extracted values
        print(f"Title: {title_text}")
        print(f"Release Date: {release_date}")
        print(f"Ratings: {ratings_text}")
        print('-' * 40)

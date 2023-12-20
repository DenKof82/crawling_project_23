import requests
from lxml import html as HTML
import pandas as pd
import time
import os
import csv
import config


def download_image(image_url, folder_path, file_name):
    try:
        response = requests.get(image_url)
        if response.status_code == 200:
            file_path = os.path.join(folder_path, file_name)
            with open(file_path, 'wb') as file:
                file.write(response.content)
            return file_path
    except Exception as e:
        print(f"Error downloading image: {e}")
    return None

def crawl_vitamin_c_products(time_limit, source, return_format, download_images=False):
    start_time = time.time()
    data = {'product_name': [], 'price': [], 'image_url': [], 'image_path': []}
    image_folder = 'downloaded_images'

    if download_images and not os.path.exists(image_folder):
        os.makedirs(image_folder)

    try:
        response = requests.get(source)
        if response.status_code != 200:
            return "Failed to retrieve data from the source"

        tree = HTML.fromstring(response.content)

        for product in tree.xpath("//div[contains(@class, 'product-item')]"):
            product_name = product.xpath("./input[@name='productName']/@value")[0].strip()
            price = product.xpath("./input[@name='productPrice']/@value")[0].strip()
            image_url = product.xpath('.//img/@src')[0]

            data['product_name'].append(product_name)
            data['price'].append(price)
            data['image_url'].append(image_url)

            if download_images:
                image_file_name = f"{product_name.replace('/', '_')}.jpg"  # Replace '/' with '_' to avoid file path issues
                image_path = download_image(image_url, image_folder, image_file_name)
                data['image_path'].append(image_path if image_path else 'Not Found')

            if time.time() - start_time > time_limit:
                break

    except Exception as e:
        return f"An error occurred: {e}"

    if return_format == 'csv':
        csv_file_path = 'vitamin_c_products.csv'
        with open(csv_file_path, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['Product Name', 'Price', 'Image URL', 'Image Path'])  # Column headers
            for product_name, price, image_url, image_path in zip(data['product_name'], data['price'], data['image_url'], data['image_path']):
                writer.writerow([product_name, price, image_url, image_path])
        return f"Data saved to CSV file: {csv_file_path}"
    else:
        return data

# Example function call
result = crawl_vitamin_c_products(
    time_limit=config.TIME_LIMIT,
    source=config.SOURCE_URL,
    return_format=config.RETURN_FORMAT,
    download_images=config.DOWNLOAD_IMAGES
)
print(result)
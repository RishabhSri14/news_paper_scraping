import requests
import csv
import os
from bs4 import BeautifulSoup
import re
import json

def remove_dims(url):
    # Regular expression pattern to match the dimensions
    pattern = r'-(\d+x\d+)\.'

    # Search for the pattern in the URL
    match = re.search(pattern, url)

    if match:
        # Remove the dimensions from the URL
        modified_url = url[:match.start()] + "." + url[match.end():]
        return modified_url

    return url  # Return the original URL if dimensions are not found

# Specify the main directory to store sub-directories and images
main_directory = "Product_Ads"

# Create the main directory if it doesn't exist
os.makedirs(main_directory, exist_ok=True)

json_folder = "output_products/"

json_file_path = os.path.join(json_folder,"data.json")
data = []

with open(json_file_path, "w") as json_file:
    json.dump(data, json_file, indent=4)

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

# Read the CSV file
with open("products_category.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)  # Skip the header row

    for row in reader:
        product_category, url = row

        # Create a sub-directory based on the product category
        sub_directory = os.path.join(main_directory, product_category)
        os.makedirs(sub_directory, exist_ok=True)

        # Start with page 1
        page_number = 1

        while True:
            # Construct the URL for the current page
            page_url = f"{url}/page/{page_number}/"

            # Send a GET request to the web page
            response = requests.get(page_url, headers=headers)

            # Create a BeautifulSoup object to parse the HTML content
            soup = BeautifulSoup(response.content, "html.parser")

            # Find all the image tags on the page
            image_tags = soup.find_all("img")

            # Extract the source (src) attribute from each image tag
            image_links = [img["src"] for img in image_tags]

            image_links = [remove_dims(img) for img in image_links]

            if len(image_links) == 0:
                break
            else:
                # Download the image links into the sub-directory
                for i in range(0, len(image_links), 2):
                    image_url = image_links[i]
                    image_name = image_url.split("/")[-1]
                    image_path = os.path.join(sub_directory, image_name)

                    # Send a GET request to download the image
                    image_response = requests.get(image_url)

                    # Save the image to the sub-directory
                    with open(image_path, "wb") as image_file:
                        image_file.write(image_response.content)
                    #add to json : unique id, newspaper name, language, source url, taken from(final url: url_with_page)
                    attributes = {
                        "ID": image_name[:3]+image_name[-3:]+product_category[0:3],
                        "Ads Category" : "Product Ads",
                        "Type of Products": product_category,
                        "Source URL": image_url,
                        "Taken From": url,
                    }
                    data.append(attributes)

            # Move to the next page
            page_number += 1
        
        print(f"Downloaded Product Category : {product_category} with {page_number - 1} pages")
        with open(json_file_path, "w") as json_file:
            json.dump(data, json_file, indent=4)

with open(json_file_path, "w") as json_file:
    json.dump(data, json_file, indent=4)
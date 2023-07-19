import urllib
import requests
import time
import  os
import json
def download_image(image_url, save_path):
    try:
        response = requests.get(image_url)
        response.raise_for_status()  # Check if the request was successful
        with open(save_path, 'wb') as file:
            file.write(response.content)
        print("Image downloaded successfully!")
    except requests.exceptions.RequestException as e:
        print(f"Error downloading image- {e}")

for brand in os.listdir('./Data'):
    print('\nDownloading Images for brand: ',brand,'\n')
    brand_name = brand[:brand.rfind('.')]
    if brand_name not in os.listdir('./images'):
        os.mkdir(f'./images/{brand_name}') 
        
    parent_image_folder = f'./images/{brand_name}/'
    with open('./Data/'+brand) as f:
        data = json.load(f)
    print('Total number of images:', str(len(data)))

    for i, obj in enumerate(data):
        links = obj['url']
        ext = links[links.rfind('.'):]
        # time.sleep(5)
        print(f'Downloading image number {i+1}...')
        urllib.request.urlretrieve(links, parent_image_folder+str(i+400)+ext)
        #OR
    # download_image(links, f'{i+1}{ext}')
        
    
    
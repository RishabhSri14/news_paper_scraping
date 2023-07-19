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
data = ["https://newspaperads.ads2publish.com/wp-content/uploads/2021/01/@home-by-nilkamal-furniture-ad-bangalore-times-23-01-2021.jpg",
"https://newspaperads.ads2publish.com/wp-content/uploads/2019/07/at-home-furniture-the-big-sale-additional-10-off-ad-bangalore-times-19-07-2019.png"
, 
"https://newspaperads.ads2publish.com/wp-content/uploads/2019/04/at-home-furniture-minimum-30-off-last-4-days-ad-bangalore-times-26-04-2019.png"
,

"https://newspaperads.ads2publish.com/wp-content/uploads/2019/04/at-home-furniture-summer-vibes-fest-upto-40-off-ad-times-of-india-bangalore-22-03-2019.png"
,

"https://newspaperads.ads2publish.com/wp-content/uploads/2019/03/at-home-furniture-the-big-sale-flat-60-off-ad-times-of-india-bangalore-22-02-2019.png"
,

"https://newspaperads.ads2publish.com/wp-content/uploads/2019/01/at-home-furniture-big-sale-flat-60-off-ad-bangalore-times-18-01-2019.png"
,

"https://newspaperads.ads2publish.com/wp-content/uploads/2019/01/at-home-furniture-the-big-sale-upto-50-off-ad-times-of-india-bangalore-12-01-2019.png"
,

"https://newspaperads.ads2publish.com/wp-content/uploads/2018/12/at-home-furniture-the-big-sale-upto-50-off-ad-bangalore-times-28-12-2018.png"
,

"https://newspaperads.ads2publish.com/wp-content/uploads/2018/12/at-home-furniture-big-sale-upto-50-off-ad-times-of-india-bangalore-14-12-2018.png"
,

"https://newspaperads.ads2publish.com/wp-content/uploads/2018/12/at-home-furniture-anniversary-celebration-upto-40-off-ad-times-of-india-bangalore-30-11-2018.png"
,

"https://newspaperads.ads2publish.com/wp-content/uploads/2018/11/at-home-furniture-anniversary-celebration-upto-40-off-ad-times-of-india-bangalore-23-11-2018.png"
,

"https://newspaperads.ads2publish.com/wp-content/uploads/2018/10/at-home-furniture-the-celebration-collection-upto-50-off-ad-times-of-india-chennai-26-10-2018.png"
,

"https://newspaperads.ads2publish.com/wp-content/uploads/2018/08/at-home-furniture-the-big-sale-flat-60-off-ad-times-of-india-bangalore-04-08-2018.png"
,

"https://newspaperads.ads2publish.com/wp-content/uploads/2018/07/at-home-furniture-the-big-sale-flat-60-off-ad-times-of-india-bangalore-20-07-2018.png"
,

"https://newspaperads.ads2publish.com/wp-content/uploads/2018/07/at-home-furniture-the-big-sale-flat-60-off-ad-times-of-india-bangalore-13-07-2018.png"
,

"https://newspaperads.ads2publish.com/wp-content/uploads/2018/06/at-home-furniture-shades-of-the-season-festival-upto-40-off-ad-bangalore-times-01-06-2018.png"
,

"https://newspaperads.ads2publish.com/wp-content/uploads/2018/05/shades-of-the-season-festival-up-to-40-off-at-home-ad-deccan-chronicle-hyderabad-18-05-2018.png"
,

"https://newspaperads.ads2publish.com/wp-content/uploads/2018/04/at-home-furniture-super-sale-upto-60-off-11-most-amazing-days-ad-times-of-india-ahmedabad-20-04-2018.png"
,

"https://newspaperads.ads2publish.com/wp-content/uploads/2018/04/at-home-furniture-super-sale-upto-60-off-11-most-amazing-days-ad-bangalore-times-13-04-2018.png"
,

"https://newspaperads.ads2publish.com/wp-content/uploads/2018/02/at-home-the-big-sale-upto-51-off-ad-times-of-india-bangalore-23-02-2018.png"
,

"https://newspaperads.ads2publish.com/wp-content/uploads/2018/01/the-big-sale-upto-51-off-at-home-ad-the-hindu-bangalore-19-01-2018.jpg"
,

"https://newspaperads.ads2publish.com/wp-content/uploads/2017/12/home-the-big-sale-upto-51-off-ad-the-hindu-chennai-22-12-2017.jpg"
,

"https://newspaperads.ads2publish.com/wp-content/uploads/2017/12/@home-the-big-sale-upto-51-off-no-room-for-reasons-ad-ahmedabad-times-15-12-2017.png"
,

"https://newspaperads.ads2publish.com/wp-content/uploads/2017/11/at-home-furniture-sit-back-relax-ad-bombay-times-24-11-2017.png"
,

"https://newspaperads.ads2publish.com/wp-content/uploads/2017/11/@home-lets-make-it-a-november-to-remember-anniversary-sale-ad-ahmedabad-times-03-11-2017.jpg"
,

"https://newspaperads.ads2publish.com/wp-content/uploads/2017/10/at-hoe-furniture-upto-50-off-ad-bombay-times-28-10-2017.jpg"
,

"https://newspaperads.ads2publish.com/wp-content/uploads/2017/10/@home-the-grand-festive-celebration-upto-50-off-ad-times-of-india-ahmedabad-14-10-17.jpg"
,

"https://newspaperads.ads2publish.com/wp-content/uploads/2017/10/@home-the-grand-festive-celebration-upto-50-off-shop-at-the-nearest-store-or-visit-www-at-home-co-in-ad-deccan-chronicle-hyderabad-14-10-2017.png"
,

"https://newspaperads.ads2publish.com/wp-content/uploads/2017/10/at-home-furniture-the-grand-festive-celebration-upto-50-off-ad-bombay-times-29-09-2017.jpg"
,

"https://newspaperads.ads2publish.com/wp-content/uploads/2017/09/@home-furniture-the-grand-festive-celebration-upto-50-off-ad-ahmedabad-times-22-9-17.jpg"
,

"https://newspaperads.ads2publish.com/wp-content/uploads/2017/09/@home-shop-this-look-at-out-store-or-visit-online-last-3-days-upto-50-off-ad-chennai-times-02-9-17.jpg"
,

"https://newspaperads.ads2publish.com/wp-content/uploads/2017/08/custom-kitchens-@home-your-kitchen-your-way-ad-property-times-mumbai-25-8-17.jpg"
,

"https://newspaperads.ads2publish.com/wp-content/uploads/2017/08/@home-the-freedom-sale-special-offers-upto-50-ad-times-of-india-bangalore-12-08-2017.jpg"
,

"https://newspaperads.ads2publish.com/wp-content/uploads/2017/08/@home-the-big-sale-ad-chennai-times-14-7-2017.jpg"
,
"https://newspaperads.ads2publish.com/wp-content/uploads/2017/08/@home-furniture-the-big-sale-last-4-days-ad-bangalore-times-28-7-2017.jpg"
]

brand = 'home'
if brand not in os.listdir('./images'):
    os.mkdir(f'./images/{brand}') 
    
parent_image_folder = f'./images/{brand}/'
print('Total number of images:', str(len(data)))

for i, links in enumerate(data):
    ext = links[links.rfind('.'):]
    # time.sleep(5)
    print(f'Downloading image number {i+1}...')
    urllib.request.urlretrieve(links, parent_image_folder+str(i+400)+ext)
    #OR
    # download_image(links, f'{i+1}{ext}')
        
    
    
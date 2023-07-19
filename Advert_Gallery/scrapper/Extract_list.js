const puppeteer = require('puppeteer');
var fs = require('fs')
const brand_names = require('./brand_names.json')
function extract_brand_links() {
  // First go to https://www.advertgallery.com/product-category/advertisements-by-brand
  console.log("Extracting Brand Links")
  x = document.getElementsByClassName("products columns-4")[0].children
  for (var i = 0; i < x.length; i++) {
    html = x[i].innerHTML
    link = html.split('"')[3]
    console.log(link)
  }

}
function extract_img_links(brand) {
  // First go to https://www.advertgallery.com/product-category/advertisements-by-brand/<brand_name>
  x = document.getElementsByClassName("products columns-4")[0].children
  var data = []
  for (var i = 0; i < x.length; i++) {
    html = x[i].innerHTML
    web_link = html.substring(html.indexOf("href=") + 6).split('"')[0]
    thumb_link = html.substring(html.indexOf("src=") + 5).split('"')[0]
    img_link = thumb_link.substring(0, thumb_link.lastIndexOf('-')) + thumb_link.substring(thumb_link.lastIndexOf('.'))
    // console.log(img_link)
    data.push({ 'Sno': 400 + i, 'title': title, 'url': img_link, 'taken from': web_link })
  }
  fs.writeFile("../Data/" + brand + ".json", JSON.stringify(data), err => {

    if (err) throw err;

    console.log("Done writing"); // Success
  });
}

async function openURLAndExecuteFunction(url) {
  try {
    // const browser = await puppeteer.launch({executablePath: '/mnt/c/Users/risha/Downloads/chromedriver.exe', timeout: 60000, headless: false});
    // console.log('YESSSSSSSS')
    const browser = await puppeteer.launch();
    const page = await browser.newPage();
    await page.goto(url);
    const data = await page.evaluate(() => {
      var data = []
      x = document.getElementsByClassName("products columns-4")[0].children
      for (var i = 0; i < x.length; i++) {
        html = x[i].innerHTML
        web_link = html.substring(html.indexOf("href=") + 6).split('"')[0]
        thumb_link = html.substring(html.indexOf("src=") + 5).split('"')[0]
        img_link = thumb_link.substring(0, thumb_link.lastIndexOf('-')) + thumb_link.substring(thumb_link.lastIndexOf('.'))
        temp = img_link.split('/')
        var title = (temp[temp.length - 1].substring(0,temp[temp.length - 1].lastIndexOf('.'))).replace('-',' ')
        // console.log(img_link)
        data.push({ 'Sno': 400 + i, 'title': title, 'url': img_link, 'taken from': web_link })
      }      
      return data;
    });
    await browser.close();
    return data;
  } catch (err) {
    console.error('Error:', err);
  }
}

const result = async function(){
  for (var i =0;i<brand_names.length;i++){

    var brand = brand_names[i]
    var url = 'https://www.advertgallery.com/product-category/advertisements-by-brand/' + brand + '/'
  
    const json_data = await openURLAndExecuteFunction(url);
    console.log(json_data)
    fs.writeFile("../Data/" + brand + ".json", JSON.stringify(json_data), err => {
    
      if (err) throw err;
    
      console.log("Done writing"); // Success
    });
  }
  return json_data 
}
result()

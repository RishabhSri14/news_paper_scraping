
var fs = require("fs");
function extract_brand_links(){
    // First go to https://www.advertgallery.com/product-category/advertisements-by-brand
    console.log("Extracting Brand Links")
    x = document.getElementsByClassName("products columns-4")[0].children
    for (var i = 0; i < x.length; i++){
        html = x[i].innerHTML
        link = html.split('"')[3]
        console.log(link)
    }

}
function extract_img_links(brand){
    // First go to https://www.advertgallery.com/product-category/advertisements-by-brand/<brand_name>
    x = document.getElementsByClassName("products columns-4")[0].children
    var data =[]
    for (var i = 0; i < x.length; i++){
        html = x[i].innerHTML
        web_link = html.substring(html.indexOf("href=")+6).split('"')[0]
        thumb_link = html.substring(html.indexOf("src=")+5).split('"')[0]
        img_link = thumb_link.substring(0,thumb_link.lastIndexOf('-'))+thumb_link.substring(thumb_link.lastIndexOf('.'))
        // console.log(img_link)
        data.push({'Sno': 400+i,'title': title,'url': img_link, 'taken from': web_link})
    }
    fs.writeFile("../Data/"+brand+".json", JSON.stringify(data), err => {
     
      if (err) throw err; 
     
      console.log("Done writing"); // Success
  });
}
var brand ='home'
var url = 'https://www.advertgallery.com/product-category/advertisements-by-brand/'+brand+'/'
// window.open('https://www.advertgallery.com/product-category/advertisements-by-brand/'+brand+'/');
// setTimeout(function() {
//     // Call your JavaScript function here
//     extract_brand_links();
//   }, 10000);
// // window.close();


// const open = require('open');

// // Open the URL
// open(url)
//   .then(() => {
//     // Execute your JavaScript function here
//     extract_img_links();
//   })
//   .catch(err => {
//     console.error('Error:', err);
//   });


const puppeteer = require('puppeteer');

async function openURLAndExecuteFunction(url) {
  try {
    // const browser = await puppeteer.launch({executablePath: '/mnt/c/Users/risha/Downloads/chromedriver.exe', timeout: 60000, headless: false});
    // console.log('YESSSSSSSS')
    const browser = await puppeteer.launch({
      executablePath: '/mnt/c/Program Files/Google/Chrome/Application/chrome.exe', // Replace with the actual path to your Chrome executable on Windows
      // args: ['--no-sandbox'], // Optionally disable sandbox if needed
      headless: false,
    });
    const page = await browser.newPage();
    await page.goto(url);
    // Execute your JavaScript function here
    await page.evaluate(() => {
      extract_img_links(brand);
    });

    await browser.close();
  } catch (err) {
    console.error('Error:', err);
  }
}

// Replace 'https://www.example.com' with the URL you want to open
openURLAndExecuteFunction(url);

// const axios = require('axios');
// const { JSDOM } = require('jsdom');
// const { window } = new JSDOM('<!DOCTYPE html><html><body></body></html>');
// const $ = require('jquery')(window);
// async function openURLAndExecuteFunction(url, jsFunction) {
//   try {
//     const response = await axios.get(url);
//     const dom = new JSDOM(response.data, { runScripts: 'dangerously', resources: 'usable', window });
//     const result = dom.window.eval(jsFunction);

//     return result;
//   } catch (error) {
//     throw error;
//   }
// }

// // Example usage:
// const jsFunction = () => {
//   // Replace this function with the JavaScript function you want to execute on the page
//   // Your code can now use the injected jQuery instance as '$' or 'jQuery'
//   return $('title').text(); // Return the page title using jQuery
// };

// openURLAndExecuteFunction(url, jsFunction)
//   .then((result) => {
//     console.log('Result:', result);
//   })
//   .catch((error) => {
//     console.error('Error:', error);
//   });


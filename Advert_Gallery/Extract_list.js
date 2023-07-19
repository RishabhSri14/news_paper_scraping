
// var fs = require("fs");
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
function extract_img_links(){
    // First go to https://www.advertgallery.com/product-category/advertisements-by-brand/<brand_name>
    x = document.getElementsByClassName("products columns-4")[0].children
    for (var i = 0; i < x.length; i++){
        html = x[i].innerHTML
        web_link = html.substring(html.indexOf("href=")+6).split('"')[0]
        thumb_link = html.substring(html.indexOf("src=")+5).split('"')[0]
        img_link = thumb_link.substring(0,thumb_link.lastIndexOf('-'))+thumb_link.substring(thumb_link.lastIndexOf('.'))
        console.log(img_link)
    }
}

window.open('https://www.advertgallery.com/product-category/advertisements-by-brand/home');
setTimeout(function() {
    // Call your JavaScript function here
    extract_brand_links();
  }, 10000);
// window.close();
window.open('https://www.advertgallery.com/product-category/advertisements-by-brand/');
// Now run the following in the console:

x = document.getElementsByClassName("products columns-4")[0].children
    for (var i = 0; i < x.length; i++){
        html = x[i].innerHTML
        link = html.split('"')[3]
    }
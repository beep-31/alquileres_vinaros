let thumbnail = document.querySelector('#thumbnail'),
    thumbnail_close = document.querySelector('#thumbnail-close'),
    photos = document.querySelectorAll('.element'),
    thumbnail_image = document.querySelector('#thumbnail-image'),
    left_btn = document.querySelector('#left'),
    right_btn = document.querySelector('#right'),
    main = document.querySelector('#main'),
    thumb_title = document.querySelector('#thumb-title'),
    thumb_description = document.querySelector('#thumb-description'),
    folder_title = document.querySelector('.main-title').getAttribute("data-title");


console.log(photos.length);
var current_photo_id;

let photo_list = []
for (let i=0; i<=photos.length - 1; i++){
    item = photos[i].style.backgroundImage
    photo_list.push(item);
}

for (let i=1; i<=photos.length; i++){
    photos[i-1].id = i.toString(10);
    if(photos.length > 9 && i>9){
        photos[i-1].id = i.toString(10);
    }

}

for (let photo of photos){
    photo.addEventListener('click', function(){
        thumbnail.style.transition = '1s';
        main.style.filter = 'blur(2px) grayscale(100%)';
        main.style.webkitFilter = 'blur(2px) grayscale(100%)';
        if(thumbnail.style.left == '-100vw'){
            current_photo_id = photo.id;
            thumb_title.innerHTML = photo.attributes[1].nodeValue;
            thumb_description.innerHTML = photo.attributes[2].nodeValue;
            thumbnail_image.style.backgroundImage = photo_list[current_photo_id-1];
            thumbnail.style.left = '0px';
            thumbnail.style.opacity = '1';
        }
    });
}

thumbnail_close.addEventListener('click', function(){
    thumbnail.style.opacity = '0';
    thumbnail.style.left = '100vw';
    main.style.filter = 'blur(0px) grayscale(0%)';
    main.style.webkitFilter = 'blur(0px) grayscale(0%)';
    if(thumbnail.style.left == '100vw'){
        setTimeout(() => {
            thumbnail.style.transition = '0s';
            thumbnail.style.left = '-100vw';
        }, 450)
    }
});

right_btn.addEventListener('click', function(){
    current_photo_id++;
    if(current_photo_id > photos.length-1){
        current_photo_id = 1;
    }
    thumb_title.innerHTML = photos[parseInt(current_photo_id)-1].attributes[1].nodeValue;
    thumb_description.innerHTML = photos[parseInt(current_photo_id)-1].attributes[2].nodeValue
    thumbnail_image.style.backgroundImage = photo_list[current_photo_id-1];
});

left_btn.addEventListener('click', function(){
    current_photo_id--;
    if(current_photo_id == 0){
        current_photo_id = photo_list.length;
    } 
    thumb_description.innerHTML = photos[parseInt(current_photo_id)-1].attributes[2].nodeValue
    thumb_title.innerHTML = photos[parseInt(current_photo_id)-1].attributes[1].nodeValue;
    thumbnail_image.style.backgroundImage = photo_list[current_photo_id-1];

});


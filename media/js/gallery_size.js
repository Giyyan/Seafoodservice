function set_width_to_media_files() {

    var width_of_media = parseInt(document.getElementById('video_gallery').offsetWidth*(0.94) / 3);
    var  videos = document.getElementsByTagName('video');
    for(var i=0; i<videos.length; i++){
        videos[i].width = width_of_media;
    }
    var photos = document.getElementsByClassName('img_in_gallery');
    for(var i=0; i<photos.length; i++){
        photos[i].width = width_of_media;
    }

}
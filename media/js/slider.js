$(document).ready(function () {
	var slides = [];
	var preloadImages = [];
	var controls = [];
	var currentImage = 0;
	$.ajax({
		url: "/get_slide_images/",
		dataType: 'json',
		success: function(resp) {
			if(resp.slides){
				slides = resp.slides;
				var parent = document.getElementById('slider');
				var image = document.createElement("image");
				image.src = slides[0];
				image.id = "img";
				image.style = "display: inline;";
				parent.appendChild(image);
				var div_arrows = document.createElement('div');
				div_arrows.className = "arrows";
				var div_left = document.createElement('div');
				div_left.className = "left";
				var div_right = document.createElement('div');
				div_right.className = "right";
				div_arrows.appendChild(div_right);
				div_arrows.appendChild(div_left);
				parent.appendChild(div_arrows);
				
				var div_controls = document.createElement('div');
				div_controls.className = "controls";
				for( var i=0; i<slides.length; i++ ){
					var div = document.createElement('div');
					div.id = i+"_controls";
					div.click(function () {
						changeControls(i);
					}); 
					controls.push("#"+i+"_controls");
					if (i == 0){
						div.className = "active_control";
						currentImage = 0;
					}
					div_controls.appendChild(div);
				}
				parent.appendChild(div_controls);
				preloadImages = slides;
			} else {
				alert("Error: "+resp.errors);
				for (error in resp.errors){								
					var id = document.getElementById('id_' + error).parentNode;
					id.appendChild(create_label(error+" is "+resp.errors[error], "id_error_" + error));
				}
			}
		},
		error: function(resp) {
			err_dict = {};
			for(e in resp){
				err_dict[e] = resp[e];
				console.log(resp[e]);
			}
			alert("Error: "+err_dict);
		},

	});
  
$(".right").click(listRight);
$(".left").click(listLeft);
    
function listLeft(){
    if(currentImage != 0) {
        currentImage--;
        changeControls(currentImage);
    }
    else{
        currentImage = slides.length-1;
        changeControls(currentImage);   
    }
}

function listRight(){
        if(currentImage != slides.length-1) {
        currentImage++;
        changeControls(currentImage);
    }
    else{
        currentImage = 0;
        changeControls(currentImage);   
    }
}

function changeControls(number){
    for	(var index = 0; index < controls.length; index++) {
        if(index != number){
            $(controls[index]).removeClass('active_control');    
        }
        else{
            $(controls[index]).addClass('active_control');
            currentImage = index;
            changeImage();
        }
    }    
}
      
function changeImage(){
    $("#img").fadeToggle("fast");
    setTimeout(function() {
    $("#img").attr("src", slides[currentImage]);
    }, 200);
    $("#img").fadeToggle("fast");
}

var delay = 7000;
setTimeout(startSlider,delay);
    
function startSlider(){
    listRight();
    setTimeout(startSlider,delay);
}
function preloadImages()
{
	alert("PreloadImages()"+arguments);
  for(var i = 0; i<arguments.length; i++)
    {
	$("<img />").attr("src", arguments);
    }
} 
    var animationSpeed = 1000;
    var currentLogoSlide = 3;
    var $carousel_Slides = $(".carousel_slides");
        
    $(".logo_right").click(function() {
        if(currentLogoSlide != $carousel_Slides.length){
            currentLogoSlide += 3;
            $("#carousel_slides").animate({'margin-left': '-=633'}, animationSpeed);
        }
        else{
            currentLogoSlide = 3;
            $("#carousel_slides").animate({'margin-left': '0'}, animationSpeed);
        }
        
    });
    
    $(".logo_left").click(function() {
        if(currentLogoSlide != 3){
             currentLogoSlide -= 3;
            $("#carousel_slides").animate({'margin-left': '+=633'}, animationSpeed);
        }
        else{
            currentLogoSlide = 3;
             $("#carousel_slides").animate({'margin-left': '0'}, animationSpeed);
        }
    });
    

});
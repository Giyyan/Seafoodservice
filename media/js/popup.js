$(document).ready(function () {
    $(".photo_img img").click(function () {
    $("#wrap_frame, #overlay").fadeIn(300);
    });
    $("#overlay, #close2").click(function () {
      $("#wrap_frame, #overlay").fadeOut(300);
    });
      positionCenter($("#wrap_frame"));
    
    var licount=$(".photo_img").length;
$("#wrapper .photo_img").each(function() {
    licount++;
    $(this).attr('rel',licount);
});

  var current_li=0;
 $(".portfolio li img").click(function () {
    var src = $(this).attr("src");
    current_li = parseInt($(this).parent().attr('rel'));
    var cur_desc = $("li[rel="+current_li+"]").find(".photo_descr").html();
    $(".description").html(cur_desc);
    $("#big_photo_img").attr("src", src);
    $("#wrap_frame, #overlay, .description").fadeIn();
     
});
    $("#right_arrow").click(function() {
    if(current_li<licount)
	{
	    var next_li = parseInt(current_li)+1;
	    var cur_src = $("li[rel="+current_li+"]").find("img").attr("src");
	    var next_src = $("li[rel="+next_li+"]").find("img").attr("src");
	    var cur_desc = $("li[rel="+next_li+"]").find(".photo_descr").html();
	    $(".description").fadeToggle("300");
	    $(".description").html(cur_desc);
	    $("#frame").fadeToggle("300");
	    $("#frame #big_photo_img").attr("src", next_src);
	    $("#frame").fadeToggle("300");
	    $(".description").fadeToggle("300");
	    current_li = next_li;
	}
 });
    $("#left_arrow").click(function() {
    if(current_li>1)
	{
	    var prev_li = parseInt(current_li)-1;
	    var cur_src = $("li[rel="+current_li+"]").find("img").attr("src");
	    var prev_src = $("li[rel="+prev_li+"]").find("img").attr("src");
	    var cur_desc = $("li[rel="+prev_li+"]").find(".photo_descr").html();
	    $(".description").fadeToggle("300");
	    $(".description").html(cur_desc);
	    $("#frame").fadeToggle("300");
	    $("#frame #big_photo_img").attr("src", prev_src);
	    $("#frame").fadeToggle("300");
	    $(".description").fadeToggle("300");
	    current_li = prev_li;
	}
    });
    
$("#overlay, #close2").click(function () {
$("#overlay, #wrap_frame, .description").fadeOut(300);
});   
    
    function positionCenter(elem) {
    elem.css({
    marginTop: '-' + elem.height() /2 + 'px',
    marginLeft: '-' + elem.width() /2 + 'px'
    });
    }
    
    
    
    $(".sertif img").click(function () {
    $("#wrap_frame2, #overlay").fadeIn(300);
    });
    $("#overlay, #close").click(function () {
      $("#wrap_frame2, #overlay").fadeOut(300);
    });
      positionCenter($("#wrap_frame2"));
    
    var licount2=$(".sertif").length;
$("#wrapper .sertif").each(function() {
    licount2++;
    $(this).attr('rel',licount2);
});

  var current_li2=0;
 $(".sertif_portfolio li img").click(function () {
    var src = $(this).attr("src");
    current_li2 = parseInt($(this).parent().attr('rel'));
    var cur_desc = $("li[rel="+current_li2+"]").find(".sertif_descr").html();
    $(".description2").html(cur_desc);
    $("#big_photo_img").attr("src", src);
    $("#wrap_frame2, #overlay, .description2").fadeIn();
     
});
    $("#right_arrow_sertif").click(function() {
    if(current_li2<licount2)
	{
	    var next_li2 = parseInt(current_li2)+1;
	    var cur_src2 = $("li[rel="+current_li2+"]").find("img").attr("src");
	    var next_src2 = $("li[rel="+next_li2+"]").find("img").attr("src");
	    var cur_desc2 = $("li[rel="+next_li2+"]").find(".sertif_descr").html();
	    $(".description2").fadeToggle("300");
	    $(".description2").html(cur_desc2);
	    $("#frame2").fadeToggle("300");
	    $("#frame2 #big_photo_img").attr("src", next_src2);
	    $("#frame2").fadeToggle("300");
	    $(".description2").fadeToggle("300");
	    current_li2 = next_li2;
	}
 });
    $("#left_arrow_sertif").click(function() {
    if(current_li2>1)
	{
	    var prev_li2 = parseInt(current_li2)-1;
	    var cur_src2 = $("li[rel="+current_li2+"]").find("img").attr("src");
	    var prev_src2 = $("li[rel="+prev_li2+"]").find("img").attr("src");
	    var cur_desc2 = $("li[rel="+prev_li2+"]").find(".sertif_descr").html();
	    $(".description2").fadeToggle("300");
	    $(".description2").html(cur_desc2);
	    $("#frame2").fadeToggle("300");
	    $("#frame2 #big_photo_img").attr("src", prev_src2);
	    $("#frame2").fadeToggle("300");
	    $(".description2").fadeToggle("300");
	    current_li2 = prev_li2;
	}
    });
    
$("#overlay, #close").click(function () {
$("#overlay, #wrap_frame2, .description2").fadeOut(300);
});   
    
    function positionCenter(elem) {
    elem.css({
    marginTop: '-' + elem.height() /2 + 'px',
    marginLeft: '-' + elem.width() /2 + 'px'
    });
    }
});


.b-popup.ui-dialog.ui-widget-content {
    padding: 0;
    background: #ffffff url(../img/popup-bottom.gif) no-repeat bottom center;
    border: none;
}

.b-popup .ui-state-hover{
    border: none;
    background: none;
}

.b-popup .ui-dialog-titlebar {
    border: none;
    background: url(../img/popup-header.gif) no-repeat 9px 9px;
    color: #003B8C;
    padding-left: 25px;
}

.b-popup.ui-dialog .ui-dialog-titlebar-close {
    padding: 0;
    top: 35%;
    right: .25em;
}

.b-popup .ui-widget-header .ui-icon {
    background-image: url(../../../css/images/ui-icons_375ee6_256x240.png);
}

.b-popup .ui-dialog .ui-dialog-content {
    padding: 0px 9px 80px 9px;
    text-align: center;
}

.b-popup .ui-dialog .ui-dialog-content .title {
    font-family: Arial;
    font-size: 22px;
    font-weight: bold;
    color: #003e88;
}

.b-popup .ui-dialog .ui-dialog-content .popup-content {
    margin: 15px 20px 25px;
    border: solid 2px #777;
    border-radius: 15px;
}

.b-popup .ui-dialog .ui-dialog-content p {
    text-align: left;
    font-family: Arial;
    margin: 15px;
    font-size: 14px;
    color: #777;
}

.b-popup .ui-dialog .ui-dialog-content .ok {
    height: 41px;
    width: 118px;
    background: url("../img/pop_ok.png") no-repeat 0 0;
    overflow: hidden;
    display: none;
    position: absolute;
    bottom: 35px;
    left: 50%;
    margin-left: -59px;
    cursor: pointer;
}

/* Chat DialogBox */
.im-dialog {}

  .im-dialog .popup {
    padding-bottom: 30px !important;
  }
  
  .im-dialog .popup-content {
    margin: 0px 15px 15px !important;
  }

    .im-dialog .popup-content p {
      text-align: center !important;
    }

  .im-dialog .ok {
    bottom: 7px !important;
    display: block !important;
  }

  .im-dialog .btn-yes,
  .im-dialog .btn-no {
    background: none;
    border-radius: 4px;
    border: none;
    cursor: pointer;
    display: inline-block;
    font-weight: bold;
    font-size: 1.3em;
    margin-bottom: -20px;
    margin-right: 25px;
    padding: 2px;
  }

  .im-dialog .btn-yes {
    color: #003D8C;
  }

  .im-dialog .btn-no {
    color: #680E28;
  }

#docTypesDialog {
  padding: 0 0 20px 30px;
  text-align: left;
}

  #docTypesDialog > div:first-child {
    font-size: 16px;
    margin-left: 15px;
  }
  
  #docTypesDialog > div {
    color: #777;
    font: 16px Arial;
    margin: 0 0 7px 20px;
  }
  
  #docTypesDialog .selectbutton {
    width: 162px;
    height: 34px;
    border: 1px solid #afafaf;
    background-color: #fff;
    border-radius: 4px;
    color: #505050;
    font-size: 14px;
    margin-top: 10px;
    overflow: hidden;
    padding: 0;
    text-align: center;
    vertical-align: middle;
    cursor: pointer;
  }
  
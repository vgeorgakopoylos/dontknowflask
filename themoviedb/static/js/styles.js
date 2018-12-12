function rightrollsidemenu() 
{
	if (document.getElementById("navbar").style.transform =="")
	{
		document.getElementById("setbarbutton").style.transform ="translateX(-130px)"
		document.getElementById("icon-bar1").style.transform = "translate3d(13px,5px,0px) rotate(390deg)";
		document.getElementById("icon-bar2").style.transform = "translate3d(2px,10px,0px) ";
		document.getElementById("icon-bar3").style.transform = "translate3d(13px,15px,0px) rotate(-390deg)";
		
		document.getElementById("navbar").style.transform ="translateX(-100%)";
		document.getElementById("datacontent").style.width="100%";
		document.getElementById("navbar").style.width="0%";
		document.getElementById("navbar").style.opacity="0";
	}
	else
	{
		document.getElementById("setbarbutton").style.transform ="";		
		document.getElementById("icon-bar1").style.transform = "translate3d(-1px,5px,0px) rotate(-30deg)";
		document.getElementById("icon-bar2").style.transform = "translate3d(0px,10px,0px) ";
		document.getElementById("icon-bar3").style.transform = "translate3d(-1px,15px,0px) rotate(30deg)";
		
		document.getElementById("navbar").style.transform ="";	
		document.getElementById("datacontent").style.width="90%";
		document.getElementById("navbar").style.width="10%";	
		document.getElementById("navbar").style.opacity="1";	
	}
}


var slideIndex = {timeoutHandleImg:0,timeoutHandleVid:0};
var timeoutHandleImg;
var timeoutHandleVid;

function showSlides(n, div, tag, timeouthandler) 
{
	var slides = document.getElementById(div).getElementsByTagName(tag); 
	if (slides.length<=1)
	{
		return;
	}
	var curslideIndex = slideIndex[timeouthandler];
	slideIndex[timeouthandler] = decideSlideIndex (slideIndex[timeouthandler], slides.length, n);
	slides[curslideIndex].style.opacity  = "0";
	slides[slideIndex[timeouthandler]].style.opacity   = "1";
	eval('clearInterval('+timeouthandler+');'+timeouthandler+'= setInterval(function(){showSlides(1, div, tag, \''+timeouthandler+'\')}, 5000);') //call by value and call by reference does not work in time handlers as far as i have tested
}

function decideSlideIndex (slideIndex, slideLength, n)
{
	if (slideIndex+n > slideLength-1) 
	{
		slideIndex = 0;
	}
	else if (slideIndex+n < 0)
	{
		slideIndex = slideLength-1;
	}
	else
	{
		slideIndex = slideIndex + n;
	}
	return slideIndex
}

$(document).ready(function() 
{
	timeoutHandleImg = setInterval(function(){showSlides(1,"imageslideshow",'img','timeoutHandleImg')}, 5000);
	timeoutHandleVid = setInterval(function(){showSlides(1,"videoslideshow",'iframe','timeoutHandleVid')}, 5000);
})





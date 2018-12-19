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

function createdYoutubePlayers()
{
	alert("ante gia");
}
$(document).ready(function() 
{
	timeoutHandleImg = setInterval(function(){showSlides(1,"imageslideshow",'img','timeoutHandleImg')}, 5000);
	timeoutHandleVid = setInterval(function(){showSlides(1,"videoslideshow",'iframe','timeoutHandleVid')}, 5000);
	createdYoutubePlayers();
})





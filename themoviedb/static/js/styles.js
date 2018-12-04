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
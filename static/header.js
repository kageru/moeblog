var lastScrollTop = pageYOffset;

document.addEventListener('scroll', onScroll);

function onScroll() {
var element = document.getElementById("header");
var st = window.pageYOffset || document.documentElement.scrollTop;
	if (st > lastScrollTop){
		element.classList.add("dontshowheader");
		element.classList.remove("showheader");
	} else {
		element.classList.add("showheader");
		element.classList.remove("dontshowheader");
	}
	lastScrollTop = st <= 0 ? 0 : st;
}

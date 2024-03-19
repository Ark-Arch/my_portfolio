const gallery = document.querySelector(".gallery");
const leftArrow = document.querySelector(".arrow-left");
const rightArrow = document.querySelector(".arrow-right");


console.log(leftArrow)

leftArrow.addEventListener("click", () => {
	console.log(leftArrow)
	gallery.scrollBy({
		left:-800,
		behaviour:"smooth"
		});
	});

rightArrow.addEventListener("click", () => {
	gallery.scrollBy({
		left:800,
		behaviour:"smooth"
		});
	});


<template>
	<main class="main-content">
		<!-- ======== Attractions Hero Slider ========================== -->
		<!-- This section features a slideshow showcasing various attractions, each with a title and a descriptive text overlay. Users can navigate through the slides using arrow buttons. -->
		<section class="slideshow">
			<div class="slideshow-inner">
				<div class="slides">
					<div class="slide is-active">
						<div class="slide-content">
							<div class="tint"></div>
							<div class="caption-border">
								<div class="caption">
									<div class="title">MASTERCLASSES</div>
									<div class="text">
										<p>
											To plant a garden is to believe in
											tomorrow.
										</p>
									</div>
								</div>
							</div>
						</div>
						<div class="image-container">
							<img
								src="../Images/activities/banner-farm.png"
								alt=""
								class="image"
							/>
						</div>
					</div>
					<div class="slide">
						<div class="slide-content">
							<div class="tint"></div>
							<div class="caption-border">
								<div class="caption">
									<div class="title">Spa</div>
									<div class="text">
										<p>
											Step into serenity and rejuvenate your senses at our tranquil spa retreat.
										</p>
									</div>
								</div>
							</div>
						</div>
						<div class="image-container">
							<img src="../Images/Spa.jpg" alt="" class="image" />
						</div>
					</div>
					<div class="slide">
						<div class="slide-content">
							<div class="tint"></div>
							<div class="caption-border">
								<div class="caption">
									<div class="title">Sonya’s Tours</div>
									<div class="text">
										<p>Sonya's Garden and River Tours.</p>
									</div>
								</div>
							</div>
						</div>
						<div class="image-container">
							<img
								src="../Images/activities/river.png"
								alt=""
								class="image"
							/>
						</div>
					</div>
					<div class="slide">
						<div class="slide-content">
							<div class="tint"></div>
							<div class="caption-border">
								<div class="caption">
									<div class="title">Workation</div>
									<div class="text">
										<p>Work on your tasks while being surrounded by nature</p>
									</div>
								</div>
							</div>
						</div>
						<div class="image-container">
							<img
								src="../Images/activities/computer-2.jpg"
								alt=""
								class="image"
							/>
						</div>
					</div>
				</div>
				<div class="arrows">
					<div class="arrow prev">
						<span class="svg svg-arrow-left">
							<svg
								version="1.1"
								id="svg4-Layer_1"
								xmlns="http://www.w3.org/2000/svg"
								xmlns:xlink="http://www.w3.org/1999/xlink"
								x="0px"
								y="0px"
								width="14px"
								height="26px"
								viewBox="0 0 14 26"
								enable-background="new 0 0 14 26"
								xml:space="preserve"
							>
								<path
									d="M13,26c-0.256,0-0.512-0.098-0.707-0.293l-12-12c-0.391-0.391-0.391-1.023,0-1.414l12-12c0.391-0.391,1.023-0.391,1.414,0s0.391,1.023,0,1.414L2.414,13l11.293,11.293c0.391,0.391,0.391,1.023,0,1.414C13.512,25.902,13.256,26,13,26z"
								/>
							</svg>
							<span class="alt sr-only"></span>
						</span>
					</div>
					<div class="arrow next">
						<span class="svg svg-arrow-right">
							<svg
								version="1.1"
								id="svg5-Layer_1"
								xmlns="http://www.w3.org/2000/svg"
								xmlns:xlink="http://www.w3.org/1999/xlink"
								x="0px"
								y="0px"
								width="14px"
								height="26px"
								viewBox="0 0 14 26"
								enable-background="new 0 0 14 26"
								xml:space="preserve"
							>
								<path
									d="M1,0c0.256,0,0.512,0.098,0.707,0.293l12,12c0.391,0.391,0.391,1.023,0,1.414l-12,12c-0.391,0.391-1.023,0.391-1.414,0s-0.391-1.023,0-1.414L11.586,13L0.293,1.707c-0.391-0.391-0.391-1.023,0-1.414C0.488,0.098,0.744,0,1,0z"
								/>
							</svg>
							<span class="alt sr-only"></span>
						</span>
					</div>
				</div>
			</div>
		</section>
		<!-- ================================================== Cards/What to see ================================================== -->
		<section id="attraction-cards">
			<div class="attraction-title-wrapper">
				<h1 class="attraction-title">What to do at Sonya`s</h1>
			</div>
			<div class="attraction-divider"></div>
			<div class="book-cards">
				<div class="book-card">
					<img src="../Images/activities/farm.png" alt="" />
					<h1>Masterclasses</h1>
					<p>
						Explore sustainable farming with our Organic Farming
						Masterclass. Elevate hospitality with our Bed and
						Breakfast Masterclass.
					</p>
					<div class="btn-box">
						<a href="#">EXPLORE MORE</a>
					</div>
				</div>
				<div class="book-card">
					<img src="../Images/activities/computer.png" alt="" />

					<h1>Workation</h1>
					<p>
						Work on your tasks while being surrounded by nature.
						Find your focus in Sonya's Garden Tagaytay spacious and
						serene garden.
					</p>
					<div class="btn-box">
						<a href="#">EXPLORE MORE</a>
					</div>
				</div>
				<div class="book-card">
					<img src="../Images/activities/spabed.png" alt="" />
					<h1>Spa</h1>
					<p>
						Step into serenity and rejuvenate your senses at our tranquil spa retreat.
					</p>
					<div class="btn-box">
						<a href="#">EXPLORE MORE</a>
					</div>
				</div>
				<div class="book-card">
					<img src="../Images/activities/river.png" alt="" />
					<h1>Sonya’s Tours</h1>
					<p>
						Embark on an enchanting journey through lush gardens and scenic river views with Sonya's Garden Garden and River Tours.
					</p>
					<div class="btn-box">
						<a href="#">EXPLORE MORE</a>
					</div>
				</div>
			</div>
		</section>
	</main>
</template>

<script>
import $ from "jquery";
export default {
	mounted() {
		// ================================================== Attractions hero slider ================================================== //
		let slideshowDuration = 4000;
		let slideshow = $(".main-content .slideshow");

		function slideshowSwitch(slideshow, index, auto) {
			if (slideshow.data("wait")) return;

			let slides = slideshow.find(".slide");
			let pages = slideshow.find(".pagination");
			let activeSlide = slides.filter(".is-active");
			let activeSlideImage = activeSlide.find(".image-container");
			let newSlide = slides.eq(index);
			let newSlideImage = newSlide.find(".image-container");
			let newSlideContent = newSlide.find(".slide-content");
			let newSlideElements = newSlide.find(".caption > *");
			if (newSlide.is(activeSlide)) return;

			newSlide.addClass("is-new");
			let timeout = slideshow.data("timeout");
			clearTimeout(timeout);
			slideshow.data("wait", true);
			let transition = slideshow.attr("data-transition");
			if (transition == "fade") {
				newSlide.css({
					display: "block",
					zIndex: 2,
				});
				newSlideImage.css({
					opacity: 0,
				});
			} else {
				let newSlideRight = "";
				let newSlideLeft = 0; // Set to 0 to slide only to the right
				let newSlideImageRight = "auto";
				let newSlideImageLeft = -slideshow.width() / 7.5;
				let newSlideImageToRight = "";
				let newSlideImageToLeft = 0;
				let newSlideContentLeft = 0;
				let newSlideContentRight = "auto";
				let activeSlideImageLeft = slideshow.width() / 3.5;

				newSlide.css({
					display: "block",
					width: 0,
					right: newSlideRight,
					left: newSlideLeft,
					zIndex: 2,
				});

				newSlideImage.css({
					width: slideshow.width(),
					right: newSlideImageRight,
					left: newSlideImageLeft,
				});

				newSlideContent.css({
					width: slideshow.width(),
					left: newSlideContentLeft,
					right: newSlideContentRight,
				});

				activeSlideImage.css({
					left: 0,
				});

				TweenMax.set(newSlideElements, { y: 20, force3D: true });
				TweenMax.to(activeSlideImage, 1, {
					left: activeSlideImageLeft,
					ease: Power3.easeInOut,
				});

				TweenMax.to(newSlide, 1, {
					width: slideshow.width(),
					ease: Power3.easeInOut,
				});

				TweenMax.to(newSlideImage, 1, {
					right: newSlideImageToRight,
					left: newSlideImageToLeft,
					ease: Power3.easeInOut,
				});

				TweenMax.staggerFromTo(
					newSlideElements,
					0.8,
					{ alpha: 0, y: 60 },
					{
						alpha: 1,
						y: 0,
						ease: Power3.easeOut,
						force3D: true,
						delay: 0.6,
					},
					0.1,
					function () {
						newSlide.addClass("is-active").removeClass("is-new");
						activeSlide.removeClass("is-active");
						newSlide.css({
							display: "",
							width: "",
							left: "",
							zIndex: "",
						});

						newSlideImage.css({
							width: "",
							right: "",
							left: "",
						});

						newSlideContent.css({
							width: "",
							left: "",
						});

						newSlideElements.css({
							opacity: "",
							transform: "",
						});

						activeSlideImage.css({
							left: "",
						});

						slideshow.find(".pagination").trigger("check");
						slideshow.data("wait", false);
						if (auto) {
							timeout = setTimeout(function () {
								slideshowNext(slideshow, false, true);
							}, slideshowDuration);
							slideshow.data("timeout", timeout);
						}
					}
				);
			}
		}

		function slideshowNext(slideshow, previous, auto) {
			let slides = slideshow.find(".slide");
			let activeSlide = slides.filter(".is-active");
			let newSlide = null;
			if (previous) {
				newSlide = activeSlide.prev(".slide");
				if (newSlide.length === 0) {
					newSlide = slides.last();
				}
			} else {
				newSlide = activeSlide.next(".slide");
				if (newSlide.length == 0)
					newSlide = slides.filter(".slide").first();
			}

			slideshowSwitch(slideshow, newSlide.index(), auto);
		}

		function homeSlideshowParallax() {
			let scrollTop = $(window).scrollTop();
			if (scrollTop > windowHeight) return;
			let inner = slideshow.find(".slideshow-inner");
			let newHeight = windowHeight - scrollTop / 2;
			let newTop = scrollTop * 0.8;

			inner.css({
				transform: "translateY(" + newTop + "px)",
				height: newHeight,
			});
		}

		$(document).ready(function () {
			$(".slide").addClass("is-loaded");

			$(".slideshow .arrows .arrow").on("click", function () {
				slideshowNext(
					$(this).closest(".slideshow"),
					$(this).hasClass("prev")
				);
			});

			$(".slideshow .pagination .item").on("click", function () {
				slideshowSwitch($(this).closest(".slideshow"), $(this).index());
			});

			$(".slideshow .pagination").on("check", function () {
				let slideshow = $(this).closest(".slideshow");
				let pages = $(this).find(".item");
				let index = slideshow.find(".slides .is-active").index();
				pages.removeClass("is-active");
				pages.eq(index).addClass("is-active");
			});

			let timeout = setTimeout(function () {
				slideshowNext(slideshow, false, true);
			}, slideshowDuration);

			slideshow.data("timeout", timeout);
		});

		if ($(".main-content .slideshow").length > 1) {
			$(window).on("scroll", homeSlideshowParallax);
		}
	},
};
</script>

<style scoped>
.third-row {
	height: 100vh;
	background: var(--text-color-c);
	display: flex;
	justify-content: end;
}

/*================================================== Attractions Hero Slider ==================================================*/

.tint {
	background-color: rgba(0, 0, 0, 0.493);
	position: absolute;
	z-index: -1;
	width: 100%;
	height: 100%;
}

.slideshow {
	display: flex;
	overflow: hidden;
	height: 100vh;
}

.slideshow .slideshow-inner {
	position: absolute;
	top: 0;
	left: 0;
	width: 100%;
	height: 100%;
}

.slideshow .slides {
	position: absolute;
	top: 0;
	left: 0;
	width: 100%;
	height: 100%;
	z-index: 1;
}

.slideshow .slide {
	display: none;
	overflow: hidden;
	position: absolute;
	top: 0;
	left: 0;
	width: 100%;
	height: 100%;
	z-index: 1;
	opacity: 0;
	transition: opacity 0.3s ease;
}

.slideshow .slide.is-active {
	display: block;
}

.slideshow .slide.is-loaded {
	opacity: 1;
}

.caption-border {
	width: 50%;
	height: 50%;
	margin-left: 7rem;
	padding: 7rem 0;
	border: 2px solid white;
}

.slideshow .slide .caption {
	display: flex;
	flex-direction: column;
	justify-content: center;
	align-items: center;
	text-align: center;
	margin-left: 1rem;
	padding: 0 100px;
}

.slideshow .slide .image-container {
	position: absolute;
	top: 0;
	left: 0;
	width: 100%;
	height: 100%;
	background-position: center;
	z-index: 1;
	background-size: cover;
	image-rendering: optimizeQuality;
}

.slideshow .slide .image-container::before {
	content: "";
	display: block;
	position: absolute;
	top: 0;
	left: 0;
	width: 100%;
	height: 100%;
	background: rgba(0, 0, 0, 0.5);
}

.slideshow .slide .image {
	width: 100%;
	object-fit: cover;
	height: 100%;
}

.slideshow .slide-content {
	position: absolute;
	width: 100%;
	height: 100%;
	z-index: 2;
	color: #fff;
	text-align: center;
	display: flex;
	justify-content: center;
	align-items: center;
}

.slideshow .slide .title {
	font-family: "Playfair Display", serif;
	font-size: 70px;
	font-weight: 400;
	line-height: 70px;
	letter-spacing: 0em;

	max-width: 500px;
	text-transform: uppercase;
}

.slideshow .slide .text {
	font-family: "Abel", sans-serif;
	font-size: 32px;
	font-weight: 400;
	line-height: 41px;
	letter-spacing: 0.16em;
	text-align: center;

	margin-top: 3rem;
	max-width: 1000px;
	font-size: 18px;
	line-height: 1.4;
}

.slideshow .arrows .arrow {
	margin: -33px 0 0;
	padding: 20px;
	position: absolute;
	top: 50%;
	cursor: pointer;
	z-index: 3;
}

.slideshow .arrows .prev {
	left: 90px;
}

.slideshow .arrows .prev:hover .svg {
	left: -10px;
}

.slideshow .arrows .next {
	right: 30px;
}

.slideshow .arrows .next:hover .svg {
	left: 10px;
}

.slideshow .arrows .svg {
	position: relative;
	left: 0;
	width: 14px;
	height: 26px;
	fill: #fff;
	transition: left 0.2s ease;
}

/* ================================================== What to See at Sonya's ================================================== */
#attraction-cards {
	height: 100vh;
	background-color: #57716c;
}

/* .attraction-title-wrapper{
    margin-top: 10rem;
} */

.attraction-title {
	color: white;
	font-family: "Playfair Display", serif;
	font-size: 70px;
	font-weight: 400;
	line-height: 128px;
	letter-spacing: 0em;
	text-align: center;
	padding-top: 2rem;
}

.attraction-divider {
	border-bottom: 1px;
	border-bottom-style: solid;
	text-align: center;
	margin-left: 6rem;
	margin-right: 2rem;
	margin-top: 3rem;
	margin-bottom: 3rem;

	color: white;
}

.book-cards {
	margin-left: 4.5rem;
	max-width: 100%;
	display: flex;
	align-items: center;
	justify-content: center;
}

.book-cards .book-card {
	padding-bottom: 2rem;
	margin: 2rem;
	width: 30rem;
	height: 26rem;
	text-align: center;
	color: #68502b;
	background-color: white;
}

.book-card img {
	position: inherit;
	width: 100%;
	height: 45%;
	filter: brightness(100%);
}

.book-card h1 {
	font-family: "Playfair Display", serif;
	font-weight: 400;
	font-style: normal;
	font-optical-sizing: auto;
	font-size: 25px;
	padding-top: 1rem;
	padding-bottom: 0.5rem;
}

.book-card p {
	font-size: 15px;
	font-family: "Abel", sans-serif;
	font-weight: 400;
	font-style: normal;
	text-align: center;
	padding-left: 2rem;
	padding-right: 2rem;
	height: 25%;
}

.btn-box {
	padding-top: 2rem;
}

.btn-box:hover a {
	width: 234px;
	height: 40px;
	box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);
	background: var(--bg-color-b);
	color: #d9d9d9;
}

.btn-box a {
	position: relative;

	display: inline-flex;
	justify-content: center;
	align-items: center;
	width: 227px;
	height: 35px;
	background: var(--bg-color-c);
	font-size: 24px;
	font-family: "Abel", sans-serif;
	font-weight: 400;
	font-style: normal;
	color: rgb(255, 255, 255);
	text-decoration: none;
	letter-spacing: 1px;
	transition: 0.5s;
}
/* Responsive styles */
</style>

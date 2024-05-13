<template>
	<!-- The main content area of the home page -->

	<main>
		<!-- The home section of the page -->
		<section class="home">
			<!-- The home banner area -->
			<div class="home-banner">
				<!-- The background image of the banner -->
				<div class="bg-img">
					<img src="../Images/banner.png" alt="" />
				</div>
				<!-- The content area of the banner -->
				<div class="content">
					<p>WELCOME TO</p>
					<h1>Sonya’s Garden</h1>
					<p>A MAGICAL BED AND BREAKFAST IN TAGAYTAY, CAVITE</p>
				</div>
			</div>
			<!-- The home about area -->
			<div class="home-about">
				<!-- The content area of the about section -->
				<div class="about-content">
					<h1>
						Your Perfect Wedding Venue and Magical Bed and Breakfast
						in Tagaytay
					</h1>
					<p>
						Plan your next getaway and look forward for a
						stress-free day! Sonya's Garden the perfect place to
						unwind and celebrate with your loved ones. Located near
						Tagaytay, our 1.5-hectare paradise offers bed and
						breakfast, restaurant, spa, and garden venue for
						weddings, debuts, birthdays, company events, and other
						events. Book your stay now!
					</p>
				</div>
				<!-- The side image area of the about section -->
				<div class="side-img">
					<img src="../Images/side photo.jpg" alt="" />
				</div>
			</div>
			<!-- The home dining area -->
			<div class="home-dining">
				<!-- The first dining card -->
				<div class="dining-card">
					<!-- The image area of the dining card -->
					<img src="../Images/dining.jpg" alt="" />
					<!-- The title area of the dining card -->
					<h1>Dine at Our Tables</h1>
					<!-- The description area of the dining card -->
					<p>
						Dine and unwind in a serene garden restaurant in
						Tagaytay. Gather your loved ones, friends, and family to
						savor Sonya's Garden salads, which are made with
						freshly-picked greens from our gardens, as well as our
						delectable pasta dishes and other classic recipes.
					</p>
					<!-- The button area of the dining card -->
					<div class="btn-box">
						<router-link to="/dining">LEARN MORE</router-link>
					</div>
				</div>
				<!-- The second dining card -->
				<div class="dining-card">
					<!-- The image area of the dining card -->
					<img src="../Images/wedding.jpg" alt="" />
					<!-- The title area of the dining card -->
					<h1>Host Events with Us</h1>
					<!-- The description area of the dining card -->
					<p>
						Exchange your sweetest wedding vows under the clear
						skies and cool breeze of Tagaytay. Experience a
						stress-free wedding day for you and your guests at
						Sonya's Garden. Plan your most special day with Sonya's
						Garden Tagaytay wedding packages and rates.
					</p>
					<!-- The button area of the dining card -->
					<div class="btn-box">
						<router-link to="/dining">LEARN MORE</router-link>
					</div>
				</div>
			</div>
		</section>

		<!-- The accommodations section of the page -->
		<section id="accomodations">
			<!-- Title of the accommodations section -->
			<h1 class="accomodation-title">Accomodations</h1>
			<div class="wrapper">
				<!-- The carousel area for displaying accommodation cards -->
				<div class="carousel">
					<!-- First accommodation card -->
					<div>
						<div class="card">
							<!-- Header of the card -->
							<div class="card-header">
								<!-- Image for the accommodation -->
								<img src="../Images/lover_s suite.jpeg" />
							</div>
							<!-- Body of the card -->
							<div class="card-body">
								<div class="card-content">
									<!-- Title of the accommodation -->
									<div class="card-title">Lover's Suite</div>
									<!-- Description of the accommodation -->
									<div class="card-text">
										<p>
											<!-- Pricing details for Lover's Suite -->
											starting at 7,200php a night
											<br />
											2 adults
										</p>
									</div>
								</div>
							</div>
						</div>
					</div>
					<!-- Second accommodation card -->
					<div>
						<div class="card">
							<!-- Header of the card -->
							<div class="card-header">
								<!-- Image for the accommodation -->
								<img src="../Images/family suite.jpeg" />
							</div>
							<!-- Body of the card -->
							<div class="card-body">
								<div class="card-content">
									<!-- Title of the accommodation -->
									<div class="card-title">Family Suite</div>
									<!-- Description of the accommodation -->
									<div class="card-text">
										<p>
											<!-- Pricing details for Family Suite -->
											starting at 14,400php a night
											<br />
											4 adults
										</p>
									</div>
								</div>
							</div>
						</div>
					</div>
					<!-- Third accommodation card -->
					<div>
						<div class="card">
							<!-- Header of the card -->
							<div class="card-header">
								<!-- Image for the accommodation -->
								<img src="../Images/business suite.webp" />
							</div>
							<!-- Body of the card -->
							<div class="card-body">
								<div class="card-content">
									<!-- Title of the accommodation -->
									<div class="card-title">Business Suite</div>
									<!-- Description of the accommodation -->
									<div class="card-text">
										<p>
											<!-- Pricing details for Business Suite -->
											starting at 7,200php a night
											<br />
											2 adults
										</p>
									</div>
								</div>
							</div>
						</div>
					</div>
					<!-- Fourth accommodation card -->
					<div>
						<div class="card">
							<!-- Header of the card -->
							<div class="card-header">
								<!-- Image for the accommodation -->
								<img src="../Images/lover_s suite.jpeg" />
							</div>
							<!-- Body of the card -->
							<div class="card-body">
								<div class="card-content">
									<!-- Title of the accommodation -->
									<div class="card-title">Lover's Suite</div>
									<!-- Description of the accommodation -->
									<div class="card-text">
										<p>
											<!-- Pricing details for Lover's Suite -->
											starting at 7,200php a night
											<br />
											2 adults
										</p>
									</div>
								</div>
							</div>
						</div>
					</div>
					<!-- Fifth accommodation card -->
					<div>
						<div class="card">
							<!-- Header of the card -->
							<div class="card-header">
								<!-- Image for the accommodation -->
								<img src="../Images/family suite.jpeg" />
							</div>
							<!-- Body of the card -->
							<div class="card-body">
								<div class="card-content">
									<!-- Title of the accommodation -->
									<div class="card-title">Family Suite</div>
									<!-- Description of the accommodation -->
									<div class="card-text">
										<p>
											<!-- Pricing details for Family Suite -->
											starting at 14,400php a night
											<br />
											4 adults
										</p>
									</div>
								</div>
							</div>
						</div>
					</div>
					<!-- Sixth accommodation card -->
					<div>
						<div class="card">
							<!-- Header of the card -->
							<div class="card-header">
								<!-- Image for the accommodation -->
								<img src="../Images/business suite.webp" />
							</div>
							<!-- Body of the card -->
							<div class="card-body">
								<div class="card-content">
									<!-- Title of the accommodation -->
									<div class="card-title">Business Suite</div>
									<!-- Description of the accommodation -->
									<div class="card-text">
										<p>
											<!-- Pricing details for Business Suite -->
											starting at 7,200php a night
											<br />
											2 adults
										</p>
									</div>
								</div>
							</div>
						</div>
					</div>
				</div>
				<!-- Button for navigating accommodations in the carousel -->
				<div>
					<!-- Icon for navigating right -->
					<i class="fa-solid fa-angles-right"></i>
				</div>
			</div>
		</section>

		<!-- ACTIVITIES SECTION -->
		<section id="activities">
			<!-- Title of the activities section -->
			<h1 class="activity-title">Activities</h1>
			<div class="wrapper">
				<!-- Carousel container for displaying activity cards -->
				<div class="carousel">
					<!-- First activity card -->
					<div>
						<div class="card">
							<!-- Header of the card -->
							<div class="card-header">
								<!-- Image for the activity -->
								<img src="../Images/Masterclasses.png" />
							</div>
							<!-- Body of the card -->
							<div class="card-body">
								<div class="card-content">
									<!-- Title of the activity -->
									<div class="card-title">Masterclasses</div>
									<!-- Description of the activity -->
									<div class="card-text">
										<p>
											<!-- Pricing details for Masterclasses -->
											Single Occupancy: P27,250 <br />
											Twin/Triple Sharing: P23,000
										</p>
									</div>
								</div>
							</div>
						</div>
					</div>
					<!-- Second activity card -->
					<div>
						<div class="card">
							<!-- Header of the card -->
							<div class="card-header">
								<!-- Image for the activity -->
								<img src="../Images/WorkStations.png" />
							</div>
							<!-- Body of the card -->
							<div class="card-body">
								<div class="card-content">
									<!-- Title of the activity -->
									<div class="card-title">Workation</div>
									<!-- Description of the activity -->
									<div class="card-text">
										<p>
											<!-- Pricing details for Workation -->
											starting at 15,000php a week
											<br />
											with various package inclusions
										</p>
									</div>
								</div>
							</div>
						</div>
					</div>
					<!-- Third activity card -->
					<div>
						<div class="card">
							<!-- Header of the card -->
							<div class="card-header">
								<!-- Image for the activity -->
								<img src="../Images/Spa.jpg" />
							</div>
							<!-- Body of the card -->
							<div class="card-body">
								<div class="card-content">
									<!-- Title of the activity -->
									<div class="card-title">Spa</div>
									<!-- Description of the activity -->
									<div class="card-text">
										<p>
											<!-- Pricing details for Spa -->
											starting at 1,100php <br />
											1 hour massage
										</p>
									</div>
								</div>
							</div>
						</div>
					</div>
					<!-- Fourth activity card -->
					<div>
						<div class="card">
							<!-- Header of the card -->
							<div class="card-header">
								<!-- Image for the activity -->
								<img src="../Images/Masterclasses.png" />
							</div>
							<!-- Body of the card -->
							<div class="card-body">
								<div class="card-content">
									<!-- Title of the activity -->
									<div class="card-title">Lover's Suite</div>
									<!-- Description of the activity -->
									<div class="card-text">
										<p>
											<!-- Pricing details for Lover's Suite -->
											Single Occupancy: P27,250 <br />
											Twin/Triple Sharing: P23,000
										</p>
									</div>
								</div>
							</div>
						</div>
					</div>
					<!-- Fifth activity card -->
					<div>
						<div class="card">
							<!-- Header of the card -->
							<div class="card-header">
								<!-- Image for the activity -->
								<img src="../Images/WorkStations.png" />
							</div>
							<!-- Body of the card -->
							<div class="card-body">
								<div class="card-content">
									<!-- Title of the activity -->
									<div class="card-title">Workation</div>
									<!-- Description of the activity -->
									<div class="card-text">
										<p>
											<!-- Pricing details for Workation -->
											starting at 15,000php a week
											<br />
											with various package inclusions
										</p>
									</div>
								</div>
							</div>
						</div>
					</div>
					<!-- Sixth activity card -->
					<div>
						<div class="card">
							<!-- Header of the card -->
							<div class="card-header">
								<!-- Image for the activity -->
								<img src="../Images/Spa.jpg" />
							</div>
							<!-- Body of the card -->
							<div class="card-body">
								<div class="card-content">
									<!-- Title of the activity -->
									<div class="card-title">Spa</div>
									<!-- Description of the activity -->
									<div class="card-text">
										<p>
											<!-- Pricing details for Spa -->
											starting at 1,100php <br />
											1 hour massage
										</p>
									</div>
								</div>
							</div>
						</div>
					</div>
				</div>
				<!-- Button for navigating events in the carousel -->
				<div class="events-button">
					<!-- Icon for navigating right -->
					<i class="fa-solid fa-angles-right"></i>
				</div>
			</div>
		</section>

		<!-- REVIEWS SECTION -->
		<section id="reviews">
			<div class="hero-img">
				<div class="hero-inner">
					<!-- Title of the reviews section -->
					<div class="hero-title">Memories from the Garden</div>
					<div class="hero-content">
						<!-- First review content -->
						<div class="review-content">
							<!-- Review text -->
							"Only one hour of Sonya’s Signature Massage, but it
							felt like every second, every stroke counts. This is
							one of the best, if not the best massage I’ve
							experienced."
							<br />
							<br />
							<br />
							<br />
							<!-- Reviewer's name -->
							<span class="reviewer-name" id="MV"
								>Tina Tecson</span
							>
						</div>
						<!-- Second review content -->
						<div class="review-content">
							<!-- Review text -->
							"Come here on an empty stomach if you’re planning to
							dine in this heaven of a place. One of the best
							lunch dates of my life."
							<br />
							<br />
							<br />
							<br />
							<!-- Reviewer's name -->
							<span class="reviewer-name" id="PN"
								>Phyllis Salvador</span
							>
						</div>
						<!-- Third review content -->
						<div class="review-content">
							<!-- Review text -->
							"We decided to check out their Panaderia to buy some
							freshly made bread. I highly recommend their Cheese
							Hopia!"
							<br />
							<br />
							<br />
							<br />
							<!-- Reviewer's name -->
							<span class="reviewer-name" id="LB"
								>Lily Collins</span
							>
						</div>
					</div>
					<!-- Button for leaving memories -->
					<div class="hero-btn-container">
						<!-- Link to leave memories -->
						<a href="#" class="hero-btn">LEAVE YOUR MEMORIES</a>
					</div>
				</div>
			</div>
		</section>
	</main>
</template>

<script>
// When the document is ready, initialize the slick carousel
import axios from "axios";

export default {

	created() {
		const client = axios.create({
			baseURL: "http://127.0.0.1:8000",
		});
		const token = localStorage.getItem("token");
		const headers = {
			Authorization: `Token ${token}`,
			"Content-Type": "application/json",
		};

		client
			.get("api/user/", { headers: headers })
			.then((res) => {
				this.isUserLoggedIn = true;
			})
			.catch((error) => {
				console.log("ERROR", error);
				this.isUserLoggedIn = false;
			});
	},

	mounted() {
		$(document).ready(function () {
			$(".carousel").slick({
				// Slick carousel settings
				speed: 500,
				slidesToShow: 3,
				slidesToScroll: 1,
				autoplay: true,
				autoplaySpeed: 1500,
				dots: false,
				centerMode: false,
				responsive: [
					{
						breakpoint: 1024,
						settings: {
							slidesToShow: 3,
							slidesToScroll: 1,
							// centerMode: true,
						},
					},
					{
						breakpoint: 800,
						settings: {
							slidesToShow: 2,
							slidesToScroll: 1,
							dots: false,
							infinite: true,
						},
					},
					{
						breakpoint: 480,
						settings: {
							slidesToShow: 1,
							slidesToScroll: 3,
							dots: false,
							infinite: true,
							autoplay: true,
							autoplaySpeed: 2000,
						},
					},
				],
			});
		});
	},
};
</script>

<style scoped>
.home-banner {
	max-width: 100%;
	height: 100vh;
	color: var(--text-color-c);
	display: flex;
	justify-content: center;
	align-items: center;
}

.home-banner h1 {
	font-family: "Playfair Display", serif;
	font-weight: 400;
	font-style: normal;
	font-optical-sizing: auto;
	font-size: 128px;
}

.home-banner p {
	font-size: 25px;
	font-family: "Abel", sans-serif;
	font-weight: 400;
	font-style: normal;
	word-spacing: 3px;
	letter-spacing: 3px;
}

.bg-img {
	position: absolute;
	top: 0;
	right: 0;
	bottom: 0;
	left: 0;
	overflow: hidden;
}

.bg-img img {
	width: 100%;
	object-fit: cover;
	filter: brightness(35%);
	opacity: 90%;
}

.content {
	text-align: center;
	z-index: 1;
	color: #fff;
}

.home-about {
	max-width: 100%;
	height: 100vh;
	display: flex;
	align-items: center;
	justify-content: flex-end;
	background-color: var(--bg-color-a);
}

.side-img {
	width: 35%;
	display: flex;
	justify-content: center;
	align-items: center;
	margin: 2rem;
}

.side-img img {
	width: auto;
	height: 80vh;
}

.about-content h1 {
	font-family: "Playfair Display", serif;
	font-weight: 400;
	font-style: normal;
	font-optical-sizing: auto;
	font-size: 50px;
	align-items: start;
	padding-bottom: 5rem;
}

.about-content p {
	font-size: 24px;
	font-family: "Abel", sans-serif;
	font-weight: 400;
	font-style: normal;
}

.home-about .about-content {
	margin-top: 9rem;
	width: 45%;
	height: 70vh;

	text-align: justify;
	z-index: 1;
	color: var(--text-color-a);
}

.home-dining {
	padding-left: 4rem;
	max-width: 100%;
	height: 100vh;
	display: flex;
	align-items: center;
	justify-content: center;
	background-color: var(--bg-color-b);
}

.home-dining .dining-card {
	margin: 2rem;
	width: 40vw;
	height: 90vh;
	text-align: center;
	color: var(--text-color-a);
	background-color: var(--bg-color-a);
}

.dining-card img {
	width: 40vw;
	height: 55vh;
}

.dining-card h1 {
	font-family: "Playfair Display", serif;
	font-weight: 400;
	font-style: normal;
	font-optical-sizing: auto;
	font-size: 40px;
	padding-top: 1rem;
}

.dining-card p {
	font-size: 20px;
	font-family: "Abel", sans-serif;
	font-weight: 400;
	font-style: normal;
	padding-left: 2rem;
	padding-right: 2rem;
}

.btn-box {
	padding-top: 2rem;
	cursor: pointer;
}

.btn-box:hover a {
	width: 234px;
	height: 45px;
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
	height: 42px;
	background: rgb(202, 201, 201);
	font-size: 24px;
	font-family: "Abel", sans-serif;
	font-weight: 400;
	font-style: normal;
	color: black;
	text-decoration: none;
	letter-spacing: 1px;
	transition: 0.5s;
}

p {
	font-family: "Abel", sans-serif;
	font-style: normal;
	font-size: 20px;
	font-weight: 400;
	line-height: 24px;
	letter-spacing: -0.04em;
}

/*======================================== Slider/Accomodations Section ========================================*/
#accomodations {
	background-color: #f4f1ed;
}

.wrapper {
	width: 100%;
	padding-top: 20px;
	text-align: center;
	margin-top: 2rem;
	margin-bottom: 2rem;
}

.accomodation-title {
	font-family: "Playfair Display", serif;
	font-size: 60px;
	font-weight: 400;
	line-height: 73px;
	letter-spacing: -0.04em;
	text-align: center;
	color: #68502b;
	margin-bottom: -4rem;
	padding-top: 1rem;
	margin-top: 0rem;
}

.carousel {
	width: 90%;
	margin: 0px auto;
}

.slick-slide {
	margin-top: 70px;
	margin-bottom: 2rem;
	margin-left: 1rem;
	margin-right: 27rem;
}

.slick-slide img {
	/* width:100%; */
	width: 400px;
	height: 342px;
	top: 291px;
	left: 27px;
}

/* .slick-prev, .slick-next{
    display: none;
    background: #000;
    border-radius: 15px;
    border-color: transparent;
} */

.card {
	width: 400px;
	/* border: 2px solid #fff; */
	box-shadow: 2px 2px 15px #472f24;
}

.card-body {
	background: #472f24;
	width: 100%;
	height: 10rem;
	width: 400px;
}

.card-content {
	text-align: left;
	color: white;
	padding: 15px;
}

.card-title {
	font-family: "Playfair Display", serif;
	font-size: 40px;
	font-weight: 400;
	line-height: 73px;
	letter-spacing: -0.04em;
	text-align: left;
}

.card-text {
	font-family: "Abel";
	font-size: 20px;
	font-weight: 400;
	/* line-height: 24px; */
	letter-spacing: -0.04em;
	text-align: left;
	margin-top: -2rem;
	padding-top: 2rem;
}

/*=========== Home Activities Section=============*/
#activities {
	background-color: #f2e3ce;
}

.activity-title {
	font-family: "Playfair Display", serif;
	font-size: 60px;
	font-weight: 400;
	line-height: 73px;
	letter-spacing: -0.04em;
	text-align: center;
	color: #68502b;
	margin-bottom: -4rem;
	padding-top: 2rem;
	margin-top: 1rem;
}

.events-button {
	background-color: #f2e3ce;
	padding-bottom: -1rem;
	align-items: center;
	justify-content: center;
}

i.fa-angles-right {
	margin-top: 0;
	font-size: 2rem;
	color: #68502b;
}

i:hover {
	transform: scale(1.3);
	transition: 1s;
	color: #856f51;
}

i.fa-angles-right:hover::after {
	content: "See More";
	position: absolute;
	left: -170%;
	top: 30%;
	font-size: 10px;
}

/*======================================== Home Reviews Section ========================================*/
.hero-img {
	background-image: url(../Images/ReviewsBG.jpg);
	height: 100%;
	width: 100%;
	background-position: center;
	background-repeat: no-repeat;
	background-size: cover;
	position: relative;
}

.hero-title {
	font-family: "Playfair Display", serif;
	font-size: 60px;
	font-weight: 400;
	line-height: 73px;
	letter-spacing: -0.04em;
	text-align: center;
	padding-top: 5rem;
	margin-left: 4.5rem;
	color: white;
}

.hero-inner {
	background-color: #020305ab;

	align-items: center;
	justify-content: center;
}

.hero-content {
	padding-left: 5rem;
	margin-top: 10rem;
	width: 100%;
	display: flex;
	justify-content: space-around;
	align-items: center;
	color: white;
}

.review-content {
	width: 400px;
	font-family: "Abel", sans-serif;
	font-size: 24px;
	font-weight: 400;
	line-height: 31px;
	letter-spacing: -0.04em;
	text-align: center;
	margin-left: 2rem;
	margin-right: 2rem;
}

.reviewer-name {
	font-family: "Playfair Display", serif;
	font-size: 40px;
	font-weight: 400;
	line-height: 73px;
	letter-spacing: -0.04em;
	text-align: center;
}

.hero-btn-container {
	display: flex;
	justify-content: center;
	margin-top: 10rem;
	padding-bottom: 10rem;
}

.hero-btn {
	padding-top: 1rem;
	padding-bottom: 5rem;
	padding-left: 3rem;
	padding-right: 3rem;
	margin-left: 4.5rem;
	text-align: center;
	width: 390px;
	height: 31px;
	font-family: "Abel", sans-serif;
	font-size: 24px;
	font-weight: 400;
	line-height: 31px;
	letter-spacing: 0.18em;
	color: black;
	background-color: #d9d9d9;
	text-decoration: none;
}

.hero-btn:hover {
	transform: scale(1.1);
	transition: 1s;
	background-color: #ecf3c9;
}
</style>

<template>
	<main>
		<div class="sticky top-0 z-10">
			<h1 class="header">Events Packages</h1>
			<ul class="navs">
				<!-- using v-for to call each nav links  -->
				<li
					class="options"
					v-for="(link, index) in navLinks"
					:key="index"
				>
					<router-link
						v-if="link.showNav"
						:to="link.path"
						active-class="active"
					>
						<span class="text home-text">{{
							link.name
						}}</span></router-link
					>
				</li>
			</ul>
		</div>
		<section class="first-row all-sec">
			<img class="events-bg-img" :src="img" :alt="alt" />
		</section>
		<section class="all-sec">
			<router-view />
		</section>
	</main>
</template>

<script>
export default {
	methods: {
		// updateActive(index) {
		// 	this.navLinks.forEach((link, i) => {
		// 		link.ind = i === index ? 1 : 0;
		// 	});
		// },
	},
	computed: {
		img() {
			return this.navLinks.find((link) => link.path === this.$route.path)
				.img;
		},
		alt() {
			return this.navLinks.find((link) => link.path === this.$route.path)
				.name;
		},
	},
	data() {
		return {
			navLinks: [
				{
					name: "Wedding Packages",
					path: "/events/wedding-pack",
					ind: 1,
					showNav: true,
					img: "/src/Images/EventsImg/wedding.jpg",
				},
				{
					name: "Food Packages",
					path: "/events/food-pack",
					ind: 2,
					showNav: true,
					img: "/src/Images/EventsImg/2food.webp",
				},
				{
					name: "Prenup Packages",
					path: "/events/prenup-pack",
					ind: 3,
					showNav: true,
					img: "/src/Images/EventsImg/prenup.jpg",
				},
				{
					name: "Proposal Packages",
					path: "/events/proposal-pack",
					ind: 4,
					showNav: true,
					img: "/src/Images/EventsImg/proposal.jpg",
				},
				{
					name: "Events",
					path: "/events",
					img: "/src/Images/ReviewsBG.jpg",
					alt: "Events",
				},
			],
		};
	},
	// ...
};
</script>

<style scoped>
.all-sec {
	margin-left: 4.0%;
	margin-bottom: 2rem;
}
/*font-family: "Playfair Display", sans-serif;
	font-weight: 400;
	font-style: normal;*/
.first-row {
	background-color: var(--bg-color-b);
	height: 73vh;
	display: flex;
	flex-direction: column;
	align-items: center;
}
.header {
	font-family: "Playfair Display", sans-serif;
	font-weight: 400;
	font-style: normal;
	font-size: 6.4rem;
	text-align: center;
	color: var(--text-color-c);
}

.navs {
	/*margin-inline: 8.85rem;*/
	display: flex;
	justify-content: center;
	padding-block: 1rem;
}
.navs a .text {
	font-size: 1.5rem;
	padding-inline: 1.5rem;
	font-family: "Abel", sans-serif;
	font-weight: 400;
	font-style: normal;
	color: var(--text-color-c);
	transition: 0.3s;
	cursor: pointer;
}

.navs a.active .text {
	color: var(--text-color-b);
}
.sticky {
	width: 100%;
	background-color: var(--bg-color-b);
}
.events-bg-img {
	height: 95%;
	width: 80%;
	object-fit: cover;
	filter: brightness(40%);
	opacity: 95%;
}
</style>

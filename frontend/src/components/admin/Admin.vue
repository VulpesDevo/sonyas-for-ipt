<template>
	<main>
		<div class="sticky top-0 z-10">
			<h1 class="header" @click="submitLogout">Events Packages</h1>
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
			<!-- <img class="events-bg-img" :src="img" :alt="alt" /> -->
		</section>
		<section class="all-sec">
			<router-view />
		</section>
	</main>
</template>

<script>
import axios from "axios";
import { ref } from "vue";
import router from "../../routes";
export default {
	methods: {
		submitLogout() {
            const token = localStorage.getItem("staff");
            console.log(token);
			const headers = {
				Authorization: `Token ${token}`,
				"Content-Type": "application/json",
			};
			axios
				.post("http://127.0.0.1:8000/api/leave", { headers: headers })
				.then((res) => {
					this.isUserLoggedIn = false;
					console.log("Status:", res.status);
					
					localStorage.removeItem("staff");
					window.scrollTo(0, 0);
					router.push({ name: "stafflogin" });
					console.log("User logged out");
				})
				.catch((error) => {
					console.log(error);
				});
		},
		// Method to reload the page
		reloadPage() {
			
			setTimeout(() => {
				this.$router.go(0);
				
			}, 500);
		},
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
				
			],
		};
	},

	// ...
};
</script>

<style scoped>
.all-sec {
	margin-left: 4.3%;
	height: 100vh;
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

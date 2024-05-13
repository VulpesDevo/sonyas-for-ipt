<template>
	<div class="menu">
		<ul class="navs">
			<!-- using v-for to call each nav links  -->
			<li class="nav-link" v-for="(link, index) in navLinks" :key="index">
				
					<router-link name="EventsNavBar" v-if="link.showNav" :to="link.path" class="text">
						{{ link.name }}</router-link
					>
			
			</li>
		</ul>
	</div>
</template>

<script>
export default {

	methods: {
		onclicknav() {},
	},
	data() {
		return {
			navLinks: [
				{
					name: "Wedding Packages",
					path: "/wedding-pack",
					showNav: true,
				},
				{
					name: "Food Packages",
					path: "/food-pack",
					showNav: true,
					label: "place",
				},
				{
					name: "Prenup Packages",
					path: "/prenup-pack",
					showNav: true,
				},
				{
					name: "Proposal Packages",
					path: "/proposal-pack",
					showNav: true,
				},
			],
		};
	},
};
</script>

<style scoped>
.navs {
	display: flex;
	justify-content: center;
	padding-top: 1rem;
}
.navs .nav-link a {
	font-size: 1.5rem;
	padding-inline: 1.5rem;
	font-family: "Abel", sans-serif;
	font-weight: 400;
	font-style: normal;
	color: var(--text-color-c);
	cursor: pointer;
}

.navs li .options.active .text {
	color: var(--text-color-b);
}
</style>

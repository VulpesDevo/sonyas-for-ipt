<template>
	<!-- Menu component -->
	<div class="menu">
		<ul class="navs">
			<!-- using v-for to call each nav links  -->
			<li
				class="nav-link"
				v-for="(link, index) in navigationLinks"
				:key="index"
			>
				<router-link
					class="anch"
					exact
					:to="link.path"
					active-class="active"
					@click="scrollToTop"
				>
					<span
						v-if="link.showIcon"
						class="material-icons-outlined icon"
						>{{ link.label }}</span
					>

					<span class="text home-text">{{ link.name }}</span>
				</router-link>
			</li>
		</ul>
	</div>
</template>

<script>
export default {
	methods: {
		// Method to scroll to the top of the page
		scrollToTop() {
			window.scrollTo(0, 0);
		},
	},
	// list  of navigation links with their properties
	data() {
		return {
			//this is in case of adding new navigation link
			navigationLinks: [
				{
					name: "Home",
					path: "/home",
					showIcon: true,
					label: "home",
				},
				{
					name: "Attraction",
					path: "/attraction",
					showIcon: true,
					label: "place",
				},
				{
					name: "Accommodation",
					path: "/accomm",
					showIcon: true,
					label: "bed",
				},
				{
					name: "Dining",
					path: "/dining",
					showIcon: true,
					label: "restaurant",
				},
				{
					name: "Events",
					path: "/events",
					showIcon: true,
					label: "event",
				},
				{
					name: "Activities",
					path: "/activities",
					showIcon: true,
					label: "directions_run",
				},
			],
		};
	},
};
</script>

<style scoped>
/* ====SIDEBAR==== */
.sidebar.close .text {
	opacity: 0;
	display: none;
}

.sidebar .text {
	padding-left: 25px;
	font-size: 15px;
	font-family: "Poppins", sans-serif;
	font-weight: 400;
	font-style: normal;
}
.sidebar li .icon {
	display: flex;
	padding-left: 4px;
	align-items: center;
	justify-content: center;

	min-width: 50px;
	height: 54px;
	border-radius: 15px;
	font-size: 22px;
}
.sidebar li .icon,
.sidebar li .text {
	color: var(--bg-color-d);

	transition: 0.5s;
}
.sidebar li {
	height: 55px;
	margin-top: 7px;
	list-style: none;
	display: flex;
	align-items: center;
	justify-content: center;
}
.sidebar li a {
	height: 120%;
	width: 100%;
	display: flex;
	align-items: center;
	text-decoration: none;
	border-top-left-radius: 15px;
	border-bottom-left-radius: 15px;
	transition: 0.5s;
}
.sidebar.close li a {
	border-radius: 15px;
	transition: 0.5s;
}

.sidebar li .anch:hover {
	background: var(--bg-color-d);
}

.sidebar li .anch:hover .icon,
.sidebar li .anch:hover .text {
	color: var(--bg-color-a);
}
.sidebar li .anch.active {
	background: var(--bg-color-d);
}
.sidebar li .anch.active .icon,
.sidebar li .anch.active .text {
	color: var(--bg-color-a);
}

.nav-link {
	padding-bottom: 10px;
	transition: 0.5s;
}
</style>

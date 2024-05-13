import { createRouter, createWebHistory } from "vue-router";
import LogIn_SignUp from "./LogIn_SignUp.vue";
import Home from "./components/Home.vue";
import Attraction from "./components/Attraction.vue";
import Dining from "./components/Dining.vue";
import Accomm from "./components/Accomm.vue";
import Events from "./components/Events.vue";
import Activities from "./components/Activities.vue";

import WeddingPack from "./components/events_subpages/WeddingPack.vue";
import FoodPack from "./components/events_subpages/FoodPack.vue";
import PrenupPack from "./components/events_subpages/PrenupPack.vue";
import ProposalPack from "./components/events_subpages/ProposalPack.vue";
import GuestProfile from "./components/GuestProfile.vue";
import Admin from "./components/admin/Admin.vue";
import Login from "./components/admin/Login.vue";

const router = createRouter({
	history: createWebHistory(),
	routes: [
		{ path: "/admin", component: Admin, name: "admin" },
		{ path: "/stafflogin", component: Login, name: "stafflogin" },
		{
			path: "/login",
			component: LogIn_SignUp,
			name: "login",
		},
		{ path: "/attraction", component: Attraction, name: "attraction" },
		{
			path: "/home",
			component: Home,
			name: "home",
		},

		{ path: "/accomm", component: Accomm, name: "accomm" },
		{ path: "/dining", component: Dining, name: "dining" },
		{
			path: "/events",
			component: Events,
			name: "events",
			children: [
				{
					path: "/events/wedding-pack",
					component: WeddingPack,
					name: "wedding",
				},
				{
					path: "/events/food-pack",
					component: FoodPack,
					name: "food",
				},
				{
					path: "/events/prenup-pack",
					component: PrenupPack,
					name: "prenup",
				},
				{
					path: "/events/proposal-pack",
					component: ProposalPack,
					name: "proposal",
				},
			],
		},
		{ path: "/activities", component: Activities },
		{
			path: "/profile",
			component: GuestProfile,
			name: "profile",
		},
	],
});

router.beforeEach((to, from, next) => {


	// Check if the user is logged in before accessing protected routes
	const token = localStorage.getItem("token");
	// const staff = localStorage.getItem("staff");
	// if (to.name !== "stafflogin" && !staff) {
	// 	// Scroll to the top of the page when accessing the staff login page
	// 	next({ name: "stafflogin" });
	// } else {
	// 	window.scrollTo(0, 0);
	// 	next();
	// }
	if (to.name !== "login" && !token && to.name !== "home") {
		// If the route is not the login page, home page, and the user is not logged in,
		// redirect to the login page
		next({ name: "login" });
	} else {
		// If the user is logged in or accessing the login page or home page, proceed to the next route
		next();
		
	}
	if (to.name === "login") {
		window.scrollTo(0, 0);
	}
});

export default router;

import { createRouter, createWebHistory } from "vue-router";
// import LogIn_SignUp from "./components/LogIn_SignUp.vue";
import WeddingPack from "./events_subpages/WeddingPack.vue";
import FoodPack from "./events_subpages/FoodPack.vue";
import PrenupPack from "./events_subpages/PrenupPack.vue";
import ProposalPack from "./events_subpages/ProposalPack.vue";

const router_event_sp = createRouter({
	name: "EventsNavBar",
	history: createWebHistory(),
	routes: [
		// { path: "/:index?", component: Viewer, props:true},
		{ path: "/events/wedding-pack", component: WeddingPack },
		{ path: "/events/food-pack", component: FoodPack },
		{ path: "/events/prenup-pack", component: PrenupPack },
		{ path: "/events/proposal-pack", component: ProposalPack },
	],
});

export default router_event_sp;

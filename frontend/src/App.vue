<template>
	<!-- Main layout structure with Navbar, router-view, and Footer -->
	<main>
		<nav class="sidebar" :class="{ close: isSidebarOpen }">
			<div class="bar-icon">
				<button class="bar-btn" @click="isSidebarOpen = !isSidebarOpen">
					<span class="fa-solid fa-bars"></span>
				</button>
			</div>
			<!-- Include Navbar component -->
			<Navbar @click="reloadPage" />
			<!-- Include Navbar component -->
			<div class="login-signup" v-if="!isUserLoggedIn">
				<span
					class="bi bi-person-circle profile-icon"
					@click="isSidebarOpen = !isSidebarOpen"
				></span>
				<p>ACCOUNT</p>
				<div class="log-box">
					<a href="/login">LOGIN</a>
				</div>
				<div class="log-box">
					<a href="/login">SIGNUP</a>
				</div>
			</div>
			<div class="login-signup" v-else>
				<span
					class="bi bi-person-circle profile-icon"
					@click="isSidebarOpen = !isSidebarOpen"
				></span>
				<p>ACCOUNT</p>
				<div class="log-box">
					<router-link to="/profile">PROFILE</router-link>
				</div>
				<div class="log-box">
					<router-link to="" @click.prevent="submitLogout"
						>LOGOUT</router-link
					>
					
				</div>
			</div>
		</nav>
		<!-- Router view to render the current route component -->
		<router-view />
		<!-- Include Footer component -->
		<Footer />
	</main>
</template>

<script>
// Import Navbar and Footer components
import Navbar from "./components/Nav.vue";
import Footer from "./components/Footer.vue";
import router from "./routes";
import { mapState } from "vuex";
import axios from "axios";

export default {
	// Register Navbar and Footer components
	name: "Sidebar",

	components: {
		Navbar,
		Footer,
	},

	data() {
		// Data property to control the sidebar state
		return {
			isSidebarOpen: true,
			isUserLoggedIn: false,
		};
	},
	computed: {
		...mapState(["currentRoute"]),
	},
	mounted() {
		if (this.isUserLoggedIn) {
			console.log("User logged in ", this.isUserLoggedIn);
		}
	},
	created() {
		const client = axios.create({
			baseURL: "http://127.0.0.1:8000",
		});
		const token = localStorage.getItem("token");
		const headers = {
			Authorization: `Token ${token}`,
			"Content-Type": "application/json",
		};
		// const stoken = localStorage.getItem("staff");
		// const sheaders = {
		// 	Authorization: `Token ${stoken}`,
		// 	"Content-Type": "application/json",
		// };

		client
			.get("api/user/", { headers: headers })
			.then((res) => {
				this.isUserLoggedIn = true;
			})
			.catch((error) => {
				console.log("ERROR", error);
				this.isUserLoggedIn = false;
			});
		// client
		// 	.get("api/sonyasstaff/", { headers: headers })
		// 	.then((res) => {
		// 		this.isUserLoggedIn = true;
		// 	})
		// 	.catch((error) => {
		// 		console.log("ERROR", error);
		// 		this.isUserLoggedIn = false;
		// 	});
	},
	methods: {
		submitLogout() {
			const token = localStorage.getItem("token");
			const headers = {
				Authorization: `Token ${token}`,
				"Content-Type": "application/json",
			};
			axios
				.post("http://127.0.0.1:8000/api/logout", { headers: headers })
				.then((res) => {
					this.isUserLoggedIn = false;
					console.log("Status:", res.status);
					localStorage.removeItem("token");
					localStorage.removeItem("username");
					window.scrollTo(0, 0);
					router.push({ name: "home" });
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
};
</script>

<style>
/* CSS styles for the component */
@import url("https://fonts.googleapis.com/css2?family=Playfair+Display:ital@0;1&display=swap");
@import url("https://fonts.googleapis.com/css2?family=Abel&family=Playfair+Display:ital@0;1&display=swap");

:root {
	--text-color-a: #68502b;
	--text-color-b: #e7d0b2;
	--text-color-c: #ffffff;
	--bg-color-a: #f4f1ed;
	--bg-color-b: #57716c;
	--bg-color-c: #4b4238;
	--bg-color-d: #05300edc;
	--card-color: #472f24;
}
* {
	margin: 0;
	padding: 0;
	box-sizing: border-box;
	user-select: none;
	list-style-type: none;
}

.sidebar .bar-icon {
	border-radius: 50%;
	margin: 0.3rem;
	transition: 1s;
	display: flex;
	align-items: center;
	justify-content: right;
	min-width: 60px;
	margin-left: 3px;
	font-size: 26px;
	text-align: center;
}
.bar-btn {
	height: 45px;
	width: 60px;
	border: none;
	font-size: 20px;
	padding-right: 10px;
	color: var(--bg-color-b);
	cursor: pointer;
	background: transparent;
}

.sidebar {
	position: fixed;
	top: 0;
	left: 0;
	height: 100%;
	width: 240px;
	padding-left: 8px;
	border-top-right-radius: 15px;
	background-color: var(--bg-color-a);
	transition: 0.3s;
	white-space: nowrap;
	z-index: 1000;
}
.sidebar.close {
	position: fixed;
	overflow: hidden;
	width: 64px;
	padding: 5px;
	text-align: center;
	justify-content: center;
	align-items: center;
}
.sidebar.close .text {
	opacity: 0;
	display: none;
}
.login-signup {
	margin-top: 10rem;
	justify-content: center;
	align-items: center;
}
.login-signup p {
	padding: 0.3rem;
	font-size: 15px;
	font-family: "Abel", sans-serif;
	font-weight: 400;
	font-style: normal;
	letter-spacing: 1px;
	color: #7c7878;
}
.login-signup .log-box:nth-child(3) a {
	margin: 0.3rem;
	position: relative;
	display: inline-flex;
	justify-content: center;
	align-items: center;
	width: 90%;
	height: 35px;
	background: rgb(13, 80, 13);
	font-size: 16px;
	font-family: "Abel", sans-serif;
	font-weight: 400;
	font-style: normal;
	color: var(--text-color-c);
	text-decoration: none;
	letter-spacing: 1px;
	transition: 0.5s;
}
.login-signup .log-box:nth-child(3):hover a {
	background: rgba(13, 80, 13, 0.815);
}
.login-signup .log-box:nth-child(4) a {
	margin: 0.3rem;
	position: relative;
	display: inline-flex;
	justify-content: center;
	align-items: center;
	width: 90%;
	height: 35px;
	border: 2px solid var(--bg-color-d);
	background-color: transparent;
	font-size: 16px;
	font-family: "Abel", sans-serif;
	font-weight: 400;
	font-style: normal;
	color: var(--bg-color-d);
	text-decoration: none;
	letter-spacing: 1px;
	transition: 0.5s;
}
.login-signup .log-box:nth-child(4):hover a {
	color: var(--text-color-c);
	background: rgba(13, 80, 13, 0.815);
}
.profile-icon {
	display: none;
	transition: 0.5s;
}
.sidebar.close .profile-icon:hover {
	color: var(--text-color-c);
	background-color: var(--bg-color-d);
	transition: 0.5s;
}
.sidebar.close .profile-icon {
	position: absolute;
	display: flex;
	align-items: center;
	justify-content: center;
	border: 0.5px solid var(--bg-color-d);
	margin-top: 5rem;
	color: var(--bg-color-d);
	width: 55px;
	height: 55px;
	border-radius: 50%;
	cursor: pointer;
	font-size: 25px;
	transition: 0.5s;
}

.sidebar.close .login-signup p,
.sidebar.close .login-signup .log-box:nth-child(3),
.sidebar.close .login-signup .log-box:nth-child(4) {
	display: none;
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

.sidebar .menu {
	margin-top: 2rem;
	height: clac(100% - 50px);
	display: flex;
	flex-direction: column;
	justify-content: space-between;
	transition: 0.5s;
}
.nav-link {
	padding-bottom: 10px;
	transition: 0.5s;
}
/* ================================================== Proposal Section ================================================== */

.events-hero1 {
    display: flex;
    justify-content: center;
	background-color: #57716C;
}

.events-hero1 img{
    margin-left: 3rem;
    padding: 2rem;
	width: 85%;
	height: 50rem;
	object-fit: cover;
	filter: brightness(50%);
	opacity: 90%;
}

.events-content{
    
    min-height: 300px;
    overflow: hidden;
    padding-bottom: 3rem;
}

.events-content-title{
    
    display: flex;
    justify-content: center;
}

.events-content-title h1{
    font-family: "Playfair Display", serif;
    font-size: 4rem;
    font-weight: 400;
    line-height: 73px;
    letter-spacing: -0.04em;
    color: #472F24;
}

.events-main-content-container{
    display: flex;  
    margin-top: 3rem;
    margin-inline: 3rem;
    overflow: hidden;
    border: #472F24 solid 5px;
    color: #472F24;
}

.events-main1{
	font-family: "abel", serif;
	font-size: 1.5rem;
	font-weight: 300;
    padding: 2rem;
    margin-left: 2rem;
    margin-top: 3rem;
    flex: 1;
}

.events-main2{
    padding-top: 5rem;
    padding-right: 2rem;
    flex: 1;
}

.prop li{
	font-size: 1.5rem;
	text-align: justify;
	list-style-type: disc;
}

.wisteria{
    border-bottom: #472F24 solid 3px;
}

.cherry-blossoms{
    margin-top: 3rem;
    border-bottom: #472F24 solid 3px;
}

.hydrangea{
    margin-top: 3rem;
}

.events-main1 h2{
    font-size: 60px;
    font-weight: 400;
    line-height: 73px;
    letter-spacing: -0.04em;
    text-align: left;
}

.events-main1 h3{
    font-size: 40px;
    font-weight: 400;
    line-height: 73px;
    letter-spacing: -0.04em;
    text-align: left;
}

.menu-list {
    font-size: 32px;
    font-weight: 400;
    line-height: 40.78px;
    letter-spacing: -0.04em;

	text-align: left;
	list-style-type: disc;
	padding-left: 1rem;
	margin-top: 1rem;
	margin-bottom: 2rem;
}

.events-main2-photo img{
    object-fit: cover;
    height: 60rem;
    filter: brightness(55%);
}

.events-main2-additional{
    margin-top: 3rem;
    justify-content: center;
    background-color: #57716C;
    color: white;
}

.events-main2-additional h2{
    font-family: "Playfair Display", serif;
    font-size: 3rem;
    font-weight: 400;
    line-height: 73px;
    letter-spacing: -0.04em;
    text-align: center;
    padding-top: 5rem;
    margin-bottom: 3rem;
}

.events-main2-additional ul{
    font-size: 31px;
    margin-left: 2rem;
    padding-right: 1rem;
    padding-bottom: 12rem;
}

/* ================================================== Prenup Section ================================================== */
.prenup-main-content-container{
    margin-top: 3rem;
    margin-inline: 3rem;

    
    overflow: hidden;
    border: #472F24 solid 5px;
    color: #472F24;
}

.prenup-paragraph1-container{
    margin-left: 6rem;
    margin-right: 6rem;
    padding-top: 3rem;
    padding-bottom: 3rem;
    border-bottom: #472F24 solid 3px;
}

.prenup-first-paragraph{
    font-family: "Abel", sans-serif;
    font-size: 35px;
    font-weight: 400;
    line-height: 61.17px;
    letter-spacing: -0.04em;
    text-align: center;
}

.prenup-flex-container{
    display: flex;
    padding: 2rem;
}

.prenup-flex1{
	font-family: "abel", serif;
    padding: 2rem;
    margin-left: 5rem;
    margin-right: 2rem;
    background-color: #57716C;
    color: #F4F1ED;
    flex: 1;
}

.prenup-flex1 h2{
    font-family: "Playfair Display", serif;
    font-size: 45px;
    font-weight: 400;
    line-height: 73px;
    letter-spacing: -0.04em;
    text-align: left;

}

.prenup-flex1 h3{
    font-family: "abel", serif;
    font-size: 35px;
    font-weight: 400;
    
    text-align: left;

}

.prenup-flex2{
    flex: 1;
}

.prenup-flex2 img{
    filter: brightness(65%);
    object-fit: cover;
    height: 100%;
    width: 88%;
}

/* ================================================== Food Section ================================================== */
.events-food1{
    text-align: center;
    color: #472F24;
}

.events-food1 h2{
    font-family: "Playfair Display", serif;
    font-size: 60px;
    font-weight: 400;
    line-height: 73px;
    letter-spacing: -0.04em;
    margin-top: 2rem;
    margin-bottom: 2rem;
}

.events-food1 h3{
    font-family: "Abel", sans-serif;
    font-size: 30px;
    font-weight: 400;
    line-height: 38.23px;
    letter-spacing: -0.04em;
    margin-top: 1rem;
    margin-bottom: 1rem;
}

.events-food2{
    display: flex;
}

.food2-note{
    background-color: #472F24;
    color: white;
	text-align: center;
	
    margin: 1rem .5rem;
    padding: 1rem;
    height: 23rem;
    width: 15rem;
}

.food2-note li{
    font-family: "Abel", sans-serif;
    font-size: 20px;
	list-style-type: disc;
}

.food2-note-title{
    font-family: "Abel", sans-serif;
    font-size: 25px;
    font-weight: 400;
    letter-spacing: 0.04em;
    
}

.events-food2-5{
    padding: 1rem .5rem;
    
}

.events-food2-5 img{
    height: 47rem;
    width: 22rem;
	object-fit: cover;
    filter: brightness(80%);
}

.prenup-main-content-container2{
    margin-top: 3rem;
    margin-inline: 3rem;
    height: 155vh;
    overflow: hidden;
    border: #57716C solid 5px;
    color: #57716C;
}

.events-food1-second{
    text-align: center;
    color: #57716C;
}

.events-food1-second h2{
    font-family: "Playfair Display", serif;
    font-size: 60px;
    font-weight: 400;
    line-height: 73px;
    letter-spacing: -0.04em;
    margin-top: 2rem;
    margin-bottom: 2rem;
}

.events-food1-second h3{
    font-family: "Abel", sans-serif;
    font-size: 30px;
    font-weight: 400;
    line-height: 38.23px;
    letter-spacing: -0.04em;
    margin-top: 1rem;
    margin-bottom: 1rem;
}

.food-second-main-container{
    display: flex;
    padding: 2rem;
}

.food-second-box1 img{
    flex: 1;
    margin-right: 2rem;
    filter: brightness(80%);
    width: 30rem;
	object-fit: cover;
    height: 100%;
}

.food-second-box2{
    flex: 1;
    background-color: #57716C;
    color: white;
    padding: 2rem;
    
}

.food-second-box2 h2{
    font-family: "Abel", sans-serif;
    font-size: 30px;
    font-weight: 400;
    line-height: 38.23px;
    letter-spacing: -0.04em;
    text-align: center;
    margin-bottom: 1rem;

}

.food-second-box2 h3{
    font-family: "Abel", sans-serif;
    font-size: 17px;
    font-weight: 400;
    line-height: 30.59px;
    
    text-align: justify;
    margin-bottom: 2rem;
}

.food-second-box2 li{
    font-family: "Abel", sans-serif;
    font-size: 17px;
    font-weight: 400;
    line-height: 30.59px;

}

</style>

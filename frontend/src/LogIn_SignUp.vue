<template>
	<main class="main-content">
		<section class="bg-login">
			<img class="bg-img-log" src="./Images/ReviewsBG.jpg" alt="" />
			<div class="loginWrapper">
				<div
					v-if="showLoginModal"
					class="modal-container fixed inset-0 flex items-center justify-center bg-black bg-opacity-50"
				>
					<div class="bg-white rounded-lg shadow-lg model-content">
						<span
							v-if="loginSuccess"
							class="icon material-icons-outlined"
						>
							check_circle
						</span>
						<span
							v-else
							class="icon material-icons-outlined mt-4 px-2 py-2"
						>
							error_outline
						</span>
						<p v-if="loginSuccess" class="success-m mt-4 px-2 py-2">
							Login successful!
						</p>

						<p v-else class="failed-m mt-2 px-2 py-2">
							Username or Password not found. <br />
							Please try again.
						</p>
						<!-- <p v-if="!registerSuccess" class="failed-m mt-4 px-2 py-2 ">
							Username or Email Address must be unique
						</p> -->
						<button
							v-if="!loginSuccess"
							@click="closeModal"
							class="mt-2 px-5 py-2 bg-red-800 text-white rounded-lg"
						>
							Close
						</button>
					</div>
				</div>
				<div
					v-if="showRegisterModal"
					class="modal-container fixed inset-0 flex items-center justify-center bg-black bg-opacity-50"
				>
					<div class="bg-white rounded-lg shadow-lg model-content">
						<span
							class="icon material-icons-outlined mt-4 px-2 py-2"
						>
							error_outline
						</span>

						<p class="failed-m mt-2 px-2 py-2">
							Use another username or email. <br />
							Please try again.
						</p>
						<!-- <p v-if="!registerSuccess" class="failed-m mt-4 px-2 py-2 ">
							Username or Email Address must be unique
						</p> -->
						<button
							v-if="!registerSuccess"
							@click="closeModal"
							class="mt-2 px-5 py-2 bg-red-800 text-white rounded-lg"
						>
							Close
						</button>
					</div>
				</div>
				<div
					v-if="showOtpModal"
					class="otp-modal fixed inset-0 flex items-center justify-center bg-black bg-opacity-50 modal-container transition-opacity duration-500"
				>
					<div
						class="otp-modal-content model-content bg-white rounded-lg shadow-lg justify-around"
					>
						<h2 class="p-4">OTP Verification</h2>
						<p class="p-6">
							Please enter the OTP sent to your email:
						</p>
						<input
							class="p-3 mb-3 h-15 bg-gray-200 hover:border-brown hover:bg-white transition duration-300 rounded"
							type="text"
							name="otp"
							v-model="otp"
							required
							placeholder="OTP"
						/>
						<div class="justify-evenly w-100">
							<button
								class="bg-blue-500 hover:bg-blue-200 m-2 w-40 rounded"
								@click="verifyOtp"
							>
								Verify
							</button>
							<button
								class="bg-red-500 hover:bg-red-200 m-2 w-40 rounded"
								@click="showOtpModal = false"
							>
								Close
							</button>
						</div>
					</div>
				</div>
				<ul class="tabs">
					<li class="active">Login</li>
					<li>Register</li>
				</ul>
				<ul class="tab__content">
					<li class="active">
						<div class="content__wrapper">
							<form method="POST" @submit.prevent="submitLogin">
								<!-- {% csrf_token %} -->
								<input
									type="text"
									name="username"
									v-model="username"
									placeholder="Username"
								/>
								<input
									type="password"
									name="password"
									v-model="password"
									placeholder="Password"
								/>
								<br />
								<a href="/forgot-password">Forgot Password?</a>
								<br />
								<input
									type="submit"
									value="Login"
									name="login"
									class="log-btn"
									@click="reloadPage"
								/>
							</form>
							<div class="benefits">
								<h1 class="benefit-divider">
									BOOKING BENEFITS
								</h1>
								<div class="benefits-con">
									<div class="benifit-card">
										<i
											class="fa-solid fa-percent benefit-icon"
										></i>
										<p>
											Get more savings on our
											accommodations.
										</p>
									</div>
									<div class="benifit-card">
										<i
											class="fa-solid fa-utensils benefit-icon"
										></i>
										<p>
											Complimentary Dinner or Lunch, with
											full Breakfast
										</p>
									</div>
									<div class="benifit-card">
										<i
											class="fa-solid fa-wifi benefit-icon"
										></i>
										<p>
											Wi-Fi is available at the dining
											area and the cottages.
										</p>
									</div>
								</div>
							</div>
						</div>
					</li>
					<li>
						<div class="content__wrapper">
							<form
								method="POST"
								@submit.prevent="submitRegistration"
							>
								<!-- {% csrf_token %} -->
								<input
									type="text"
									name="first_name"
									v-model="first_name"
									placeholder="First Name"
									required
								/>
								<input
									type="text"
									name="last_name"
									v-model="last_name"
									required
									placeholder="Last Name"
								/>
								<input
									type="tel"
									name="contact_number"
									v-model="contact"
									pattern="[0-9]{11}"
									required
									placeholder="09**********"
								/>
								<input
									type="text"
									name="location"
									v-model="location"
									required
									placeholder="Home Address"
								/>
								<input
									type="text"
									name="username"
									v-model="username"
									required
									placeholder="Username"
								/>
								<input
									type="email"
									name="email"
									v-model="email"
									required
									placeholder="Email Address"
								/>
								<input
									type="password"
									name="password"
									v-model="password"
									required
									placeholder="Password"
								/>
								<input
									type="password"
									name="password2"
									v-model="password2"
									required
									placeholder="Re-enter Password"
								/>
								<p
									v-if="!password && !password2"
									class="failed-m mt-2 px-2 py-2"
								></p>
								<p
									v-else-if="password !== password2"
									class="failed-m mt-2 px-2 py-2"
								>
									Passwords do not match.
								</p>

								<p v-else class="success-m mt-2 px-2 py-2">
									Passwords match.
								</p>
								<input
									type="submit"
									value="Register"
									name="register"
								/>
							</form>
						</div>
					</li>
				</ul>
			</div>
		</section>
	</main>
</template>
<script>
import axios from "axios";

import { ref } from "vue";
import router from "./routes";
import emailjs from "emailjs-com";
export default {
	name: "register-login",
	data() {
		return {
			// showLoginModal: null,
			// loginSuccess: null,
			object: null,
			// // Data property for showing/hiding the OTP modal
			// showOtpModal: false,
		};
	},
	setup() {
		const email = ref("");
		const first_name = ref("");
		const last_name = ref("");
		const location = ref("");
		const contact = ref("");

		// for OTP verification
		const otp = ref("");
		const showOtpModal = ref(false); // to show the OTP modal
		const otp_val = ref(null); // Define otp_val

		const username = ref("");
		const password = ref("");
		const password2 = ref("");
		const showLoginModal = ref(false);
		const loginSuccess = ref(false);
		const showRegisterModal = ref(false);
		const registerSuccess = ref(false);

		const client = axios.create({
			baseURL: "http://127.0.0.1:8000",
			withCredentials: true,
			timeout: 5000,
			xsrfCookieName: "csrftoken",
			xsrfHeaderName: "X-Csrftoken",
			headers: {
				"Content-Type": "application/json",
			},
		});
		const verifyOtp = () => {
			// Verify the OTP

			if (otp.value == otp_val.value) {
				alert("Email address verified...");

				// The OTP is valid

				// this.$emit("close-modal");
				// this.$emit("login-user", response.data.user);
				client
					.post("/api/register", {
						email: email.value,
						first_name: first_name.value,
						last_name: last_name.value,
						location: location.value,
						contact: contact.value,
						username: username.value,
						password: password.value,
					})
					.then((response) => {
						client
							.post("/api/login", {
								username: username.value,
								password: password.value,
							})
							.then((response) => {
								const token = response.data.token; // Replace with your token
								localStorage.setItem("token", token);
								localStorage.setItem(
									"username",
									response.data.user.username
								);

								router.push({ name: "home" }).then(() => {
									window.location.reload();
								});
							});
					})
					.catch((error) => {
						showRegisterModal.value = true;
						registerSuccess.value = false;
					});
			} else {
				alert("Invalid OTP");
			}
		};
		const submitRegistration = () => {
			otp_val.value = Math.floor(Math.random() * 900000) + 100000;

			emailjs
				.send(
					"service_d5qxdx5",
					"template_oqirukd",
					{
						to_email: email.value,
						to_name: `${first_name.value}_${last_name.value}`,
						message: `Your OTP is: ${otp_val.value}`,
					},
					"q4h4FsnDFS63Vb78i"
				)
				.then((message) => {
					if (message.text === "OK") {
						alert("OTP sent to your email " + email.value);
						showOtpModal.value = true;
					}
				});
		};

		const submitLogin = () => {
			//console.log(email.value, password.value);
			client
				.post("/api/login", {
					username: username.value,
					password: password.value,
				})
				.then((response) => {
					console.log("Login successful:", response.data);
					// Redirect to home page
					const token = response.data.token; // Replace with your token
					localStorage.setItem("token", token);
					localStorage.setItem(
						"username",
						response.data.user.username
					);
					router.push({ name: "home" }).then(() => {
						// After navigating to the "home" route, reload the page
						const client = axios.create({
							baseURL: "http://127.0.0.1:8000",
						});
						const token = localStorage.getItem("token");
						const headers = {
							Authorization: `Token ${token}`,
							"Content-Type": "application/json",
						};

						client
							.get("api/profile/", { headers: headers })
							.then((res) => {
								console.log(res.data);
							})
							.catch((error) => {
								console.log("ERROR", error);
							});
						window.location.reload();
					});
				})
				.catch((error) => {
					showLoginModal.value = true;
					loginSuccess.value = false;
				});
		};

		const submitLogout = () => {
			client.post("/api/logout").then((res) => {
				console.log("Logged out user:", response.data);
			});
		};

		// Watch for changes in currentUser
		const updateFormBtn = () => {
			registrationToggle.value = !registrationToggle.value;
		};
		const closeModal = () => {
			showLoginModal.value = false;
			showRegisterModal.value = false;
		};

		return {
			showOtpModal,
			otp,
			verifyOtp,
			closeModal,
			showLoginModal,
			loginSuccess,
			showRegisterModal,
			registerSuccess,
			email,
			contact,
			first_name,
			last_name,
			location,
			username,
			password,
			password2,
			updateFormBtn,
			submitRegistration,
			submitLogin,
			submitLogout,
		};
	},

	methods: {
		sendOTP() {
			const email = document.getElementById("email");
			const otpverify = document.getElementsByClassName("otpverify")[0];

			let otp_val = Math.floor(Math.random() * 10000);

			let emailbody = `<h2>Your OTP is </h2>${otp_val}`;
			Email.send({
				SecureToken: "fbebd213-4ddf-45d9-b205-3f5313s01cs3",
				To: email.value,
				From: "abc@gmail.com",
				Subject: "Email OTP using JavaScript",
				Body: emailbody,
			}).then((message) => {
				if (message === "OK") {
					alert("OTP sent to your email " + email.value);

					otpverify.style.display = "flex";
					const otp_inp = document.getElementById("otp_inp");
					const otp_btn = document.getElementById("otp-btn");

					otp_btn.addEventListener("click", () => {
						if (otp_inp.value == otp_val) {
							alert("Email address verified...");
						} else {
							alert("Invalid OTP");
						}
					});
				}
			});
		},
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

		client
			.get("api/user/", { headers: headers })
			.then((res) => {
				console.log(res.data);
			})
			.catch((error) => {
				console.log("ERROR", error);
			});
	},
	mounted() {
		var clickedTab = $(".tabs > .active");
		var tabWrapper = $(".tab__content");
		var activeTab = tabWrapper.find(".active");
		var activeTabHeight = activeTab.outerHeight();

		activeTab.show();
		tabWrapper.height(activeTabHeight);

		$(".tabs > li").on("click", function () {
			$(".tabs > li").removeClass("active");
			$(this).addClass("active");
			clickedTab = $(".tabs .active");
			activeTab.fadeOut(250, function () {
				$(".tab__content > li").removeClass("active");
				var clickedTabIndex = clickedTab.index();
				$(".tab__content > li").eq(clickedTabIndex).addClass("active");
				activeTab = $(".tab__content > .active");
				activeTabHeight = activeTab.outerHeight();
				tabWrapper
					.stop()
					.delay(50)
					.animate(
						{
							height: activeTabHeight,
						},
						500,
						function () {
							activeTab.delay(50).fadeIn(250);
						}
					);
			});
		});
	},
};
</script>

<style scoped>
.model-content {
	font-size: 25px;
	font-family: "Abel", sans-serif;
	font-weight: 100;
	font-style: normal;
	height: 40%;
	width: 40%;
	display: flex;
	flex-direction: column;
	justify-content: center;
	align-items: center;
	align-content: space-around;
}
.modal-container {
	z-index: 5;
}

.icon {
	font-size: 5rem;
	color: black;
}
.main_content {
	margin-left: 12.49%;
	background: #504b4b;
}

.bg-img-log {
	object-fit: cover;
	position: absolute;
	filter: brightness(0.5);
	opacity: 0.8;
	width: 100%;
	height: 100%;
	z-index: -1;
}
.loginWrapper {
	background: transparent;
	display: flex;
	flex-direction: column;
	position: relative;
	width: 50%;
	height: 100vh;
	justify-content: center;
	align-content: center;
	text-align: center;
	margin: auto;
	right: 0;
	left: 0;
	z-index: 100;
	transition: box-shadow 1s;
}

.logginFormFooter {
	text-align: center;
	color: #777;
	width: 100%;
	font-size: 12px;
	position: fixed;
	bottom: 10px;
}

.logginFormFooter a {
	color: #777;
	font-weight: 600;
}
.logginFormFooter a:hover {
	color: #aaa;
}

* {
	box-sizing: border-box;
	padding: 0;
	margin: 0;
}

nav {
	z-index: 9;
	color: #fff;
	position: fixed;
	top: 0;
	left: 0;
	width: 100%;
	padding: 20px 0;
	text-align: center;
}

.tabs {
	display: table;
	table-layout: fixed;
	width: 100%;
	-webkit-transform: translateY(5px);
	transform: translateY(5px);
	background-color: var(--text-color-a);
}

.tabs > li {
	transition-duration: 0.25s;
	display: table-cell;
	list-style: none;
	text-align: center;
	padding: 20px 20px 25px 20px;
	position: relative;
	overflow: hidden;
	cursor: pointer;
	color: #f7f0f0;

	background-color: none;
}
.tabs > li:before {
	z-index: -1;
	position: absolute;
	content: "";
	width: 100%;
	height: 120%;
	color: #000000;
	top: 0;
	left: 0;
	background-color: #ffffff;
	-webkit-transform: translateY(100%);
	transform: translateY(100%);
	transition-duration: 0.25s;
}

.tabs > li:hover:before {
	-webkit-transform: translateY(70%);
	transform: translateY(70%);
}
.tabs > li.active {
	color: #000000;
}
.tabs > li.active:before {
	transition-duration: 0.5s;
	background-color: #ffffff;
	-webkit-transform: translateY(0);
	transform: translateY(0);
}

.tab__content {
	position: relative;
	width: 100%;
	border-radius: 5px 5px 0px 0px;
	background-color: #ffffff;
	-webkit-box-shadow: 0px 12px 34px -8px rgba(0, 0, 0, 0.28);
	-moz-box-shadow: 0px 12px 34px -8px rgba(0, 0, 0, 0.28);
	box-shadow: 0px 12px 34px -8px rgba(0, 0, 0, 0.28);
}
.tab__content > li {
	width: 100%;
	position: absolute;
	border-radius: 5px;
	color: #000000;
	top: 0;
	left: 0;

	display: none;
	list-style: none;
}
.tab__content > li .content__wrapper {
	text-align: center;
	border-radius: 5px;
	padding-top: 24px;
	padding-bottom: 24px;
	background-color: #ffffff;
}

form input {
	border: none;
	padding: 12px;
	background: #d8d8d8;
	color: #0f0f0f;
	font-size: 16px;
	margin: 12px;
	width: 300px;
	font-weight: 100;
	outline: none;
	border-radius: 5px;
}

form input:first-child {
	margin-top: 8px;
	border-radius: 5px;
}
form input:last-child {
	margin-top: 16px;
	margin-bottom: 0px;
	margin-left: 0px;
}

form input:focus {
	background-color: #ffffff;
	border: 1px solid var(--text-color-a);
	border-radius: 5px;
}
form input:hover {
	background-color: #fff;
}
form input:placeholder {
	color: rgb(60, 60, 65);
}

form [type="submit"]:focus,
form [type="submit"]:hover {
	background: #275e02;
}

form [type="submit"] {
	background: #275e02;
	color: #fff;
	width: 60%;

	margin-bottom: 2rem;
	align-self: center;
	cursor: pointer;
}

::-webkit-input-placeholder {
	color: #504b4b;
}
:-moz-placeholder {
	color: #504b4b;
}
::-moz-placeholder {
	color: #504b4b;
}
:-ms-input-placeholder {
	color: #504b4b;
}

.benefit-divider {
	position: absolute;
	margin-bottom: 7.5rem;
	font-size: 20px;
	font-family: "Abel", sans-serif;
	font-weight: 400;
	font-style: normal;
	color: var(bg);
	background-color: var(--text-color-c);
	width: 15rem;
	text-align: center;
}

.benefits {
	padding-top: 1rem;
	user-select: none;
	border-top: 1px solid var(--card-color);
	margin: 2rem;
	height: 40%;
	display: flex;
	flex-direction: column;
	justify-content: center;
	align-items: center;
}

.benefit-icon {
	border-radius: 50%;
	background: var(--card-color);
	width: 85px;
	height: 50px;
	text-align: center;
	color: var(--bg-color-a);
	display: flex;
	justify-content: center;
	align-items: center;
	font-size: 15px;
}

.benefits-con {
	display: flex;
	justify-content: center;
	align-items: center;
	align-self: start;
	margin-top: 2.5rem;
}

.benifit-card {
	display: flex;
	justify-content: center;
	align-items: center;
	align-self: start;
}

.benifit-card p {
	margin-inline: 1rem;
	font-size: 15px;
	font-family: "Abel", sans-serif;
	font-weight: 400;
	font-style: normal;
	display: flex;
	justify-content: center;
	align-items: start;
	color: var(--card-color);
}
</style>

<template>
	<main class="main-content">
		<section class="profile-section">
			<div class="border-container">
				<div class="name-photo">
					<input
						type="file"
						id="photo-input"
						@change="handlePhotoChange"
						style="display: none"
						accept="image/*"
					/>
					<label for="photo-input">
						<img
							class="guest-photo"
							:src="picture"
							alt=""
							@click="openPhotoInput"
						/>
					</label>
					<h1 class="full-name text-4xl font-bold">
						{{ first_name }} {{ last_name }}
					</h1>
					
				</div>
				<div class="editable-data mt-4 justify-content-end w-50">
						<i
							class="material-icons edit-data-icon"
							@click="isEditing ? saveChanges() : toggleEditing()"
						>{{ isEditing ? 'check' : 'edit' }}</i
						>
					</div>
				<form class="guest-data">

					<div class="labels">
						<p for="username">Username:</p>
						<p for="email">Email:</p>
						<!-- <p for="password">Password:</p> -->
						<p for="contact">Contact:</p>
						<p for="address">Address:</p>
					</div>
					<div class="data">
						<div class="editable-data">
							<input
								type="text"
								id="username"
								name="username"
								v-model="username"
								:readonly="!isEditing"
								ref="usernameInput"
							/>
						</div>

						<div class="editable-data">
							<input
								type="email"
								id="email"
								name="email"
								v-model="email"
								:readonly="!isEditing"
								ref="emailInput"
							/>
						</div>

						<!-- <div class="editable-data">
							<input
								type="password"
								id="password"
								name="password"
								v-model="password"
								:readonly="!isEditing"
								ref="passwordInput"
							/>
						</div> -->

						<div class="editable-data">
							<input
								type="text"
								id="contact"
								name="contact"
								v-model="contact"
								ref="contactInput"
								
								readonly
							/>
						</div>

						<div class="editable-data">
							<input
								type="text"
								id="address"
								name="address"
								v-model="location"
								:readonly="!isEditing"
								ref="addressInput"
							/>
						</div>
					</div>
				</form>
			</div>
		</section>
		<section class="booking-history-section">
			<div class="booking-history">
				<h1 class="booking-divider">BOOKINGS</h1>
				<div
					class="bookings"
					v-for="book in booking_data"
					:key="book.id"
				>
					<span class="material-icons-outlined icon">bed</span>
					<div class="booking-details">
						<h1 class="header-name">{{ book.room_type }}</h1>
						<p class="number-guests">
							For {{ book.adults_count }} adults
							{{ book.children_count }} Children
						</p>
						<div class="booking-date">
							<input
								type="date"
								id="date-now"
								name="date"
								v-model="book.check_in"
								readonly
							/>
							<p>-</p>
							<input
								type="date"
								id="date-to"
								name="date"
								v-model="book.check_out"
								readonly
							/>
						</div>
						<p class="booking-id">{{ book.booking_id }}</p>
					</div>
					<h1 class="amount">{{ book.total_price }}php</h1>
				</div>
			</div>
		</section>
	</main>
</template>

<script>
import axios from "axios";

export default {
	name: "Profile",
	data() {
		return {
			email: null,
			contact:null,
			first_name: null,
			last_name: null,
			password: null,
			location: null,
			picture: null,
			username: null,
			booking_data: [],
			isEditing: false,
		};
	},

	methods: {
		handlePhotoChange(event) {
			const file = event.target.files[0];
			// Handle the file upload logic here
			const fileName = file.name;
			this.picture = fileName;
			console.log(fileName);
			// const reader = new FileReader();
			// reader.onload = (e) => {
			// 	this.picture = e.target.result;
			// };
			// reader.readAsDataURL(file);
			// const formData = new FormData();
			// formData.append("file", file);
			// axios
			// 	.post("http://127.0.0.1:8000/api/upload", formData, {
			// 		headers: {
			// 			"Content-Type": "multipart/form-data",
			// 		},
			// 	})
			// 	.then((response) => {
			// 		console.log(response.data);
			// 	})
			// 	.catch((error) => {
			// 		console.log(error);
			// 	});
		},
		toggleEditing() {
			this.isEditing = !this.isEditing;
			if (this.isEditing) {
				this.$refs.usernameInput.removeAttribute("readonly");
				this.$refs.emailInput.removeAttribute("readonly");
				this.$refs.passwordInput.removeAttribute("readonly");
				this.$refs.addressInput.removeAttribute("readonly");
				this.$refs.contactInput.setAttribute("readonly");
				
			} else {
				this.$refs.usernameInput.setAttribute("readonly", true);
				this.$refs.emailInput.setAttribute("readonly", true);
				this.$refs.contactInput.setAttribute("readonly", true);
				this.$refs.passwordInput.setAttribute("readonly", true);
				this.$refs.addressInput.setAttribute("readonly", true);
			}
		},
		saveChanges() {
			const client = axios.create({
				baseURL: "http://127.0.0.1:8000",
			});
			const token = localStorage.getItem("token");
			const headers = {
				Authorization: `Token ${token}`,
				"Content-Type": "application/json",
			};
			const data = {
				email: this.email,
				first_name: this.first_name,
				last_name: this.last_name,
				location: this.location,
				password: this.password,
				picture: this.picture,
				username: this.username,
			};

			client
				.put("api/profile", data, { headers: headers })
				.then((res) => {
					console.log("Profile updated successfully");
				})
				.catch((error) => {
					console.log("ERROR", error);
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
		console.log(token);

		client
			.get("api/profile", { headers: headers })
			.then((res) => {
				console.log("user: ", res.data);
				this.email = res.data.email;
				this.first_name = res.data.first_name;
				this.last_name = res.data.last_name;
				this.location = res.data.location;
				this.contact = res.data.contact;
				this.password = res.data.password;
				this.picture = res.data.picture;
				this.username = res.data.username;
			})
			.catch((error) => {
				console.log("ERROR", error);
			});
		client
			.get("api/submitbooking", { headers: headers })
			.then((res) => {
				this.booking_data = res.data.reverse();
				console.log("booking_data: ", this.booking_data);
			})
			.catch((error) => {
				console.log("ERROR", error);
			});
	},
};
</script>

<style scoped>
main {
	margin-left: 4.3%;
	display: flex;
	flex-direction: column;
	justify-content: center;
	background: var(--bg-color-b);
}
.profile-section {
	height: 100vh;
	background: var(--bg-color-b);
}
.booking-history-section {
	background: var(--bg-color-b);
	padding-bottom: 2rem;
}
.border-container {
	display: flex;
	flex-direction: column;
	align-items: center;
	justify-content: center;
	margin: 4rem;
	border: 2px solid var(--text-color-b);
	border-bottom: none;
	height: 100%;
}

/*font-family: "Abel", sans-serif;
	font-weight: 400;
	font-style: normal;
	font-family: "Playfair Display", serif;
	font-weight: 400;
	font-style: normal;
	
	*/
.name-photo {
	display: flex;
	flex-direction: column;
	align-items: center;
	justify-content: center;
}
.guest-photo {
	width: 15rem;
	height: 15rem;
	border-radius: 50%;
	object-fit: cover;
	cursor: pointer;
}
.full-name {
	font-family: "Playfair Display", serif;
	font-weight: 400;
	font-style: normal;
	font-size: 45px;
	color: var(--text-color-b);
	padding-block: 1rem;
}
.guest-data {
	display: flex;
	width: 70%;
	justify-content: center;
	align-items: center;
	font-size: 25px;
	font-family: "Abel", sans-serif;
	font-weight: 400;
	height: 20rem;
	padding-inline: 3rem;
}
.labels {
	width: 20%;
	display: flex;
	font-family: "Abel", sans-serif;
	font-weight: 400;
	color: var(--text-color-b);
	flex-direction: column;
	justify-content: space-around;
	height: 80%;
}

.data {
	display: flex;
	flex-direction: column;
	justify-content: space-around;
	height: 80%;
	width: 60%;
}
.data input {
	width: 100%;
	font-family: "Abel", sans-serif;
	font-weight: 400;
	color: var(--text-color-b);
	background: transparent;
	padding-left: 1rem;
	margin-right: 1rem;
}
.editable-data {
	display: flex;
}
.edit-data-icon {
	cursor: pointer;
	color: var(--text-color-b);
}
.booking-divider {
	position: absolute;
	top: 53rem;
	font-size: 35px;
	font-family: "Abel", sans-serif;
	font-weight: 400;
	font-style: normal;
	color: var(--text-color-b);
	background-color: var(--bg-color-b);
	width: 17rem;
	text-align: center;
}
.bookings {
	border-top: 1px solid var(--text-color-b);
	display: flex;
	align-items: center;
	justify-content: space-around;
	font-family: "Abel", sans-serif;
	font-weight: 400;
	font-style: normal;
	color: var(--text-color-b);
	font-size: 25px;
	height: 20rem;
	width: 80%;
}

.booking-history {
	padding-top: 5rem;
	display: flex;
	justify-content: center;
	flex-direction: column;
	align-items: center;
	border: 2px solid var(--text-color-b);
	border-top: none;
	margin-inline: 4rem;
}

.header-name {
	font-family: "Playfair Display", serif;
	font-weight: 400;
	font-style: normal;
}

.booking-date {
	display: flex;
	justify-content: space-evenly;
}
.booking-date input {
	background: transparent;
}

.booking-id {
	color: var(--card-color);
	margin-top: 1rem;
	width: 7rem;
	text-align: center;
	background: var(--text-color-b);
	transition: 0.5s;
}

.icon {
	font-size: 4rem;
}
/*:root {
	--text-color-a: #68502b;
	--text-color-b: #e7d0b2;
	--text-color-c: #ffffff;
	--bg-color-a: #f4f1ed;
	--bg-color-b: #57716c;
	--bg-color-c: #4b4238;
	--bg-color-d: #05300edc;
	--card-color: #472f24;
}*/
</style>

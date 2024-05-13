<template>
	<main>
		<section class="first-row">
			<!-- Slider container -->
			<div class="slider">
				<!-- Slider images list -->
				<ul id="slider-list">
					<!-- Slide 1 -->
					<li id="no-js-slider-1" class="slide">
						<!-- Image for slide 1 -->
						<img src="../Images/lover_s suite.jpeg" />
						<!-- Overlay content for slide 1 -->
						<div class="overlay-content">
							<!-- Title for slide 1 -->
							<h2>Lover’s Suite</h2>
							<!-- Description for slide 1 -->
							<div class="descript">
								<p>
									A romantic escape for two with a king-sized
									bed and a private balcony, creating an
									intimate retreat.
								</p>
							</div>
						</div>
						<!-- Navigation: previous slide -->
						<a class="prev" href="#no-js-slider-3">prev</a>
						<!-- Navigation: next slide -->
						<a class="next" href="#no-js-slider-2">next</a>
					</li>
					<!-- Slide 2 -->
					<li id="no-js-slider-2" class="slide">
						<!-- Image for slide 2 -->
						<img src="../Images/family suite.jpeg" />
						<!-- Overlay content for slide 2 -->
						<div class="overlay-content">
							<!-- Title for slide 2 -->
							<h2>Family Suite</h2>
							<!-- Description for slide 2 -->
							<div class="descript">
								<p>
									Enjoy a cozy family getaway with a
									king-sized bed and a comfortable sofa bed in
									our Family Suite, complete with a private
									balcony for shared moments.
								</p>
							</div>
						</div>
						<!-- Navigation: previous slide -->
						<a class="prev" href="#no-js-slider-1">prev</a>
						<!-- Navigation: next slide -->
						<a class="next" href="#no-js-slider-3">next</a>
					</li>
					<!-- Slide 3 -->
					<li id="no-js-slider-3" class="slide">
						<!-- Image for slide 3 -->
						<img src="../Images/business suite.webp" />
						<!-- Overlay content for slide 3 -->
						<div class="overlay-content">
							<!-- Title for slide 3 -->
							<h2>Business Suite</h2>
							<!-- Description for slide 3 -->
							<div class="descript">
								<p>
									A romantic escape for two, our Business
									Suite features a king-sized bed and a
									private balcony, creating an intimate
									retreat for corporate travelers.
								</p>
							</div>
						</div>
						<!-- Navigation: previous slide -->
						<a class="prev" href="#no-js-slider-2">prev</a>
						<!-- Navigation: next slide -->
						<a class="next" href="#no-js-slider-1">next</a>
					</li>
				</ul>
			</div>
			<!-- Select container -->
			<div class="select">
				<!-- Choices container -->
				<div class="choices">
					<!-- Option 1 -->
					<a
						href="#no-js-slider-1"
						class="the-option"
						active-class="active"
					>
						<!-- Image for option 1 -->
						<img src="../Images/lover_s suite.jpeg" alt="" />
					</a>
					<!-- Option 2 -->
					<a
						href="#no-js-slider-2"
						class="the-option"
						active-class="active"
					>
						<!-- Image for option 2 -->
						<img src="../Images/family suite.jpeg" alt="" />
					</a>
					<!-- Option 3 -->
					<a
						href="#no-js-slider-3"
						class="the-option"
						active-class="active"
					>
						<!-- Image for option 3 -->
						<img src="../Images/business suite.webp" alt="" />
					</a>
				</div>
			</div>
		</section>

		<!-- This section represents the booking interface and information about rooms and cottages at Sonya's Garden Bed and Breakfast in Tagaytay. It allows users to select dates, room types, and the number of guests for their stay, along with providing details about booking benefits and room descriptions. -->
		<section class="second-row">
			<div class="outer-container">
				<div class="book-container">
					<h1 class="book-header">Book your Stay</h1>
					<div class="inner-book">
						<div class="date-col cols">
							<p class="date-title">DATE</p>
							<div class="date-select">
								<input type="date" id="date-now" name="date" />
								<p>to</p>
								<input type="date" id="date-to" name="date" />
							</div>
						</div>

						<div class="room-col cols">
							<p class="room-title">ROOM</p>
							<div class="room-drop">
								<p class="room-name">Lover's Suite</p>
								<span class="arrow"
									><i class="fa-solid fa-angle-down"></i
								></span>
							</div>
							<div class="room-drop-content inactive">
								<div class="flex justify-between suite">
									<p class="lover-suite text-start">
										Lover's Suite
									</p>
									<p class="pr-2">
										Available rooms: {{ loverSuite }}
									</p>
								</div>
								<span></span>
								<div class="flex justify-between suite">
									<p class="business-suite text-start">
										Business Suite
									</p>
									<p class="pr-2">
										Available rooms: {{ businessSuite }}
									</p>
								</div>
								<span></span>
								<div
									class="flex justify-between suite text-start"
								>
									<p class="family-suite">Family Suite</p>
									<p class="pr-2">
										Available rooms: {{ familySuite }}
									</p>
								</div>
							</div>
						</div>

						<div class="guest-col cols">
							<p class="guest-title">GUEST</p>
							<div class="guest-drop">
								<p>
									
									<span class="adult">1</span> Adult,
									<span class="child">0</span> Children
								</p>
								<span class="arrow"
									><i class="fa-solid fa-angle-down"></i
								></span>
							</div>
							<div class="guest-drop-content inactive">
								<p class="drop-container">
									<span class="room-minus minus opacity-0 " style="cursor: default;">-</span>
									
									<span class="text">Guests</span>
									<span class="room-plus plus opacity-0" style="cursor: default;">+</span>
								</p>
								<p
									class="drop-container"
									style="
										border-top: 2px solid #e7d0b2;
										border-bottom: 2px solid #e7d0b2;
									"
								>
									<span class="adult-minus minus">-</span>
									<span
										class="adult-no"
										style="padding-right: 0.5rem"
										>1</span
									>
									<span class="text">Adults</span>
									<span class="adult-plus plus">+</span>
								</p>
								<p class="drop-container">
									<span class="child-minus minus">-</span>
									<span
										class="child-no"
										style="padding-right: 0.5rem"
										>0</span
									>
									<span class="text">Children</span>
									<span class="child-plus plus">+</span>
								</p>
							</div>
						</div>

						<div
							type="button"
							class="btn book-btn"
							data-toggle="modal"
							data-target="#booking-modal"
							@click.prevent="transferTextContent"
						>
							BOOK NOW
						</div>
						<!-- Modal -->
						<div
							class="modal fade"
							id="booking-modal"
							data-backdrop="static"
							tabindex="-1"
							aria-labelledby="staticBackdropLabel"
							aria-hidden="true">
							date-select
							<div class="modal-dialog modal-l">
								<div class="modal-content">
									<div class="box-2">
										<div class="form-summary">
											<div class="form-cont" style="">
												<h2
													class="modal-title booking-summary-title"
													id="staticBackdropLabel"
												>
													Booking Summary
												</h2>
												<h4 class="summary-subtitle">
													Assigned Stay
												</h4>
												<h3 id="" class="summary-info">
													<div class="date-select">
														<p>from</p>
														<input
															type="date"
															id="date-now"
															name="date"
															class="date-mod date-now-m"
															readonly
														/>
														<p>to</p>
														<input
															type="date"
															id="date-to"
															name="date"
															class="date-mod date-to-m"
															readonly
														/>
													</div>
												</h3>
												<h4 class="summary-subtitle">
													Room Booked
												</h4>
												<h3
													id=""
													class="summary-info room-name-sum"
												>
													Lover’s Suite
												</h3>
												<h4 class="summary-subtitle">
													Number of Guests
												</h4>
												<h3 id="" class="summary-info">
													
													<span class="adult-num"
														>1</span
													>
													Adult,
													<span class="child-num"
														>0</span
													>
													Child
												</h3>
											</div>

											<div class="box-2-prices-container">
												<div
													class="summary-info-box pr-9"
												>
													<h3
														id=""
														class="summary-info"
													>
														<span
															class="adult-num-mod"
															>1</span
														>
														Adults
													</h3>
													<h3
														id=""
														class="summary-info"
													>
														<span
															class="child-num-mod"
															>1</span
														>
														Child
													</h3>
													<h3
														id=""
														class="summary-info"
													>
														Discount
													</h3>
												</div>
												<div class="summary-price-box">
													<h3
														id=""
														class="summary-info price-adult"
													>
														₱ 3000.00 ea
													</h3>
													<h3
														id=""
														class="summary-info price-child"
													>
														₱ 500 ea
													</h3>
													<h3
														id=""
														class="summary-info discounts"
													>
														₱ -500
													</h3>
												</div>
											</div>
										</div>
										<div class="summary-border"></div>
										<div class="box-2-prices-container1">
											<div class="summary-info-box">
												<h3 id="" class="summary-info">
													Total :
												</h3>
											</div>
											<div class="summary-price-box">
												<h3
													id=""
													class="summary-info total-price"
													style="margin-top: 6px"
												>
													₱ 6000.00
												</h3>
											</div>
										</div>
										<div class="menu-button-div">
											<a
												class="btn menu-btn"
												data-dismiss="modal"
												@click.prevent="saveBooking"
												>Confirm</a
											>
											<button
												type="button"
												class="btn btn-cancel"
												data-dismiss="modal"
											>
												Cancel
											</button>
										</div>
									</div>
								</div>
							</div>
						</div>
					</div>

					<div>
						<!-- Snackbar for failed booking -->
						<div
							v-if="showFailedSnackbar"
							class="fixed bottom-0 left-0 right-0 flex items-center justify-center w-full JakeCitrus h-16 bg-red-500 text-white"
						>
							<p>Booking failed. Please try again.</p>
						</div>
						<!-- Snackbar for successful booking -->
						<div
							v-if="showSuccessSnackbar"
							class="fixed bottom-0 left-0 right-0 flex items-center justify-center w-full z-50 h-16 bg-green-500 text-white"
						>
							<p>Booking successful!</p>
						</div>
						<!-- Rest of your code -->
						<!-- ... -->
					</div>

					<div class="benefits">
						<h1 class="benefit-divider">BOOKING BENEFITS</h1>
						<div class="benefits-con">
							<div class="benifit-card">
								<i class="fa-solid fa-percent benefit-icon"></i>
								<p>Get more savings on our accommodations.</p>
							</div>
							<div class="benifit-card">
								<i
									class="fa-solid fa-utensils benefit-icon"
								></i>
								<p>
									Complimentary Dinner or Lunch, with full
									Breakfast
								</p>
							</div>
							<div class="benifit-card">
								<i class="fa-solid fa-wifi benefit-icon"></i>
								<p>
									Wi-Fi is available at the dining area and
									the cottages.
								</p>
							</div>
						</div>
					</div>
				</div>
				<div class="room-suites">
					<h1 class="room-header">Rooms and Cottages</h1>
					<p>
						Experience a relaxing getaway and recharge your mind and
						body at Sonya's Garden magical Bed and Breakfast in
						Tagaytay. Connect with nature and breathe in fresh air
						while indulging in healthy meals. Check out our
						family-style accommodations today!
					</p>
					<br />
					<p>
						Many guests have already vowed to return for the simple
						joys it offers, like waking up to the smell of flowers,
						languishing in bed from last night’s soothing massage,
						contemplating in the undisturbed solitude that surrounds
						each cottage, relaxing by the charming bay windows that
						open to a resplendent view of nature, enjoying the warm
						hospitality of Sonya and her staff—and other delightful
						discoveries that has made a stay at the B&B a unique
						experience for every person.
					</p>
					<br />
					<p>
						The B&B has become a popular destination for a romantic
						getaway. One of the best times to spend the night at
						Sonya’s is during the hushed nights at the beginning of
						the week, when the garden is quiet save for the crickets
						and their song, or the soft tinkling of glass chimes
						that signals the passing of breeze. The damp months of
						June to October lure the romantic with the murmur of
						falling rain and the resulting sparkle of a dew-draped
						garden.
					</p>
				</div>
			</div>
		</section>

		<!-- This section showcases different suite options available for booking, each with a brief description highlighting key features and amenities, along with a "SEE DETAILS" button for users to explore further. -->
		<section class="third-row">
			<div class="book-cards">
				<div class="book-card">
					<img src="../Images/lover_s suite.jpeg" alt="" />
					<h1>Lover’s Suite</h1>
					<p>
						The Lovers Suite for 2 offers an intimate and romantic
						escape, featuring a plush king-sized bed, a private
						balcony with panoramic views, and a luxurious spa-style
						bathroom for an indulgent and unforgettable romantic
						retreat.
					</p>
					<div class="btn-box">
						<a href="#">SEE DETAILS</a>
					</div>
				</div>
				<div class="book-card">
					<img src="../Images/family suite.jpeg" alt="" />

					<h1>Family Suite</h1>
					<p>
						The Family Suite for 4 provides a comfortable and
						spacious haven with two separate beds, a well-appointed
						living area, and thoughtful amenities, ensuring a
						delightful stay for families to relax and enjoy quality
						time together.
					</p>
					<div class="btn-box">
						<a href="#">SEE DETAILS</a>
					</div>
				</div>
				<div class="book-card">
					<img src="../Images/business suite.webp" alt="" />
					<h1>Business Suite</h1>
					<p>
						The Business Suite for 2 provides a sophisticated and
						functional space with a dedicated workspace, high-speed
						internet, and modern amenities, catering to the needs of
						business travelers for a productive and comfortable
						stay.
					</p>
					<div class="btn-box">
						<a href="#">SEE DETAILS</a>
					</div>
				</div>
			</div>
		</section>
	</main>
</template>

<script>
import axios from "axios";
export default {
	setup() {},
	created() {
		const token = localStorage.getItem("token");
		const headers = {
			Authorization: `Token ${token}`,
			"Content-Type": "application/json",
		};
		axios
			.get("http://localhost:8000/api/checkrooms/", { headers })
			.then((response) => {
				this.room_number = response.data.map(
					(room) => room.room_number
				);
				console.log("Available rooms:", this.room_number);
				// Get the room count each of the  three option o room type

				this.loverSuite = response.data.filter(
					(room) => room.room_type === "Lover's Suite" && room.availability === true
				).length;
				this.businessSuite = response.data.filter(
					(room) => room.room_type === "Business Suite" && room.availability === true
				).length;
				this.familySuite = response.data.filter(
					(room) => room.room_type === "Family Suite" && room.availability === true
				).length;
			})
			.catch((error) => {
				console.error("Error creating booking:", error.response.data);
				// Optionally, you can handle the error here
			});
	},
	data() {
		return {
			loverSuite: 0,
			familySuite: 0,
			businessSuite: 0,
			total_price: null,
			room_number: [],
			showFailedSnackbar: false,
			showSuccessSnackbar: false,
		};
	},

	methods: {
		transferTextContent() {
			const today = new Date().toISOString().split("T")[0];
			document.getElementById("date-now").setAttribute("min", today);
			document.getElementById("date-to").setAttribute("min", today);

			const roomName = document.querySelector(".room-name");
			// const roomNo = document.querySelector(".room");
			const adult = document.querySelector(".adult");
			const child = document.querySelector(".child");
			const dateTo = document.getElementById("date-to");
			const dateFrom = document.getElementById("date-now");
			//------------------------------------------------//
			const _roomName = document.querySelector(".room-name-sum");
			// const _roomNo = document.querySelector(".room-num");
			const _adult = document.querySelector(".adult-num");
			const _child = document.querySelector(".child-num");
			const m_adult = document.querySelector(".adult-num-mod");
			const m_child = document.querySelector(".child-num-mod");
			const _dateTo = document.querySelector(".date-to-m");
			const _dateFrom = document.querySelector(".date-now-m");
			const total = document.querySelector(".total-price");
			const disc = document.querySelector(".discounts");
			const room_price = document.querySelector(".price-adult");

			function countDivisionsByTwo(number) {
				let count = 0;
				while (number >= 2) {
					count++;
					number = Math.floor(number / 2);
				}
				return count;
			}

			let numberadult = parseInt(adult.textContent);
			let numberchild = parseInt(child.textContent);
			let count =
				numberadult >= 2 ? countDivisionsByTwo(numberadult) * 500 : 0;

			console.log("Number of divisions by 2:", count, numberadult);

			let price_room = 0;
			if (roomName.textContent.toString().includes("Lover's Suite")) {
				price_room = 4000;
			} else if (
				roomName.textContent.toString().includes("Business Suite")
			) {
				price_room = 3500;
			} else if (
				roomName.textContent.toString().includes("Family Suite")
			) {
				price_room = 3000;
			}
			console.log(
				roomName.textContent.toString() + "num room: " + price_room
			);
			let peradult = price_room * numberadult;
			peradult -= count;
			console.log(peradult);
			let perchild = 500 * numberchild;
			let total_price = peradult + perchild;

			if (_dateTo == null || _dateFrom == null) {
				const now = new Date();
				_dateFrom.value = now.toISOString().split("T")[0];

				// Calculate and set tomorrow's date to dateTo input
				const tomorrow = new Date(now.getTime() + 24 * 60 * 60 * 1000);
				_dateTo.value = tomorrow.toISOString().split("T")[0];
				const dateFrom = new Date(_dateFrom.value); // Assuming _dateFrom is an input element
				const dateTo = new Date(_dateTo.value); // Assuming _dateTo is an input element

				const differenceInTime = dateTo.getTime() - dateFrom.getTime();
				const differenceInDays = differenceInTime / (1000 * 3600 * 24);
				console.log("Difference in days:", differenceInDays);
			}
			const date_From = new Date(dateFrom.value); // Assuming _dateFrom is an input element
			const date_To = new Date(dateTo.value); // Assuming _dateTo is an input element

			const differenceInTime = date_To.getTime() - date_From.getTime();
			const differenceInDays = differenceInTime / (1000 * 3600 * 24);
			console.log("Difference in days:", differenceInDays);
			total_price *= differenceInDays;
			this.total_price = total_price;
			room_price.textContent = "₱ " + price_room + " ea";
			disc.textContent = "-₱ " + count;
			total.textContent = "₱ " + total_price;
			_roomName.textContent = roomName.textContent;
			// _roomNo.textContent = roomNo.textContent;
			_adult.textContent = numberadult;
			_child.textContent = child.textContent;
			m_adult.textContent = adult.textContent;
			m_child.textContent = child.textContent;
			_dateTo.value = dateTo.value;
			_dateFrom.value = dateFrom.value;
			console.log("Source roomName text content:", dateTo.value);

			const room_type = roomName.textContent;
			const token = localStorage.getItem("token");
			const headers = {
				Authorization: `Token ${token}`,
				"Content-Type": "application/json",
			};
			axios
				.get(`http://localhost:8000/api/checkrooms/`, { headers })
				.then((response) => {
					this.room_number = response.data
						.filter((room) => room.room_type === room_type)
						.map((room) => room.room_number);
					console.log("Available rooms:", this.room_number);
				})
				.catch((error) => {
					console.error(
						"Error creating booking:",
						error.response.data
					);
					// Optionally, you can handle the error here
				});

			// Optionally return a value from the method if needed
		},
		saveBooking() {
			const _roomName = document.querySelector(".room-name-sum");
			// const _roomNo = document.querySelector(".room-num");
			const _adult = document.querySelector(".adult-num");
			const _child = document.querySelector(".child-num");
			const _dateTo = document.querySelector(".date-to-m");
			const _dateFrom = document.querySelector(".date-now-m");

			const room_type = _roomName.textContent;
			// const room_count = _roomNo.textContent;
			const adults_count = _adult.textContent;
			const children_count = _child.textContent;

			const check_out = _dateTo.value;
			const check_in = _dateFrom.value;
			const randomRoomNumber =
				this.room_number[
					Math.floor(Math.random() * this.room_number.length)
				];
			console.log(randomRoomNumber);
			const token = localStorage.getItem("token");
			const headers = {
				Authorization: `Token ${token}`,
				"Content-Type": "application/json",
			};
			console.log(this.total_price);
			const data = {
				room_type: room_type,
				room_number: randomRoomNumber,
				// room_count: room_count,
				adults_count: adults_count,
				children_count: children_count,
				total_price: parseFloat(this.total_price),
				check_in: check_in,
				check_out: check_out,
			};

			// Send POST request to Django backend
			axios
				.post("http://localhost:8000/api/submitbooking/", data, {
					headers,
				})
				.then((response) => {
					console.log("Booking created successfully:", response.data);
					this.showSuccessBookingSnackbar();
				})
				.catch((error) => {
					console.error(
						"Error creating booking:",
						error.response.data
					);
					// Optionally, you can handle the error here
				});
		},
		showSuccessBookingSnackbar() {
			this.showSuccessSnackbar = true;
			// Automatically hide after 3 seconds
			setTimeout(() => {
				this.hideSuccessBookingSnackbar();
			}, 5000);
		},
		hideSuccessBookingSnackbar() {
			this.showSuccessSnackbar = false;
		},
	},

	mounted() {
		//this.total_price = total_of_price;
		// myModal.addEventListener("shown.bs.modal", () => {
		// 	myInput.focus();
		// });
		function toggleIconAndContent() {
			// Selecting elements for the guest and room dropdowns
			let gicon = document.querySelector(".guest-drop .arrow i");
			let gcontent = document.querySelector(".guest-drop-content");
			let icon = document.querySelector(".room-drop .arrow i");
			let content = document.querySelector(".room-drop-content");

			// Logic for toggling dropdown menus and icons
			if (gicon.classList.contains("fa-angle-down")) {
				// If guest dropdown arrow is facing down, switch to up and show guest content, hide room content
				gicon.classList.remove("fa-angle-down");
				gicon.classList.add("fa-angle-up");
				icon.classList.add("fa-angle-down");
				icon.classList.remove("fa-angle-up");
				gcontent.classList.remove("inactive");
				gcontent.classList.add("active");
				content.classList.remove("active");
				content.classList.add("inactive");
			} else if (
				gicon.classList.contains("fa-angle-up") &&
				icon.classList.contains("fa-angle-down")
			) {
				// If both dropdown arrows are in opposite directions, hide guest content, and keep room content hidden
				gicon.classList.remove("fa-angle-up");
				gicon.classList.add("fa-angle-down");
				icon.classList.remove("fa-angle-up");
				icon.classList.add("fa-angle-down");
				gcontent.classList.remove("active");
				gcontent.classList.add("inactive");
				content.classList.add("inactive");
			} else {
				// If room dropdown arrow is facing up, switch to down and show room content, hide guest content
				gicon.classList.remove("fa-angle-up");
				gicon.classList.add("fa-angle-down");
				icon.classList.remove("fa-angle-down");
				icon.classList.add("fa-angle-up");
				gcontent.classList.remove("active");
				gcontent.classList.add("inactive");
				content.classList.remove("inactive");
				content.classList.add("active");
			}
		}
		/**
		 * Initializes the date inputs with current and next day's dates.
		 * Selects room options and updates the room name accordingly.
		 */

		document.addEventListener("DOMContentLoaded", function () {
			// Get the current date and set it to dateNow input
			const dateNow = document.getElementById("date-now");
			const dateTo = document.getElementById("date-to");
			const now = new Date();
			dateNow.value = now.toISOString().split("T")[0];

			// Calculate and set tomorrow's date to dateTo input
			const tomorrow = new Date(now.getTime() + 24 * 60 * 60 * 1000);
			dateTo.value = tomorrow.toISOString().split("T")[0];

			// Select all room suite elements
			const suiteElements = document.querySelectorAll(".suite");
			const roomName = document.querySelector(".room-name");

			suiteElements.forEach(function (suiteElement) {
				suiteElement.addEventListener("click", function () {
					const firstPElement = suiteElement.querySelector("p");

					// Get the text content of the first p element
					const suiteText = firstPElement.textContent.trim();

					roomName.textContent = suiteText;
					console.log(suiteText);
					roomChoices();
				});
			});
		});

		/**
		 * Toggles the visibility of room and guest dropdown contents.
		 * Manages the arrow icons based on dropdown visibility.
		 */
		function roomChoices() {
			let gicon = document.querySelector(".guest-drop .arrow i");
			let gcontent = document.querySelector(".guest-drop-content");
			let icon = document.querySelector(".room-drop .arrow i");
			let content = document.querySelector(".room-drop-content");

			if (icon.classList.contains("fa-angle-down")) {
				// If room dropdown is open, close it and open guest dropdown
				icon.classList.remove("fa-angle-down");
				icon.classList.add("fa-angle-up");
				gicon.classList.add("fa-angle-down");
				gicon.classList.remove("fa-angle-up");
				content.classList.remove("inactive");
				content.classList.add("active");
				gcontent.classList.remove("active");
				gcontent.classList.add("inactive");
			} else if (
				icon.classList.contains("fa-angle-up") &&
				gicon.classList.contains("fa-angle-down")
			) {
				// If room dropdown is open and guest dropdown is closed, close both
				icon.classList.remove("fa-angle-up");
				icon.classList.add("fa-angle-down");
				gicon.classList.remove("fa-angle-up");
				gicon.classList.add("fa-angle-down");
				content.classList.remove("active");
				content.classList.add("inactive");
				gcontent.classList.add("inactive");
			} else {
				// If room dropdown is closed, close guest dropdown and open room dropdown
				icon.classList.remove("fa-angle-up");
				icon.classList.add("fa-angle-down");
				gicon.classList.remove("fa-angle-down");
				gicon.classList.add("fa-angle-up");
				content.classList.remove("active");
				content.classList.add("inactive");
				gcontent.classList.remove("inactive");
				gcontent.classList.add("active");
			}
		}
		document.addEventListener("DOMContentLoaded", function () {
			// Room
			// var roomMinus = document.querySelector(".room-minus");
			// var roomPlus = document.querySelector(".room-plus");
			// var roomNo = document.querySelector(".room-no");
			// var roomDisplay = document.querySelector(".room");
			// var maxRoom = 5;

			// roomMinus.addEventListener("click", function () {
			// 	var currentRoomNo = parseInt(roomNo.textContent);
			// 	if (currentRoomNo > 1) {
			// 		roomNo.textContent = currentRoomNo - 1;
			// 		roomDisplay.textContent = roomNo.textContent;
			// 	}
			// });

			// roomPlus.addEventListener("click", function () {
			// 	var currentRoomNo = parseInt(roomNo.textContent);
			// 	if (currentRoomNo < maxRoom) {
			// 		roomNo.textContent = currentRoomNo + 1;
			// 		roomDisplay.textContent = roomNo.textContent;
			// 	}
			// });

			// Adult
			var adultMinus = document.querySelector(".adult-minus");
			var adultPlus = document.querySelector(".adult-plus");
			var adultNo = document.querySelector(".adult-no");
			var adultDisplay = document.querySelector(".adult");
			var maxAdult = 4;

			adultMinus.addEventListener("click", function () {
				var currentAdultNo = parseInt(adultNo.textContent);
				if (currentAdultNo > 1) {
					adultNo.textContent = currentAdultNo - 1;
					adultDisplay.textContent = adultNo.textContent;
				}
			});

			adultPlus.addEventListener("click", function () {
				var currentAdultNo = parseInt(adultNo.textContent);
				if (currentAdultNo < maxAdult) {
					adultNo.textContent = currentAdultNo + 1;
					adultDisplay.textContent = adultNo.textContent;
				}
			});

			// Child
			var childMinus = document.querySelector(".child-minus");
			var childPlus = document.querySelector(".child-plus");
			var childNo = document.querySelector(".child-no");
			var childDisplay = document.querySelector(".child");
			var maxChild = 3;

			childMinus.addEventListener("click", function () {
				var currentChildNo = parseInt(childNo.textContent);
				if (currentChildNo > 0) {
					childNo.textContent = currentChildNo - 1;
					childDisplay.textContent = childNo.textContent;
				}
			});

			childPlus.addEventListener("click", function () {
				var currentChildNo = parseInt(childNo.textContent);
				if (currentChildNo < maxChild) {
					childNo.textContent = currentChildNo + 1;
					childDisplay.textContent = childNo.textContent;
				}
			});
		});

		document.addEventListener("DOMContentLoaded", function () {
			let guestDrop = document.querySelector(".guest-drop");
			guestDrop.addEventListener("click", toggleIconAndContent);
		});
		document.addEventListener("DOMContentLoaded", function () {
			let roomDrop = document.querySelector(".room-drop");
			roomDrop.addEventListener("click", roomChoices);
		});

		const suite_option = document.querySelectorAll(".the-option");
		const slider = document.querySelector(".slider");

		suite_option.forEach((link) => {
			link.addEventListener("click", function () {
				// Remove the "active" class from all links
				suite_option.forEach((link) => link.classList.remove("active"));
				// Add the "active" class to the clicked link
				this.classList.add("active");
				// Add the animate class to trigger the animation
				slider.classList.add("animate");
				// Remove the animate class after the animation completes
				setTimeout(() => {
					slider.classList.remove("animate");
				}, 500);
			});
		});

		$(".next").on("click", function () {
			// Remove active class from all options
			$(".the-option").removeClass("active");
			// Add active class to the option corresponding to the next slide
			let nextSlideId = $(this).attr("href");
			$(".the-option[href='" + nextSlideId + "']").addClass("active");

			// Add the animate class to trigger the animation
			slider.classList.add("animate");
			// Remove the animate class after the animation completes
			setTimeout(() => {
				slider.classList.remove("animate");
			}, 500);
		});

		$(".prev").on("click", function () {
			// Remove active class from all options
			$(".the-option").removeClass("active");
			// Add active class to the option corresponding to the previous slide
			let prevSlideId = $(this).attr("href");
			$(".the-option[href='" + prevSlideId + "']").addClass("active");

			// Add the animate class to trigger the animation
			slider.classList.add("animate");
			// Remove the animate class after the animation completes
			setTimeout(() => {
				slider.classList.remove("animate");
			}, 500);
		});
	},
};
</script>

<style scoped>
.first-row {
	height: 100vh;
	background: var(--text-color-c);
	display: flex;
	flex-direction: column;
}

.second-row {
	height: 100vh;
	background: var(--text-color-b);
	display: flex;
	justify-content: end;
}

.third-row {
	height: 100vh;
	background: var(--text-color-c);
	display: flex;
	justify-content: end;
}

/*--------------- FIRST SECTION --------------- */

@keyframes TMNT {
	0% {
		left: 0px;
	}

	100% {
		left: -1200px;
	}
}

a.prev,
a.next {
	height: 91px;
	position: absolute;
	width: 43px;
	top: 50%;
	margin-top: -30px;
	opacity: 0.6;
	text-indent: -99999px;
	cursor: pointer;
	transition: opacity 0.5s ease-out;
}

a.prev:hover,
a.next:hover {
	opacity: 1;
}

.prev {
	left: 0;
	background: url("https://lh4.googleusercontent.com/-JN1IZLtuToI/UUoZnMG3C_I/AAAAAAAAAE8/SEbJ9nqXGnY/s226/sprite.png")
		no-repeat -200px 25px;
}

.next {
	right: 0;
	background: url("https://lh4.googleusercontent.com/-JN1IZLtuToI/UUoZnMG3C_I/AAAAAAAAAE8/SEbJ9nqXGnY/s226/sprite.png")
		no-repeat -167px 25px;
}

@keyframes fadein {
	0% {
		opacity: 0;
	}

	100% {
		opacity: 1;
	}
}

.slider {
	height: 75vh;
	width: 95%;
	position: relative;
	overflow: hidden;
	margin-left: 65px;
}

.animate {
	animation: fadein 0.3s ease-in;
}

.slide {
	position: absolute;
	height: 100%;
	width: 100%;
	background-color: #57716c;
	justify-content: center;
}

.slider .slide:target {
	z-index: 1;
}

img {
	position: absolute;
	height: 75vh;
	width: 100%;
	right: 0;
	top: 0;
	filter: brightness(35%);
}

.overlay-content {
	position: absolute;
	bottom: 0;
	left: 50%;
	transform: translate(-50%, -20%);
	color: #fff;
	/* Text color */
	height: 40%;
	width: 90%;
}

.overlay-content h2 {
	margin-bottom: 10px;
	font-family: "Playfair Display", serif;
	font-weight: 400;
	font-style: normal;
	font-optical-sizing: auto;
	font-size: 90px;
}

.overlay-content .descript {
	width: 50%;
	text-align: justify;
}

.descript p {
	font-size: 24px;
	font-family: "Abel", sans-serif;
	font-weight: 400;
	font-style: normal;
}

.select {
	bottom: 0;
	display: flex;
	height: 25%;
	width: 100%;
	justify-content: end;
	align-items: center;
}

.choices {
	position: relative;
	height: 100%;
	width: 96%;

	display: flex;
	justify-content: center;
	align-items: center;
}

.choices img {
	position: relative;
	height: 9rem;
	width: 15rem;

	background-size: cover;
	transition: 0.5s;
}

.the-option {
	margin: 2rem;
}

.the-option.active img {
	filter: brightness(100%);
	box-shadow: 0 5px 15px rgba(0, 0, 0, 0.8);
}

.the-option:hover img {
	filter: brightness(100%);
}

/*--------------- SECOND SECTION --------------- */
.outer-container {
	display: flex;
	flex-direction: column;
	width: 95.7%;
	height: 100%;
	align-items: center;
}

.outer-container .book-container {
	background: var(--bg-color-a);
	width: 80%;
	height: 40%;
	margin: 2rem;
	box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);
}

input {
	border: transparent;
	padding: 5px 10px;
	font-family: "Abel", sans-serif;
	font-weight: 400;
	font-style: normal;
	font-size: 20px;
	color: var(--card-color);
	margin: 0;
	background-color: var(--bg-color-a);
}

input:focus {
	outline: none;
}

/* BB */
.guest-drop {
	cursor: pointer;
	display: flex;
	width: 15rem;
	user-select: none;
	padding-left: 0.5rem;
}

.arrow {
	display: flex;
	justify-content: end;
	margin-right: 0.5rem;
	width: 40px;
	height: 25px;
}

.guest-drop-content.inactive {
	position: absolute;

	opacity: 0;
	background: var(--card-color);
	width: 15rem;
	height: 10rem;
	top: 120%;
	z-index: 5;
	transition: 0.5s all;
}

.guest-drop-content.active {
	position: absolute;
	display: block;
	opacity: 1;
	background: var(--card-color);
	width: 15rem;
	height: 11.5rem;
	top: 123%;
	z-index: 5;
	border-radius: 5px;
	box-shadow: 0 0 20px rgba(0, 0, 0, 0.8);
	transition: 0.5s all;
}

.guest-drop-content .drop-container {
	display: flex;
	justify-content: center;
	align-items: center;
	width: 15rem;
	margin-top: 0.2rem;
	color: var(--text-color-b);
}

.minus {
	background: var(--text-color-a);
	width: 2.5rem;
	height: 2.5rem;
	display: flex;
	justify-content: center;
	align-items: center;
	margin: 0.5rem;
	margin-right: 2rem;
	cursor: pointer;
	font-size: 30px;
	font-weight: bold;
	user-select: none;
	border-radius: 5px;
	transition: 0.5s;
}

.minus:hover {
	background: #756048;
}

.plus {
	background: var(--text-color-a);
	width: 2.5rem;
	height: 2.5rem;
	display: flex;
	justify-content: center;
	align-items: center;
	margin: 0.5rem;
	cursor: pointer;
	font-size: 25px;
	font-weight: bold;
	user-select: none;
	border-radius: 5px;
	transition: 0.5s;
}

.plus:hover {
	background: #756048;
}

.text {
	width: 5rem;
	user-select: none;
}

.room-drop {
	cursor: pointer;
	display: flex;
	justify-content: space-between;
	width: 15rem;
	padding-left: 0.5rem;
	user-select: none;
}

.room-drop-content.inactive {
	position: absolute;
	user-select: none;
	opacity: 0;
	background: var(--card-color);
	width: 15rem;
	height: 11.5rem;
	top: 120%;
	z-index: 5;
	transition: 0.5s all;
}

.room-drop-content.active {
	position: absolute;
	user-select: none;
	display: flex;
	flex-direction: column;
	justify-content: center;
	opacity: 1;
	background: var(--card-color);
	width: 20rem;
	height: 11.5rem;
	top: 123%;
	z-index: 5;
	border-radius: 5px;
	box-shadow: 0 0 20px rgba(0, 0, 0, 0.8);
	transition: 0.5s all;
}

.room-drop-content span {
	border: 0.1px solid #e7d0b2;
	margin: 0 0.5rem;
}

.room-drop-content.inactive span {
	border: none;
}

.room-drop-content.inactive p {
	position: relative;
	display: none;
}

.room-drop-content div {
	position: relative;
	margin: 0.4rem;
	padding-top: 0.7rem;
	padding-left: 1rem;
	height: 45px;
	cursor: pointer;
	color: var(--text-color-b);
	text-align: left;
	font-size: 20px;
	font-family: "Abel", sans-serif;
	font-style: normal;
	border-radius: 5px;
	transition: 0.5s;
}

.room-drop-content div:hover {
	background: var(--text-color-a);
}

/* BB */

.book-container .book-header {
	font-family: "Playfair Display", serif;
	font-weight: 400;
	font-style: normal;
	font-optical-sizing: auto;
	font-size: 40px;
	height: 20%;
	color: var(--text-color-b);
	background: var(--card-color);
	text-align: center;
	align-items: center;
}

.inner-book {
	font-family: "Abel", sans-serif;
	font-weight: 400;
	font-style: normal;
	color: var(--card-color);
	height: 30%;
	display: flex;
	justify-content: start;
	align-items: center;
	padding: 2rem;
}

.inner-book .date-col {
	display: flex;
	flex-direction: column;
	align-items: start;
	margin-right: 1.5rem;
	justify-content: center;
}

.inner-book .room-col {
	padding-left: 1rem;
	width: 260px;
	display: flex;
	border-left: 2px solid var(--card-color);
	flex-direction: column;
	align-items: start;
	justify-content: center;
}

.inner-book .guest-col {
	padding-left: 1rem;
	width: 260px;
	display: flex;
	border-left: 2px solid var(--card-color);
	flex-direction: column;
	align-items: start;
	justify-content: center;
}

.date-select {
	display: flex;
	font-size: 15px;
}
.date-mod {
	background: transparent;
}

.inner-book .book-btn {
	user-select: none;
	margin-left: 3rem;
	background-color: var(--card-color);
	width: 15%;
	height: 50px;
	font-size: 20px;
	font-family: "Abel", sans-serif;
	font-weight: 400;
	font-style: normal;
	color: var(--text-color-b);
	display: flex;
	justify-content: center;
	align-items: center;
	cursor: pointer;
	transition: 0.5s;
}

.book-btn:hover {
	position: relative;
	width: 15%;
	height: 52px;
	background-color: var(--text-color-a);
	box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);
	color: var(--text-color-b);
}

.benefit-divider {
	position: absolute;
	margin-bottom: 7.5rem;
	font-size: 24px;
	font-family: "Abel", sans-serif;
	font-weight: 400;
	font-style: normal;
	color: var(bg);
	background-color: var(--bg-color-a);
	width: 15rem;
	text-align: center;
}

.benefits {
	user-select: none;
	border-top: 1.5px solid var(--card-color);
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
	width: 80px;
	height: 65px;
	text-align: center;
	color: var(--bg-color-a);
	display: flex;
	justify-content: center;
	align-items: center;
	font-size: 30px;
}

.benefits-con {
	display: flex;
	justify-content: center;
	align-items: center;
}

.benifit-card {
	display: flex;
	justify-content: center;
	align-items: center;
}

.benifit-card p {
	margin-left: 1rem;
	font-size: 20px;
	font-family: "Abel", sans-serif;
	font-weight: 400;
	font-style: normal;
	color: var(--card-color);
}

.room-suites {
	margin: 0 9rem;
	color: var(--card-color);
}

.room-suites .room-header {
	text-align: center;
	font-family: "Playfair Display", serif;
	font-weight: 400;
	font-style: normal;
	font-optical-sizing: auto;
	font-size: 50px;
	padding-bottom: 2rem;
}

.room-suites p {
	justify-content: center;
	text-align: justify;
	font-size: 20px;
	font-family: "Abel", sans-serif;
	font-weight: 400;
	font-style: normal;
}

/*======================================== Card Book Section ========================================*/

.book-cards {
	max-width: 95%;
	display: flex;
	align-items: center;
	justify-content: center;
}

.book-cards .book-card {
	margin: 2rem;
	width: 25%;
	height: 75%;
	text-align: center;
	color: var(--text-color-a);
	background-color: var(--text-color-b);
}

.book-card img {
	position: inherit;
	width: 100%;
	height: 50%;
	filter: brightness(100%);
}

.book-card h1 {
	font-family: "Playfair Display", serif;
	font-weight: 400;
	font-style: normal;
	font-optical-sizing: auto;
	font-size: 30px;
	padding-top: 0.5rem;
	padding-bottom: 0.5rem;
}

.book-card p {
	font-size: 18px;
	font-family: "Abel", sans-serif;
	font-weight: 400;
	font-style: normal;
	text-align: center;
	padding-left: 2rem;
	padding-right: 2rem;
	height: 25%;
}

.btn-box {
	padding-top: 2rem;
}

.btn-box:hover a {
	width: 234px;
	height: 40px;
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
	height: 35px;
	background: var(--bg-color-c);
	font-size: 24px;
	font-family: "Abel", sans-serif;
	font-weight: 400;
	font-style: normal;
	color: rgb(255, 255, 255);
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

.roombook-main-title-container {
	margin-top: 4rem;
	margin-bottom: 1rem;
	margin-left: 3rem;
	width: 100%;
	height: 10rem;
}

.roombook-main-title {
	display: flex;
	flex-direction: row;

	color: #472f24;
	font-family: "Playfair Display", serif;
	font-size: 128px;
	font-weight: 400;
	line-height: 73px;
	letter-spacing: -0.04em;
	text-align: center;
}
.roombook-main-title:before,
.roombook-main-title:after {
	content: "";
	flex: 1 1;
	border-bottom: 1px solid;
	margin: 1.5rem;
}
.roombook-main-title:before {
	margin-right: -12px;
}
.roombook-main-title:after {
	margin-left: -2px;
}

/* ======================================== Box 1  ========================================*/
.room-booking-container {
	margin-left: 6rem;
	margin-right: 2rem;
	margin-bottom: 1rem;
	padding-top: 1rem;
	background-color: #f4f1ed;
	display: flex;
	height: auto;
}

.box-1 {
	background-color: #4b4238;
	width: 80%;
}

.roombook-title {
	background-color: #472f24;
	display: flex;
	justify-content: center;
	color: white;
	font-family: "Playfair Display", serif;
	font-size: 40px;
	font-weight: 400;
	line-height: 73px;
	letter-spacing: -0.04em;
}

.box-suite-info {
	margin: 2rem;
	padding: 2rem;
	border: 4px solid #e7d0b2;
}

.box-container {
	margin-top: 1rem;
	display: flex;
}

.box-suite-info h2 {
	color: #e7d0b2;
	font-family: "Playfair Display", serif;
	font-size: 55px;
	font-weight: 400;
	line-height: 73px;
	letter-spacing: -0.04em;
	text-align: left;
}

.box-container2 {
	margin-top: -1rem;
}

.room-features {
	margin-top: 2rem;
}

.box-suite-info p {
	margin-top: -1rem;
	color: #e7d0b2;
	font-family: "Abel", sans-serif;
	font-size: 28px;
	font-weight: 400;
	line-height: 45.88px;
	letter-spacing: -0.04em;
	text-align: left;
}

.room-list {
	color: #e7d0b2;
	font-family: "Abel", sans-serif;
	font-size: 25px;
	font-weight: 400;
	line-height: 41px;
	letter-spacing: -0.04em;
	text-align: left;
	list-style-type: disc;
	padding-left: 3rem;
	margin-top: 1rem;
	margin-bottom: 1rem;
}

/* ======================================== Box 2  ========================================*/
.box-2 {
	padding: 2rem;
	background-color: #e7d0b2;
}
.form-summary {
	display: flex;
	justify-content: space-between;
	margin-top: 2rem;
}
.modal-content {
	width: 100rem;
}
.modal-dialog {
	display: flex;
	justify-content: center;
}

.booking-summary-title {
	justify-content: center;
	color: #4b4238;
	font-family: "Playfair Display", serif;
	font-size: 55px;
	font-weight: 400;
	line-height: 73px;
	letter-spacing: -0.04em;
	text-align: left;
}

.summary-subtitle {
	margin-top: 2rem;
	color: #4b4238;
	font-family: "Abel", sans-serif;
	font-size: 23px;
	font-weight: 400;
	line-height: 20.39px;
	letter-spacing: -0.04em;
	text-align: left;
}

.summary-info {
	margin-top: 8px;
	color: #4b4238;
	font-family: "Abel", sans-serif;
	font-size: 32px;
	font-weight: 400;
	line-height: 40.78px;
	letter-spacing: -0.04em;
	text-align: left;
}

.summary-border {
	margin-top: 2rem;

	display: flex;
	justify-content: center;
	width: 100%;
	border: 2px solid #4b4238;
}

.box-2-prices-container {
	display: flex;
	justify-content: space-around;
	align-self: end;
	margin-top: 11.5rem;
}
.box-2-prices-container1 {
	display: flex;
	justify-content: space-between;
}

.menu-button-div {
	margin-top: 2rem;
	display: flex;
	height: 10vh;
	justify-content: center;
}

.menu-btn {
	padding-top: 1rem;
	padding-bottom: 3rem;
	padding-left: 3rem;
	padding-right: 3rem;
	text-align: center;
	width: 390px;
	height: 25px;
	font-family: "Abel", sans-serif;
	font-size: 20px;
	font-weight: 200;
	line-height: 31px;
	letter-spacing: 0.18em;
	color: #ffffff;
	background-color: #68502b;
	text-decoration: none;
}

.menu-btn:hover {
	transition: 0.5s;
	color: #68502b;
	background-color: #fdeedf;
	box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);
}

.btn-cancel {
	margin-left: 1rem;
	padding-top: 1rem;
	padding-bottom: 3rem;
	padding-left: 3rem;
	padding-right: 3rem;
	text-align: center;
	width: 390px;
	height: 25px;
	font-family: "Abel", sans-serif;
	font-size: 20px;
	font-weight: 200;
	line-height: 31px;
	letter-spacing: 0.18em;
	color: #68502b;
	background-color: white;
	text-decoration: none;
}

.btn-cancel:hover {
	transition: 0.5s;
	color: #68502b;
	background-color: #e2d3c5;
	box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);
}
</style>

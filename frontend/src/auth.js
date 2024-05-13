import { ref, watchEffect } from "vue";
import axios from "axios";

const currentUser = ref(null);
const email = ref("");
const first_name = ref("");
const last_name = ref("");
const location = ref("");
const username = ref("");
const password = ref("");

watchEffect(() => {
	axios
		.get("http://127.0.0.1:8000/api/user")
		.then((res) => {
			currentUser.value = true;
		})
		.catch((error) => {
			currentUser.value = false;
		});
});

const submitRegistration = () => {
	// Your registration logic here
};

const submitLogin = () => {
	// Your login logic here
};

const submitLogout = () => {
	// Your logout logic here
};

export {
	currentUser,
	email,
	first_name,
	last_name,
	location,
	username,
	password,
	submitRegistration,
	submitLogin,
	submitLogout,
};

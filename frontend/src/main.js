import { createApp } from "vue";
import App from "./App.vue";
import Events from "./components/Events.vue";
import router from "./routes";
// import router_events from "./routes_events";
import axios from "axios";
// Create a Vue app instance
const app = createApp(App);
// const events = createApp(Events);
// Use Vue Router
axios.defaults.baseURL = "http://127.0.0.1:8000";
app.use(router, axios);
// events.use(router_events);

// Mount the Vue app to the specified element in the DOM
app.mount("#app");

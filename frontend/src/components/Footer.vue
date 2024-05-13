<!-- Footer section containing contact information and social media icons -->
<template>
    <main id="contacts">
        <div class="footer-wrapper">
            <!-- Footer column 1: Contact information -->
            <div class="footer1">
                <div class="footer-title">
                    Sonya's Secret <br />
                    Garden
                </div>
                <div class="footer-text">
                    Please let us know how we <br />
                    can make your stay more <br />
                    delightful.
                </div>
                <div class="footer-contact">
                    Barangay Buck Estate, Alfonso, Cavite, PH <br />
                    (near the vicinity of Tagaytay City) <br />
                    info@sonyasgarden.com
                </div>
            </div>
            <!-- Divider between footer columns -->
            <div class="divider"></div>
            <!-- Footer column 2: Social media icons -->
            <div class="footer2">
                <i class="fa-brands fa-facebook"></i>
                <i class="fa-solid fa-envelope"></i>
                <i class="fa-brands fa-twitter"></i>
            </div>
            <!-- Copyright notice -->
            <p class="footer-copyright">
                Copyright © 2024 Sonya’s Secret Garden. All Rights
                Reserved. Gabrentina || Galan || Gozum || Nitro || Tecson
            </p>
        </div>
    </main>
</template>

<script setup>
</script>

<style scoped>
.contacts {
	margin-right: 1100rem;
}
/*=========== Home Footer Section ==============*/
.footer-wrapper {
    padding-top: 4rem;
    background-color: #4B4238;
    padding-bottom: 5rem;
}

.footer1 {
    display: flex;
    justify-content: space-evenly;
}

.footer-title {
    color: #E7D0B2;
    text-align: left;
    font-family: "Playfair Display", serif;
    font-size: 60px;
    font-weight: 400;
    line-height: 73px;
    letter-spacing: -0.04em;
    text-align: center;
}

.footer-text {
    color: #E7D0B2;
    text-align: center;
    font-family: "Abel", sans-serif;
    font-size: 32px;
    font-weight: 400;
    line-height: 50px;
    letter-spacing: -0.04em;
    text-align: center;
}

.footer-contact {
    color: #E7D0B2;
    text-align: right;
    font-family: "Abel", sans-serif;
    font-size: 24px;
    font-weight: 400;
    line-height: 50px;
    letter-spacing: -0.04em;
    text-align: right;
}

.divider {
    border-bottom: 2.7px;
    border-bottom-style: solid;
    text-align: center;
    margin: 2rem 8rem;
    color: #E7D0B2;
}

.footer2 {
    display: flex;
    justify-content: space-evenly;
    background-color: #4B4238;
    margin: 1rem 29rem;
}

.footer2 i {
    color: #E7D0B2;
    font-size: 6rem;
}

.footer-copyright {
    margin-top: 2rem;
    font-family: "Abel", sans-serif;
    font-size: 20px;
    font-weight: 400;
    line-height: 50px;
    letter-spacing: -0.04em;
    text-align: center;
    color: #E7D0B2;
}
</style>
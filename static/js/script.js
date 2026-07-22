// ======================================
// Typing Animation
// ======================================

const roles = [
    "Python Developer",
    "AI Engineer",
    "Machine Learning Enthusiast",
    "Backend Developer"
];

let currentRole = 0;

const typingText = document.getElementById("typing-text");

if (typingText) {

    setInterval(() => {

        currentRole++;

        if (currentRole >= roles.length) {
            currentRole = 0;
        }

        typingText.textContent = roles[currentRole];

    }, 2000);

}


// ======================================
// Reveal Sections
// ======================================

const reveals = document.querySelectorAll(".reveal");

function revealSections() {

    reveals.forEach(section => {

        const sectionTop = section.getBoundingClientRect().top;

        if (sectionTop < window.innerHeight - 120) {

            section.classList.add("active");

        } else {

            section.classList.remove("active");

        }

    });

}

window.addEventListener("scroll", revealSections);
window.addEventListener("load", revealSections);


// ======================================
// Skill Bar Animation
// ======================================

const skillSection = document.querySelector(".skills");

if (skillSection) {

    const skillObserver = new IntersectionObserver((entries) => {

        if (entries[0].isIntersecting) {

            document.querySelectorAll(".progress-bar").forEach(bar => {

                const level = bar.dataset.level;

                if (level) {

                    bar.style.width = level + "%";

                }

            });

            skillObserver.unobserve(skillSection);

        }

    }, {

        threshold: 0.4

    });

    skillObserver.observe(skillSection);

}


// ======================================
// Flash Message
// ======================================

const flash = document.querySelector(".flash-message");

if (flash) {

    setTimeout(() => {

        flash.style.opacity = "0";

        setTimeout(() => {

            flash.style.display = "none";

        }, 500);

    }, 6000);

}


// ======================================
// Navbar
// ======================================

const nav = document.querySelector("nav");

if (nav) {

    let lastScroll = 0;

    window.addEventListener("scroll", () => {

        const currentScroll = window.pageYOffset;

        // Dark navbar after scrolling

        if (currentScroll > 40) {

            nav.classList.add("scrolled");

        } else {

            nav.classList.remove("scrolled");

        }

        // Hide while scrolling down

        if (currentScroll > lastScroll && currentScroll > 100) {

            nav.style.transform = "translateY(-100%)";

        }

        // Show while scrolling up

        else {

            nav.style.transform = "translateY(0)";

        }

        lastScroll = currentScroll;

    });

}


// ======================================
// GitHub Stats
// ======================================

async function loadGithubStats() {

    const repo = document.getElementById("repo-count");

    const followers = document.getElementById("followers");

    const following = document.getElementById("following");

    const github = document.getElementById("github-link");

    if (!repo || !followers || !following || !github) return;

    try {

        const response = await fetch("/api/github/stats");

        const data = await response.json();

        repo.textContent = data.repositories;

        followers.textContent = data.followers;

        following.textContent = data.following;

        github.href = data.profile;

    }

    catch (error) {

        console.log(error);

    }

}


// ======================================
// Horizontal Project Slider
// ======================================

const slider = document.querySelector(".projects-container");

function slideLeft() {

    if (!slider) return;

    slider.scrollBy({

        left: -380,

        behavior: "smooth"

    });

}

function slideRight() {

    if (!slider) return;

    slider.scrollBy({

        left: 380,

        behavior: "smooth"

    });

}


// ======================================
// Initialize
// ======================================

window.addEventListener("load", () => {

    revealSections();

    loadGithubStats();

});
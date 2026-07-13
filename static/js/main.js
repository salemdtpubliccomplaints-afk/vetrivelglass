const toggle = document.querySelector(".menu-toggle");
const nav = document.querySelector(".main-nav");

if (toggle && nav) {
    toggle.addEventListener("click", () => {
        const open = nav.classList.toggle("open");
        toggle.setAttribute("aria-expanded", open ? "true" : "false");
    });

    nav.querySelectorAll("a").forEach((link) => {
        link.addEventListener("click", () => {
            nav.classList.remove("open");
            toggle.setAttribute("aria-expanded", "false");
        });
    });
}

const revealItems = document.querySelectorAll(".reveal");
if ("IntersectionObserver" in window) {
    const observer = new IntersectionObserver((entries, obs) => {
        entries.forEach((entry) => {
            if (entry.isIntersecting) {
                entry.target.classList.add("visible");
                obs.unobserve(entry.target);
            }
        });
    }, { threshold: 0.12 });

    revealItems.forEach((item) => observer.observe(item));
} else {
    revealItems.forEach((item) => item.classList.add("visible"));
}

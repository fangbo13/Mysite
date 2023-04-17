document.addEventListener("DOMContentLoaded", function () {
    const skillRatings = document.querySelectorAll(".skill-rating");
    skillRatings.forEach((rating) => {
        const level = rating.getAttribute("data-level");
        rating.style.setProperty("--level", `${level}%`);
    });
});


 // ----------------------获取skillbar的值修改并传入css中----------------------
document.addEventListener("DOMContentLoaded", function () {
    const skillBars = document.querySelectorAll(".skill-bar");
    skillBars.forEach((bar) => {
        const level = bar.getAttribute("data-level");
        bar.style.width = `${level}%`;
    });
});
 // ----------------------获取skillbar的值修改并传入css中----------------------
document.addEventListener("DOMContentLoaded", function () {
    const skillBars = document.querySelectorAll(".skill-bar");
    skillBars.forEach((bar) => {
        const level = bar.getAttribute("data-level");
        bar.style.width = `${level}%`;
    });
});


 // ----------------------view detail----------------------
document.addEventListener('DOMContentLoaded', function () {
    // 获取模态框及相关元素
    const modal = document.getElementById('modal');
    const modalTitle = document.getElementById('project-title');
    const modalDescription = document.getElementById('project-description');
    const modalDate = document.getElementById('project-date');
    const modalImage = document.getElementById('project-image');
    const closeButton = document.querySelector('.close');

    // 为每个“查看详情”按钮添加点击事件监听器
    const ctaButtons = document.querySelectorAll('.cta-button');
    ctaButtons.forEach(function (button) {
        button.addEventListener('click', function () {
            const cardInfo = button.parentElement;
            modalTitle.innerText = cardInfo.querySelector('h3').innerText;
            modalDescription.innerText = cardInfo.querySelector('p').innerText;
            modalDate.innerText = cardInfo.querySelector('.date').innerText;
            modalImage.src = cardInfo.previousElementSibling.src;
            modal.style.display = 'block';
        });
    });

    // 当用户点击关闭按钮时，关闭模态框
    closeButton.onclick = function () {
        modal.style.display = 'none';
    };

    // 当用户点击模态框外部时，关闭模态框
    window.onclick = function (event) {
        if (event.target == modal) {
            modal.style.display = 'none';
        }
    };
});


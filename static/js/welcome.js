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
    const modalCustomDescription = document.getElementById('custom-description');
    const modalDate = document.getElementById('project-date');
    const modalImage = document.getElementById('project-image');
    const closeButton = document.querySelector('.close');
    const projectLink = document.getElementById('project-link');
    

    // 为每个“查看详情”按钮添加点击事件监听器
    const ctaButtons = document.querySelectorAll('.cta-button');
    ctaButtons.forEach(function (button) {
        button.addEventListener('click', function () {
            const cardInfo = button.parentElement;
            modalTitle.innerText = cardInfo.querySelector('h3').innerText;
            modalCustomDescription.innerText = button.getAttribute('data-custom-description'); 
            modalImage.src = cardInfo.previousElementSibling.src;
            projectLink.href = button.getAttribute("data-project-url");
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


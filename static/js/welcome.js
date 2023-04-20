 // ----------------------获取skillbar的值修改并传入css中----------------------
document.addEventListener("DOMContentLoaded", function () {
    const skillBars = document.querySelectorAll(".skill-bar");
    skillBars.forEach((bar) => {
        const level = bar.getAttribute("data-level");
        bar.style.width = `${level}%`;
    });
});


 // ----------------------works缩略图展开----------------------

 // 获取所有作品项和筛选按钮
const workItems = document.querySelectorAll('.work-item');
const filterButtons = document.querySelectorAll('.filter-btn');

// 为筛选按钮添加点击事件
filterButtons.forEach(button => {
  button.addEventListener('click', () => {
    const filterValue = button.getAttribute('data-filter');

    workItems.forEach(item => {
      if (filterValue === '*' || item.classList.contains(filterValue.slice(1))) {
        item.style.display = 'flex';
      } else {
        item.style.display = 'none';
      }
    });
  });
});

// 为作品项添加点击事件，打开模态框
workItems.forEach(item => {
  item.addEventListener('click', () => {
    const modal = new bootstrap.Modal(document.getElementById('workModal'));
    modal.show();
  });
});

// Sidebar Toggle
const sidebar = document.querySelector(".sidebar");
const mainContent = document.querySelector(".main-content");
document.getElementById("toggleSidebar").addEventListener("click", () => {
    sidebar.classList.toggle("sidebar-hidden");
    if (window.innerWidth > 768) {
        if (sidebar.classList.contains("sidebar-hidden")) {
            mainContent.style.marginLeft = "0";
        } else {
            mainContent.style.marginLeft = "16rem";
        }
    }
});

// Lấy pathname hiện tại (VD: /nutrition.html)
const currentPath = window.location.pathname;

// Lấy tất cả các liên kết trong sidebar
const sidebarLinks = document.querySelectorAll('.sidebar a');

sidebarLinks.forEach(link => {
    // Nếu đường dẫn của link trùng với đường dẫn hiện tại
    if (link.getAttribute('href') === currentPath) {
        link.classList.add('bg-blue-100', 'text-blue-600', 'font-semibold');
    }
});





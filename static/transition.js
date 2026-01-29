document.querySelectorAll("a").forEach(link => {
    link.addEventListener("click", function(e) {
        e.preventDefault();
        const href = this.href;

        document.body.style.opacity = "0";
        document.body.style.transform = "translateY(10px)";

        setTimeout(() => {
            window.location.href = href;
        }, 300);
    });
});

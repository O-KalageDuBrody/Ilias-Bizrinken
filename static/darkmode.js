document.addEventListener("DOMContentLoaded", () => {
    const toggle = document.getElementById("darkModeToggle");

    if (!toggle) return; // sécurité si le bouton n'existe pas sur une page

    // Charger l'état sauvegardé
    if (localStorage.getItem("darkMode") === "enabled") {
        document.body.classList.add("dark");
        toggle.textContent = "☀️";
    }

    toggle.addEventListener("click", () => {
        document.body.classList.toggle("dark");

        if (document.body.classList.contains("dark")) {
            toggle.textContent = "☀️";
            localStorage.setItem("darkMode", "enabled");
        } else {
            toggle.textContent = "🌙";
            localStorage.setItem("darkMode", "disabled");
        }
    });
});

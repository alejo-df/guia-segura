(function () {
    const root = document.documentElement;
    const toggle = document.getElementById('themeToggle');

    function applyTheme(theme) {
        root.setAttribute('data-theme', theme);
        localStorage.setItem('guiaSeguraTheme', theme);

        if (!toggle) return;
        const icon = toggle.querySelector('i');
        const label = toggle.querySelector('span');

        if (theme === 'dark') {
            if (icon) icon.className = 'fas fa-sun';
            if (label) label.textContent = 'Modo claro';
        } else {
            if (icon) icon.className = 'fas fa-moon';
            if (label) label.textContent = 'Modo nocturno';
        }
    }

    const savedTheme = localStorage.getItem('guiaSeguraTheme') || 'light';
    applyTheme(savedTheme);

    if (toggle) {
        toggle.addEventListener('click', function () {
            const current = root.getAttribute('data-theme') || 'light';
            applyTheme(current === 'dark' ? 'light' : 'dark');
        });
    }
})();

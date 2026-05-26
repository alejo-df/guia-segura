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


// Estados de error y validacion visual de formularios
(function () {
    function defaultMessage(field) {
        if (field.dataset.errorMessage) return field.dataset.errorMessage;
        const label = field.closest('.mb-3, .form-group, .col-md-6, .col-12')?.querySelector('label');
        const name = label ? label.textContent.replace('*', '').trim() : 'Este campo';
        if (field.validity.valueMissing) return `${name} es obligatorio.`;
        if (field.validity.typeMismatch) return `Ingrese un valor válido para ${name.toLowerCase()}.`;
        if (field.validity.tooShort) return `${name} no cumple con la longitud mínima.`;
        if (field.validity.patternMismatch) return `${name} no tiene el formato esperado.`;
        return `Revise el valor ingresado en ${name.toLowerCase()}.`;
    }

    function ensureFeedback(field) {
        const parent = field.closest('.mb-3, .form-group, .col-md-6, .col-12, .col-md-10') || field.parentElement;
        if (!parent) return null;
        let feedback = parent.querySelector('.invalid-feedback.client-feedback');
        if (!feedback) {
            feedback = document.createElement('div');
            feedback.className = 'invalid-feedback client-feedback';
            parent.appendChild(feedback);
        }
        return feedback;
    }

    function updateField(field) {
        if (!field.matches('input, select, textarea')) return;
        if (field.type === 'hidden' || field.type === 'submit' || field.type === 'button') return;
        const feedback = ensureFeedback(field);
        if (!feedback) return;
        if (!field.checkValidity()) {
            field.classList.add('is-invalid');
            field.classList.remove('is-valid');
            feedback.textContent = defaultMessage(field);
        } else if (field.value && field.required) {
            field.classList.remove('is-invalid');
            field.classList.add('is-valid');
            feedback.textContent = '';
        } else {
            field.classList.remove('is-invalid');
            field.classList.remove('is-valid');
            feedback.textContent = '';
        }
    }

    document.querySelectorAll('.field-error').forEach(function (error) {
        const group = error.closest('.mb-3, .form-group, .col-md-6, .col-12');
        const field = group ? group.querySelector('input, select, textarea') : null;
        if (field) field.classList.add('is-invalid');
    });

    document.querySelectorAll('form').forEach(function (form) {
        form.querySelectorAll('input[required], select[required], textarea[required], input[type="email"]').forEach(function (field) {
            field.addEventListener('input', function () { updateField(field); });
            field.addEventListener('change', function () { updateField(field); });
            field.addEventListener('blur', function () { updateField(field); });
        });

        form.addEventListener('submit', function (event) {
            if (!form.checkValidity()) {
                event.preventDefault();
                event.stopPropagation();
                form.classList.add('was-validated');
                form.querySelectorAll('input, select, textarea').forEach(updateField);
                const firstInvalid = form.querySelector('.is-invalid, :invalid');
                if (firstInvalid) firstInvalid.focus({ preventScroll: false });
                return false;
            }
            form.classList.add('was-validated');
        });
    });
})();

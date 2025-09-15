document.querySelectorAll('.accordion-header').forEach(header => {
    header.addEventListener('click', () => {
        header.classList.toggle('active');
        const target = document.querySelector(header.getAttribute('data-bs-target'));
        if (target) {
            target.classList.contains('show') ?
                header.setAttribute('aria-expanded', 'true') :
                header.setAttribute('aria-expanded', 'false');
        }
    });
});
/*
    close burger menu with click on any item
    prevent auto showing at load
    catch "bootstrap is undefined" exception
*/

function main() {
    try {
        const bsCollapseHeader = window.bootstrap.Collapse.getOrCreateInstance('#navbarNav', {toggle: false});

        bsCollapseHeader.hide()

        const navLinksArr = document.querySelectorAll('#navbarNav .nav-link');

        navLinksArr.forEach(aLink => {
            aLink.addEventListener('click', () => {
                bsCollapseHeader.hide()
            })
        });
    } catch (error) {
        console.error('Error closing burger menu:', error);
    }
}

if (window.bootstrap) {
    main()
}
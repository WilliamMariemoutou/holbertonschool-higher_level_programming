const header = document.querySelector('#toggle_header');

header.onclick = function () {
    const header = document.querySelector('header');

    if (header.className === 'red') {
        header.className = 'green';
    } else {
        header.className = 'red';
    }
};

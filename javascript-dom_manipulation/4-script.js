const addItem = document.querySelector('#add_item');
addItem.onclick = function () {
    const list = document.querySelector('.my_list');

    const newItem = document.createElement('li');
    newItem.textContent = 'Item';
    list.appendChild(newItem);
};
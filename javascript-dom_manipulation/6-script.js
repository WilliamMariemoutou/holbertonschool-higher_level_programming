const url = 'https://swapi-api.hbtn.io/api/people/5/?format=json';

fetch(url)
.then(function (response) {
    return response.json();
})
.then (function (data) {
    const characterTag = document.querySelector('#character');

    characterTag.textContent = data.name;
})

.catch(function (reeor) {
    console.log('Error:', error);
})
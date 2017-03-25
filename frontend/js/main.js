const teamShow = require('./team-show');
const offers = require('./offers');
const initializeSearchbar = require('./searchbar');

document.addEventListener('DOMContentLoaded', () => {
    const route = document.querySelector('.main').getAttribute('id');
    initializeSearchbar(document.querySelector('#searchbar'));
    switch (route) {
        case 'team-show': teamShow(); break;
        case 'offers': offers(); break;
    }
});

$(document).ready(function () {
  const url = 'https://swapi-api.alx-tools.com/api/films/?format=json';
  $.getJSON(url, function (films) {
    $.each(films.results, function (index, movie) {
      const title = movie.title;
      const $li = $('<li>').text(title);
      $('#list_movies').append($li);
    });
  });
});

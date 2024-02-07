$(document).ready(function () {
  const url = 'https://swapi-api.alx-tools.com/api/people/5/?format=json';
  $.getJSON(url, function (person) {
    $('#character').text(person.name);
  });
});

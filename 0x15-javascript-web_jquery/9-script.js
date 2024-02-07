$(document).ready(function () {
  const url = 'https://hellosalut.stefanbohacek.dev/?lang=fr';
  $.getJSON(url, function (welcome) {
    $('#hello').text(welcome.hello);
  });
});

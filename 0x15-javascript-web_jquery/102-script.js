$(document).ready(function () {
  $('#btn_translate').click(function () {
    const lang = $('#language_code').val();
    const url = 'https://hellosalut.stefanbohacek.dev/?lang=' + lang;

    $.getJSON(url, function (welcome) {
      const translation = welcome.hello;
      $('#hello').html(translation);
    });
  });
});

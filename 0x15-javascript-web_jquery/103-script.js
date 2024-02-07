$(document).ready(function () {
  function fetchTranslate () {
    const lang = $('#language_code').val();
    const url = 'https://hellosalut.stefanbohacek.dev/?lang=' + lang;

    $.getJSON(url, function (welcome) {
      const translate = welcome.hello;
      $('#hello').html(translate);
    });
  }

  $('#btn_translate').click(fetchTranslate);
  $('#language_code').keypress(function (event) {
    if (event.which === 13) {
      fetchTranslate();
    }
  });
});

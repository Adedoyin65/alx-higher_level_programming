#!/usr/bin/node
const dan = $('#toggle_header');
const guv = $('header');
dan.click(function () {
  guv.toggleClass('green red');
});

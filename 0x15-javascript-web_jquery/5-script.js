#!/usr/bin/node
const dan = $('#add_item');
const guv = $('.my_list');
dan.click(function () {
  guv.append('<li>Item</li>');
});

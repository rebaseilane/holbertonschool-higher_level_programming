#!/usr/bin/node

const url = 'https://hellosalut.stefanbohacek.com/?lang=fr';
const hello = document.querySelector('#hello');

fetch(url)
  .then(function (response) {
    return response.json();
  })
  .then(function (data) {
    hello.textContent = data.hello;
  });
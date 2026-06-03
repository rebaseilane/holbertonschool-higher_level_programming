#!/usr/bin/node

const languages = ["C is fun", "Python is cool", "JavaScript is amazing"];

let i;
let output = '';

for (i = 0; i < languages.length; i++) {
  output += languages[i] + "\n";
}

process.stdout.write(output);

#!/usr/bin/node

const size = parseInt(process.argv[2], 10);

if (isNaN(size)) {
  console.log("Missing size");
} else {
  let i = 0;

  while (i < size) {
    let line = "";
    let j = 0;

    while (j < size) {
      line += "X";
      j += 1;
    }

    console.log(line);
    i += 1;
  }
}

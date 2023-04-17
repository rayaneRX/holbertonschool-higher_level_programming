#!/usr/bin/node

const fs = require('fs');

const ftr = process.argv[2];

fs.readFile(ftr, 'utf-8', (err, data) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log(data);
});

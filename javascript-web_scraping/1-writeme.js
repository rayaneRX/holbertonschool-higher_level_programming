#!/usr/bin/node

const fs = require('fs');

const ftr = process.argv[2];
const str = process.argv[3];

fs.writeFile(ftr, str, 'utf-8', (err) => {
  if (err) {
    console.error(err);
    return;
  }
});

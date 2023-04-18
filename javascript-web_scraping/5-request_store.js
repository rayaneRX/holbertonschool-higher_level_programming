#!/usr/bin/node

const fs = require('fs');
const request = require('request');

const ftr = process.argv[2];
const str = process.argv[3];

request(ftr, function (error, response, body) {
  if (error) {
    console.error(error);
    return;
  }

  fs.writeFile(str, body, 'utf-8', function (error) {
    if (error) {
      console.error(error);
    }
  });
});

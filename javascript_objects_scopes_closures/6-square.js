#!/usr/bin/node
const oldSquare = require('./5-square.js');

class Square extends Square {
    charPrint (c) {
        if (c === undefined) {
          c = 'X';
        }
      for (let i = 0; i < this.width; i++) {
        let row = '';
        for (let j = 0; j < this.height ; j++) {
          row += c;
        }
        console.log(row);
      }
    }
  }
module.exports = Square;

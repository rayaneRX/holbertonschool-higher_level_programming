#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
let counter = 0;
for (studentAge of list) {
  if (studentAge === searchElement) {
        counter++;
    }
}
return counter;
};

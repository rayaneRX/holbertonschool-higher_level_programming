#!/usr/bin/node

exports.esrever = function (list) {
  const reversList = [];
  for (let i = list.length - 1; i >= 0; i--) {
    reversList.push(list[i]);
  }
  return reversList;
};

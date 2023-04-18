#!/usr/bin/node

const request = require('request');
const api = process.argv[2];

request(api, function (error, response, body) {
  if (error) {
    console.error(error);
    return;
  }
    const todo = JSON.parse(body);
    const completedTasks = {};

    for (const todos of todo) {
      if (todos.completed === true) {
        if (todoItem.userId in completed) {
        completedTasks[todoItem.userId]++;
      } else {
        completedTasks[todoItem.userId] = 1;
      }
    }
  }
  console.log(completedTasks);
});

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
    const completed = []
    for (const todos of todo) {
          if (todos.completed === true)
            completed.push(todos)}
    for (let i=0; i < completed.length; i++) {
    const userId = completed[i].userId;
    if (completedTasks[userId]) completedTasks[userId]++;
    else completedTasks[userId] = 1;

  }
  console.log(completedTasks);
});

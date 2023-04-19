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
    console.log(completed.length);
  //   for (const todos of todo) {
  //     if (todos.completed === true) {
  //       // completed.push(todos)
  //       if (todos.userId in completed) {
  //       completedTasks[todos.userId]++;
  //     } else {
  //       completedTasks[todos.userId] = 1;
  //     }
  //   }
  // }
  // console.log(completedTasks);
});

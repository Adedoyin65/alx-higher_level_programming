#!/usr/bin/node
const request = require('request');

function countCompletedTasksByUrl (apiUrl) {
  request({ url: apiUrl, json: true }, (error, response) => {
    if (error) {
      console.error('Error fetching data:', error);
      return;
    }
    const todos = response.body;
    const completedTasks = todos.filter(todo => todo.completed);
    const completedCountByUser = completedTasks.reduce((acc, todo) => {
      if (acc[todo.userId]) {
        acc[todo.userId]++;
      } else {
        acc[todo.userId] = 1;
      }
      return acc;
    }, {});
    console.log(JSON.stringify(completedCountByUser, null, 2));
  });
}
const apiUrl = process.argv[2];
if (!apiUrl) {
  console.error('Usage: node script.js <API_URL>');
  process.exit(1);
}
countCompletedTasksByUrl(apiUrl);

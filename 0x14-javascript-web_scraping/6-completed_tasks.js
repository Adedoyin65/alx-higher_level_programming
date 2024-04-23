#!/usr/bin/node

const request = require('request');

// Extract API URL from command line arguments
const apiUrl = process.argv[2];

// Make a GET request to the API URL
request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    process.exit(1);
  }

  // Parse the JSON response body
  const todos = JSON.parse(body);

  // Initialize an object to store completed tasks by user ID
  const completedTasksByUser = {};

  // Iterate over each todo
  todos.forEach(todo => {
    // Check if the task is completed
    if (todo.completed) {
      // Increment the completed tasks count for the user
      if (completedTasksByUser[todo.userId]) {
        completedTasksByUser[todo.userId]++;
      } else {
        completedTasksByUser[todo.userId] = 1;
      }
    }
  });

  // Print users with completed tasks and the number of completed tasks
  console.log('Users with completed tasks:');
  for (const userId in completedTasksByUser) {
    console.log(`'${userId}': ${completedTasksByUser[userId]}`);
  }
});

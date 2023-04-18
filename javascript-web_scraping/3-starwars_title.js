#!/usr/bin/node

const request = require("request");

const movieID = process.argv[2];
const api = "https://swapi-api.hbtn.io/api/films/" + movieID;

request(api, function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    const movie = JSON.parse(body);
    console.log(movie.title);
  }
});

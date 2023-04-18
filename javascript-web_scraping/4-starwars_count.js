#!/usr/bin/node

const request = require('request');

const api = process.argv[2];

const characterID = '18';

let count = 0;

request(api, function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    const films = JSON.parse(body).results;

    for (let i = 0; i < films.length; i++) {
      const characters = films[i].characters;
      if (characters.includes(`https://swapi-api.hbtn.io/api/people/${characterID}/` )) {
        count++;
      }
      if (characters.includes('http://swapi.co/api/people/18/')) {
        count++;
      }
    }

    console.log(count);
  }
});

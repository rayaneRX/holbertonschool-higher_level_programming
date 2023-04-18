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
      if (characters.includes('https://swapi-api.hbtn.io/api/people/${characterID}/')) {
        count++;
      }
      if (characters.includes('https://s3.eu-west-3.amazonaws.com/hbtn.intranet/files/correction_system/2136/19645/file_2?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA4MYA5JM5DUTZGMZG%2F20230418%2Feu-west-3%2Fs3%2Faws4_request&X-Amz-Date=20230418T150822Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=2fdbac5d7ed42416978ba990e697dfcdc92eb2a12c1aa9106c69121200fa166e')) {
        count++;
      }
    }

    console.log(count);
  }
});

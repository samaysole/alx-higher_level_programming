#!/usr/bin/node
const request = require('request');
const requestURL = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

function printCharacters (characters, id) {
  request(characters[id], (error, response, body) => {
    if (error) {
      console.log(error);
    } else {
      console.log(JSON.parse(body).name);
      if (id + 1 < characters.length) {
        printCharacters(characters, id + 1);
      }
    }
  });
}

request(requestURL, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const characters = JSON.parse(body).characters;
    printCharacters(characters, 0);
  }
});

#!/usr/bin/node

const request = require('request');

const fetchCharacters = (characters, index) => {
  if (index === characters.length) return;

  request(characters[index], (error, response, body) => {
    if (error) {
      console.error('Error:', error);
    } else {
      const character = JSON.parse(body);
      console.log(character.name);
      fetchCharacters(characters, index + 1);
    }
  });
};


const getMovieCharacters = (movieId) => {
  const url = `https://swapi-api.hbtn.io/api/films/${movieId}`;

  request(url, (error, response, body) => {
    if (error) {
      console.error('Error:', error);
    } else {
      const movie = JSON.parse(body);
      fetchCharacters(movie.characters, 0);
    }
  });
};

const movieId = process.argv[2];
getMovieCharacters(movieId);

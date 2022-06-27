const axios = require('axios')
const hotpTotpGenerator = require('hotp-totp-generator')

const URL = 'https://dps-challenge.netlify.app/.netlify/functions/api/challenge';

const jsonBody = {
  github: 'https://github.com/zaidishz/dps222',
  email: 'zaidishz@gmail.com',
  url: 'https://dps222.herokuapp.com/',
  notes:
    'Classifier: Random Forest Regressor. Deployment: Heroku with flask'
};

const password = hotpTotpGenerator.totp({
  key: 'zaidishz@gmail.comDPSCHALLENGE',
  X: 120,
  T0: 0,
  algorithm: 'sha512',
  digits: 10
});

const headers = {
  'Content-Type': 'application/json',
  'Authorization': `Basic ${password}`
};

axios
  .post(URL, jsonBody, { headers })
  .then((response) => console.log('Response', response))
  .catch((error) => console.log('Error', error));
import { createClient, print } from 'redis';

const errMessage = 'Redis client not connected to the server:';
const successMessage = 'Redis client connected to the server';
const client = createClient();

client.on('error', err => console.log(`${errMessage} ${err}`))
  .on('connect', () => console.log(successMessage));


function setNewSchool(schoolName, value) {
  client.set(schoolName, value, print);
}

function displaySchoolValue(schoolName) {
  client.get(schoolName, (err, value) => {
    console.log(value);
  });
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');

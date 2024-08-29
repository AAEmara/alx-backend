import { createClient, print } from 'redis';
import { promisify } from 'util';

const errMessage = 'Redis client not connected to the server:';
const successMessage = 'Redis client connected to the server';
const client = createClient();

client.on('error', err => console.log(`${errMessage} ${err}`))
  .on('connect', () => console.log(successMessage));

const get = promisify(client.get).bind(client);

function setNewSchool(schoolName, value) {
  client.set(schoolName, value, print);
}

async function displaySchoolValue(schoolName) {
  const value = await get(schoolName);
  console.log(value);
}

(async () => {
    await displaySchoolValue('Holberton');
    await setNewSchool('HolbertonSanFrancisco', '100');
    await displaySchoolValue('HolbertonSanFrancisco');
})();

import { createClient } from 'redis';

const errMessage = 'Redis client not connected to the server:';
const successMessage = 'Redis client connected to the server';
const client = createClient();

client.on('error', err => console.log(`${errMessage} ${err}`))
  .on('connect', () => console.log(successMessage));

client.subscribe('holberton school channel');

client.on('message', (channel, message) => {
  console.log(message);
  if (message === 'KILL_SERVER') {
    client.unsubscribe('holberton school channel', () => {
      client.quit();
    });
  }
});

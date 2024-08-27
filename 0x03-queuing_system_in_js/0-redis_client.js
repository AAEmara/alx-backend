import { createClient } from 'redis';

const errMessage = 'Redis client not connected to the server:';
const successMessage = 'Redis client connected to the server';

const client = createClient();

client.on('error', err => console.log(`${errMessage} ${err}`))
  .on('connect', () => console.log(successMessage));

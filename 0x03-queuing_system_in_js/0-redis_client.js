import { createClient } from 'redis';

const errMessage = 'Redis client not connected to the server:';
const successMessage = 'Redis client connected to the server';

async function connectRedis() {
  const client = createClient();

  client.on('error', err => console.log(`${errMessage} ${err}`));
  client.on('connect', () => console.log(successMessage));

  await client.connect();
}

connectRedis();

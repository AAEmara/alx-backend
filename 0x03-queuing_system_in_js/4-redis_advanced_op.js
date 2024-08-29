import { createClient, print} from 'redis';

const errMessage = 'Redis client not connected to the server:';
const successMessage = 'Redis client connected to the server';
const client = createClient();

client.on('error', err => console.log(`${errMessage} ${err}`))
  .on('connect', () => console.log(successMessage));

client.HSET('HolbertonSchools', 'Portland', 50, print);
client.HSET('HolbertonSchools', 'Seattle', 80, print);
client.HSET('HolbertonSchools', 'New York', 20, print);
client.HSET('HolbertonSchools', 'Bogota', 20, print);
client.HSET('HolbertonSchools', 'Cali', 40, print);
client.HSET('HolbertonSchools', 'Paris', 2, print);

client.HGETALL('HolbertonSchools', (err, value) => {
  if (err) {
    console.log(err);
  } else {
    console.log(value)
  }
});

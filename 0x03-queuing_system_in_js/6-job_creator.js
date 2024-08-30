import { createQueue } from 'kue';

const queue = createQueue();
const jobData = {
  phoneNumber: 'string',
  message: 'string'
};
const job = queue.create('push_notification_code', jobData)
  .save( (err) => {
    if ( !err ) {
      console.log(`Notification job created ${job.id}`);
    }
  });

job.on('complete', (result) => {
  console.log('Notification job completed');
}).on('failed attempt', (result) => {
  console.log('Notification job failed');
});

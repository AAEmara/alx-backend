import { createQueue } from 'kue';

// Phone numbers which are going to be blacklisted by our jobs processors.
const blacklistedPhones = [ '4153518780', '4153518781' ];

const queue = createQueue();

function sendNotification(phoneNumber, message, job, done) {
  job.progress(0, 100);

  if (blacklistedPhones.includes(phoneNumber)) {
    job.failed();
    return done(new Error(`Phone number ${phoneNumber} is blacklisted`));
  }
  job.progress(50, 100);
  console.log(`Sending notification to ${phoneNumber}, with message: \
${message}`);
  done();
}

queue.process('push_notification_code_2', 2,
  (job, done) => {
    sendNotification(job.data.phoneNumber, job.data.message, job, done);
  });

import createPushNotificationsJobs from './8-job.js';
import { createQueue } from 'kue';
import { expect } from 'chai';

const queue = createQueue();

// Test Suite for `createPushNotificationsJobs` function.
describe('createPushNotificationsJobs', () => {
  before( () => {
    queue.testMode.enter();
  });

  afterEach( () => {
    queue.testMode.clear();
  });

  after( () => {
    queue.testMode.exit();
  });

  it('display an error message if jobs is not an array', (done) => {
    expect(createPushNotificationsJobs.bind('hi', queue))
      .to.throw(Error, 'Jobs is not an array');
    done();
  });

  it('create two new jobs to the queue', (done) => {
    const jobs = [
    {
      phoneNumber: '4153518780',
      message: 'This is the code 1234 to verify your account'
    },
    {
      phoneNumber: '4153518781',
      message: 'This is the code 4562 to verify your account'
    }];

    createPushNotificationsJobs(jobs, queue);
    expect(queue.testMode.jobs.length).to.equal(2);
    done();
  });
});

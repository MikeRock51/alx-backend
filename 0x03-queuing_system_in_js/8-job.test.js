const queue = require("kue").createQueue();
import createPushNotificationsJobs from "./8-job";
import { expect } from "chai";

before(function () {
  queue.testMode.enter();
});

afterEach(function () {
  queue.testMode.clear();
});

after(function () {
  queue.testMode.exit();
});
const job = [
  {
    phoneNumber: "4153518780",
    message: "This is the code 1234 to verify your account",
  },
  {
    phoneNumber: "234 897 255444 4",
    message: "Mike Rock is about to take off",
  },
];

describe("createPushNotificationsJobs", function () {
  it("Display a error message if jobs is not an array", function () {
    expect(() => createPushNotificationsJobs("job", queue)).throw(
      Error,
      "Jobs is not an array"
    );
  });

  it("Create two new jobs to the queue", function () {
    createPushNotificationsJobs(job, queue);
    expect(queue.testMode.jobs.length).to.equal(2);
    expect(queue.testMode.jobs[0].type).to.equal("push_notification_code_3");
    expect(queue.testMode.jobs[1].data).to.eql(job[1]);
  });
});

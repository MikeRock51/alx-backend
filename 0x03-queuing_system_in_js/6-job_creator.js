import kue from "kue";

const queue = kue.createQueue();
const jobData = {
  phoneNumber: "0810245847",
  message: "You really, really Rock",
};

const job = queue.create("push_notification_code", jobData).save((error) => {
  error
    ? console.log("Notification job failed")
    : console.log(`Notification job created: ${job.id}`);
}).on("complete", () => {
  console.log("Notification job completed");
});

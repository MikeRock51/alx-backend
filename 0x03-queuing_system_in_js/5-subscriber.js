import { createClient } from "redis";

const client = createClient();
const channel = "holberton school channel";

client
  .on("ready", () => {
    console.log("Redis client connected to the server");
    client.subscribe(channel);
  })
  .on("error", (err) => {
    console.log("Redis client not connected to the server: ", err);
  });

client.on("message", (source, message) => {
  source === channel && console.log(message);
  message === "KILL_SERVER" && client.unsubscribe(channel) && client.quit();
});

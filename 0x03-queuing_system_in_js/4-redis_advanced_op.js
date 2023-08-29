import { createClient, print } from "redis";

const client = createClient();

client
  .on("ready", () => {
    console.log("Redis client connected to the server");
  })
  .on("error", (err) => {
    console.log("Redis client not connected to the server: ", err);
  });

const hash = {
  Portland: 50,
  Seattle: 80,
  "New York": 20,
  Bogota: 20,
  Cali: 40,
  Paris: 2,
};

for (const key in hash) {
    client.hset("HolbertonSchools", key, hash[key], print);
}

client.hgetall("HolbertonSchools", (err, data) => {
    data && console.log(data);
    err && console.log(err);
});

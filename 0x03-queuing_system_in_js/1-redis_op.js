import { createClient } from "redis";

const client = createClient();

function setNewSchool(schoolName, value, callback) {
  client.set(schoolName, value, callback);
}

function displaySchoolValue(schoolName, callback) {
  client.get(schoolName, callback);
}

client.on("error", (err) =>
  console.log("Redis client not connected to the server: ", err)
);

client.on("ready", () => {
  console.log("Redis client connected to the server");
  displaySchoolValue("Holberton", (error, value) => {
	console.log(value);
  });
  setNewSchool("HolbertonSanFrancisco", "100", (error, response) => {
	console.log(`Response: ${response}`);
  });
  displaySchoolValue("HolbertonSanFrancisco", (error, value) => {
	console.log(value);
  });
});

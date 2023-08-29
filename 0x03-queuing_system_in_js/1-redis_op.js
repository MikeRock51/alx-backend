import { createClient } from "redis";

const client = createClient();

function setNewSchool(schoolName, value) {
  client.set(schoolName, value, (error, response) => {
	error && console.log(`Error: ${error}`);
	response && console.log(`Response: ${response}`);
  });
}

function displaySchoolValue(schoolName) {
  client.get(schoolName, (error, value) => {
	error && console.log(`Error: ${error}`);
	value && console.log(value);
  });
}

client.on("error", (err) =>
  console.log("Redis client not connected to the server: ", err)
);

client.on("ready", () => {
  console.log("Redis client connected to the server");
});

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');

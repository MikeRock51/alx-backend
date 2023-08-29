import { createClient } from "redis";
import { promisify } from "util";

const client = createClient();
const get = promisify(client.get).bind(client);
function setNewSchool(schoolName, value) {
  client.set(schoolName, value, (error, response) => {
	error && console.log(`Error: ${error}`);
	response && console.log(`Response: ${response}`);
  });
}

async function displaySchoolValue(schoolName) {
  try {
    console.log(await get(schoolName));
  } catch(error) {
    console.log(`Error: ${error}`)
  }
}

client.on("error", (err) =>
  console.log("Redis client not connected to the server: ", err)
);

client.on("ready", () => {
  console.log("Redis client connected to the server");
});

const displayAsync = promisify(displaySchoolValue);

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');

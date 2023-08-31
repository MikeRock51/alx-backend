import express from 'express';
import { createClient } from 'redis';
import { promisify } from 'util';

const app = express();
const port = 1245;
const client = createClient();

client.on("error", (err) =>
  console.log("Redis client not connected to the server: ", err)
);

client.on("ready", () => {
  console.log("Redis client connected to the server");
});

const listProducts = [
  {
    id: 1,
    name: "Suitcase 250",
    price: 50,
    stock: 4,
  },
  {
    id: 2,
    name: "Suitcase 450",
    price: 100,
    stock: 10,
  },
  {
    id: 3,
    name: "Suitcase 650",
    price: 350,
    stock: 2,
  },
  {
    id: 4,
    name: "Suitcase 1050",
    price: 550,
    stock: 5,
  },
];

function getItemById(id) {
  return listProducts.filter((product) => product.id === id)[0];
}

function reserveStockById(itemId, stock) {
  client.set(`item.${itemId}`, stock, (error, reply) => {
    error && console.log(`Error: ${error}`);
    value && console.log(value);
  });
}

async function getCurrentReservedStockById(itemId) {
  const get = promisify(client.hget).bind(client);
  return await get('item', itemId);
}

app.get("/list_products", (req, res) => {
  res.send(listProducts);
});

app.get('/list_products/:itemId', async (req, res) => {
  const id = req.params.itemId;
  const stock = await getCurrentReservedStockById(id);
  !stock ? res.send({"status":"Product not found"})
  : res.send(stock);
});

app.listen(port, () => {
  console.log(`App listening on port ${port}`);
});

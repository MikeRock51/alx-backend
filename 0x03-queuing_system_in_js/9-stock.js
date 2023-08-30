const express = require("express");

const app = express();
const port = 1245;

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

app.get('/list_products', (req, res) => {
    res.send(listProducts);
})

app.listen(port, () => {
    console.log(`App listening on port ${port}`);
});

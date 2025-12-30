const API_URL = "http://127.0.0.1:8000/products/";

async function addProduct() {
  const product = {
    iid: document.getElementById("iid").value,
    iname: document.getElementById("iname").value,
    icategory: document.getElementById("icategory").value,
    price: parseFloat(document.getElementById("price").value),
    quantity: parseInt(document.getElementById("quantity").value)
  };

  const res = await fetch(API_URL, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(product)
  });

  const result = await res.json();
  alert(result.message || result.detail);
}

async function loadProducts() {
  const res = await fetch(API_URL);
  const products = await res.json();
  const table = document.getElementById("productTable");
  table.innerHTML = "<tr><th>ID</th><th>Name</th><th>Category</th><th>Price</th><th>Quantity</th></tr>";
  products.forEach(p => {
    table.innerHTML += `<tr>
      <td>${p.iid}</td>
      <td>${p.iname}</td>
      <td>${p.icategory}</td>
      <td>${p.price}</td>
      <td>${p.quantity}</td>
    </tr>`;
  });
}

document.getElementById("button-get-products").addEventListener("click", function () {
  fetch("http://127.0.0.1:8000/all_products/")
    .then((response) => response.json())
    .then((data) => {
      const productsDiv = document.getElementById("products");

      data.forEach((product) => {
        const productDiv = document.createElement("div");
        productDiv.className = "product";

        for (const key in product) {
          const detail = document.createElement("p");
          detail.textContent = `${key}: ${product[key]}`;
          productDiv.appendChild(detail);
        }

        productsDiv.appendChild(productDiv);
      });
    })
    .catch((error) => console.error("Error:", error));
});

document.getElementById("get-current-product").addEventListener("click", function () {
  const ProductName = document.getElementById("name-of-product").value;
  const productDetailDiv = document.getElementById("detail-product");
  productDetailDiv.innerHTML = "";
  const productsDiv = document.getElementById("products");
  productsDiv.innerHTML = "";

  fetch(`http://127.0.0.1:8000/product/${ProductName}`)
    .then((response) => response.json())
    .then((product) => {
      const productDetailDiv = document.getElementById("detail-product");
      const productDiv = document.createElement("div");
      productDiv.className = "product";

      for (const key in product) {
        const detail = document.createElement("p");
        detail.textContent = `${key}: ${product[key]}`;
        productDiv.appendChild(detail);
      }

      productDetailDiv.appendChild(productDiv);
    })
    .catch((error) => console.error("Error:", error));
});

document.getElementById("get-field-of-product").addEventListener("click", function () {
  const ProductField = document.getElementById("field-of-product").value;
  const ProductName = document.getElementById("name-of-product").value;
  const DetailFieldDiv = document.getElementById("detail-product");
  DetailFieldDiv.innerHTML = "";
  const productsDiv = document.getElementById("products");
  productsDiv.innerHTML = "";

  fetch(`http://127.0.0.1:8000/product/${ProductName}/${ProductField}`)
    .then((response) => response.json())
    .then((field) => {
      const fieldDiv = document.createElement("div");
      fieldDiv.className = "product";

      const detail = document.createElement("p");
      detail.textContent = `${field.field}: ${field.value}`;
      fieldDiv.appendChild(detail);

      DetailFieldDiv.appendChild(fieldDiv);
    })
    .catch((error) => console.error("Error:", error));
});

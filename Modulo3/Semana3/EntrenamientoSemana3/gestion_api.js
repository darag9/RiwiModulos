fetch('http://localhost:3000/productos')
    .then(response => response.json())
    .then(data => console.log('Available products: ', data))
    .catch(error => console.error('Error:', error));

const newProduct = {'id': 4, 'name': 'monitor', 'precio': 200};

fetch('http://localhost:3000/productos', {
    method: 'POST',
    headers: {'Content-type': 'application/json'},
    body: JSON.stringify(newProduct)
})
    .then(response => response.json())
    .then(data => console.log('Product updated: ', data))
    .catch(error => console.error('Error: ', error));

const updatedProduct = {'nombre': 'laptop', 'precio': 2500};

// Specify the product ID in the URL for the PUT request
fetch('http://localhost:3000/productos/4', {
    method: 'PUT',
    headers: {'Content-type': 'application/json'},
    body: JSON.stringify(updatedProduct)
})
    .then(response => response.json())
    .then(data => console.log('Product updated: ', data))
    .catch(error => console.error('Error: ', error));
fetch('http://localhost:3000/productos/4', {method: 'DELETE'})
    .then(() => console.log('Effectively deleted product.'))
    .catch(error => console.error('Error. Product could not be deleted.', error));


function productValidation(product) {
    if (!product.nombre || typeof product.precio !== 'number') {
        console.error('Error. Product properties not valid.');
        return false;
    }
    return true;
}


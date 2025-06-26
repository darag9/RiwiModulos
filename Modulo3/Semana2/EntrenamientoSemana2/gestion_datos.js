console.log('Object management with data, sets and maps!');

/* Object initialization */

const products = {
    1: {
        id: 123, 
        name: 'rice', 
        price: 6000
        },
    2: {
        id: 456, 
        name: 'milk', 
        price: 6000
        },
    3: {
        id: 789, 
        name: 'tomato', 
        price: 5600
        },
    4: {
        id: 789, 
        name: 'tomato', 
        price: 3200
        },
};

/* Create set out of the products */

const setProducts = new Set(Object.values(products).map((product) => product.name));
console.log(setProducts);

/* Create map of the products */

const mapProducts = new Map([
    ['rice', 'organics'],
    ['tomato', 'organics'],
    ['milk', 'drinks']
]);

console.log('Products and categories map: ', mapProducts);

/* Print the products */

for (const product in products) {
    console.log(`Product #: ${product}\nId: ${products[product].id}\nProduct: ${products[product].name}\nPrice: ${products[product].price}`);
};

/* Print the unique products from the set */

for (const product of setProducts) {
    console.log(`Unique product: ${product}`);
};

/* Print the categories and the products from the map */

mapProducts.forEach((category, product) => {
    console.log(`Product: ${product}\nCategory: ${category}`);
});

/* Complete prints test */

console.log('Data management complete tests!');

console.log('Product list (Object): ', products);
console.log('Unique products list (Sets): ', setProducts);
console.log('Categories and prodcuts (Maps): ', mapProducts);
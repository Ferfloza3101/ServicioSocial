// Precio del producto
let precioProducto = 100;

// Porcentaje del IVA
let porcentajeIVA = 21;

// Calcular el precio del IVA
let precioIVA = (precioProducto * porcentajeIVA) / 100;

// Calcular el precio final
let precioFinal = precioProducto + precioIVA;

// Mostrar los resultados
console.log("Precio del IVA: " + precioIVA + " euros");
console.log("Precio final: " + precioFinal + " euros");

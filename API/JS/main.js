// Seleccionamos el contenedor donde se mostrarán los Pokémon
const listaPokemon = document.querySelector("#listapokemon");
const URL = "https://pokeapi.co/api/v2/pokemon/";

// Función para cargar todos los Pokémon en orden
function loadAllPokemon() {
  listaPokemon.innerHTML = "";

  const promesas = [];

  for (let i = 1; i <= 386; i++) {
    promesas.push(fetch(`${URL}${i}`).then(response => response.json()));
  }

  Promise.all(promesas)
    .then(pokemonArray => {
      pokemonArray.sort((a, b) => a.id - b.id);
      pokemonArray.forEach(poke => mostrarPokemon(poke));
    })
    .catch(error => console.error("Error en la carga de Pokémon:", error));
}

loadAllPokemon();

function mostrarPokemon(poke) {
  let tipos = poke.types
    .map(type => `<p class="${type.type.name} tipo">${type.type.name}</p>`)
    .join("");

  let pokeId = poke.id.toString().padStart(3, "0");

  const div = document.createElement("div");
  div.classList.add("pokemon");

  if (poke.types.length > 0) {
    div.classList.add(poke.types[0].type.name.toLowerCase());
    div.style.setProperty("--type-primary", `var(--type-${poke.types[0].type.name.toLowerCase()})`);
  }

  if (poke.types.length > 1) {
    div.classList.add("dual-type");
    div.style.setProperty("--type-secondary", `var(--type-${poke.types[1].type.name.toLowerCase()})`);
  }

  div.innerHTML = `
    <div class="pokemon-imagen">
      <img src="${poke.sprites.other["official-artwork"].front_default}" alt="${poke.name}">
    </div>
    <div class="pokemon-info">
      <div class="nombre-contenedor">
        <p class="pokemon-id">#${pokeId}</p>
        <h2 class="pokemon-nombre">${poke.name}</h2>
      </div>
      <div class="pokemon-tipos">
        ${tipos}
      </div>
      <div class="pokemon-stats">
        <p class="stat">${poke.height}m</p>
        <p class="stat">${poke.weight}kg</p>
      </div>
    </div>
  `;
  listaPokemon.append(div);
}

const botonesDropdown = document.querySelectorAll(".dropdown-content a");

botonesDropdown.forEach(boton => {
  boton.addEventListener("click", event => {
    event.preventDefault();

    const tipoSeleccionado = event.currentTarget.classList[1];
    listaPokemon.innerHTML = "";

    const promesasTipos = [];

    for (let i = 1; i <= 386; i++) {
      promesasTipos.push(fetch(`${URL}${i}`).then(response => response.json()));
    }

    Promise.all(promesasTipos)
      .then(pokemonArray => {
        const pokemonsFiltrados = pokemonArray.filter(poke =>
          poke.types.some(tipo => tipo.type.name === tipoSeleccionado)
        );
        pokemonsFiltrados.sort((a, b) => a.id - b.id);
        pokemonsFiltrados.forEach(poke => mostrarPokemon(poke));
      })
      .catch(error => console.error("Error en el filtrado por tipo:", error));
  });
});

const botonesGeneracion = document.querySelectorAll(".generation-buttons .gen-button");

const generaciones = {
  "1ra Generación": [1, 151],
  "2da Generación": [152, 251],
  "3ra Generación": [252, 386]
};

botonesGeneracion.forEach(boton => {
  boton.addEventListener("click", event => {
    const generacionSeleccionada = event.target.textContent.trim();
    const [inicio, fin] = generaciones[generacionSeleccionada];

    listaPokemon.innerHTML = "";

    const promesasGeneracion = [];

    for (let i = inicio; i <= fin; i++) {
      promesasGeneracion.push(fetch(`${URL}${i}`).then(response => response.json()));
    }

    Promise.all(promesasGeneracion)
      .then(pokemonArray => {
        pokemonArray.sort((a, b) => a.id - b.id);
        pokemonArray.forEach(poke => mostrarPokemon(poke));
      })
      .catch(error => console.error("Error en la carga de generación:", error));
  });
});

const logoPokedex = document.querySelector(".nav-left img");

if (logoPokedex) {
  logoPokedex.addEventListener("click", event => {
    event.preventDefault();
    loadAllPokemon();
  });
}

const searchInput = document.querySelector(".search-input");
const searchButton = document.querySelector(".search-button");

searchButton.addEventListener("click", () => {
  const searchQuery = searchInput.value.trim().toLowerCase();

  if (searchQuery === "") {
    alert("Por favor, ingresa un nombre o número de Pokémon.");
    return;
  }

  listaPokemon.innerHTML = "";

  fetch(`${URL}${searchQuery}`)
    .then(response => {
      if (!response.ok) {
        throw new Error("Pokémon no encontrado");
      }
      return response.json();
    })
    .then(data => mostrarPokemon(data))
    .catch(error => {
      console.error("Error en la búsqueda:", error);
      alert("No se encontró ningún Pokémon con ese nombre o número.");
    });
});
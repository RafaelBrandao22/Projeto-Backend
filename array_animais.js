let animais = ["cachorro", "gato", "elefante", "leão", "tigre"];

// Imprime todos os elementos do array
for (let i = 0; i < animais.length; i++) {
  console.log(animais[i]);
}

// Função para contar quantos elementos existem no array
function contarElementos(array) {
  let contador = 0;

  for (let i = 0; i < array.length; i++) {
    contador++;
  }

  return contador;
}

// Chama a função e imprime o total
let total = contarElementos(animais);
console.log("Total de elementos:", total);

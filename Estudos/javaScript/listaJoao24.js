let num1 = "999999999999999999999999999999";
let num2 = "1";


let arr1 = num1.split("");
let arr2 = num2.split("");

let resultado = [];
let resto = 0;


while (arr1.length > 0 || arr2.length > 0 || resto > 0) {

  let dig1 = 0;
  let dig2 = 0;

  
  if (arr1.length > 0) {
    dig1 = Number(arr1.pop());
  }

  if (arr2.length > 0) {
    dig2 = Number(arr2.pop());
  }

  let soma = dig1 + dig2 + resto;

  
  resultado.unshift(soma % 10);

  
  resto = Math.floor(soma / 10);
}


console.log(resultado.join(""));
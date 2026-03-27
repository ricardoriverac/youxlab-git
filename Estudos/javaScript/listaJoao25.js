let dia = 1;
let mes = 1;
let ano = 2012;
let hora = 14;
let minuto = 35;
let segundo = 2;

let intervalo = 83046391;


let data = new Date(ano, mes - 1, dia, hora, minuto, segundo);


data.setSeconds(data.getSeconds() + intervalo);


let novoDia = data.getDate();
let novoMes = data.getMonth() + 1;
let novoAno = data.getFullYear();

let novaHora = data.getHours();
let novoMinuto = data.getMinutes();
let novoSegundo = data.getSeconds();


console.log(novoDia + "/" + novoMes + "/" + novoAno);
console.log(novaHora + ":" + novoMinuto + ":" + novoSegundo);
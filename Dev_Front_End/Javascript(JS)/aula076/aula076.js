const numero = document.getElementById("numero");
const btn_promessa = document.getElementById("btn_promessa");

btn_promessa.addEventListener("click", (evt) => {
  numero.innerHTML = "Processando...";
  promessa();
});

const promessa = () => {
  let p = new Promise((res, rej) => {
    let resultado = false;
    let tempo = 3000;
    setTimeout(() => {
      if (resultado) {
        res("Deu tudo certo");
        numero.innerHTML = "Deu tudo certo";
        numero.classList.remove("erro");
        numero.classList.add("ok");
      } else {
        rej("Deu tudo errado");
        numero.innerHTML = "Deu tudo errado";
        numero.classList.add("erro");
        numero.classList.remove("ok");
      }
    }, tempo);
  });
  return p;
};

numero.innerHTML = "Esperando";

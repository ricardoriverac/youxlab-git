const btn_inserir = document.querySelector("#btn_inserir");
const body = document.querySelector("#body");

function adicionarDados() {
  const nome = document.getElementById("inputNome").value;
  const telefone = document.getElementById("inputTelefone").value;
  const cpf = document.getElementById("inputCpf").value;
  const email = document.getElementById("inputEmail").value;

  const btnEditar = (document.createElement("button").innerHTML =
    "<button class='classEditar'>Editar</button>");
  const btnRemover = (document.createElement("button").innerHTML =
    "<button class='classRemover'>Remover</button>");

  const novaLinha = document.createElement("tr");
  const novoNome = document.createElement("td");
  const novoTelefone = document.createElement("td");
  const novoCpf = document.createElement("td");
  const novoEmail = document.createElement("td");
  const novosBotoes = document.createElement("td");

  novoNome.classList.add("colunaNome");
  novoTelefone.classList.add("colunaTelefone");
  novoCpf.classList.add("colunaCpf");
  novoEmail.classList.add("colunaEmail");

  novoNome.textContent = nome;
  novoTelefone.textContent = telefone;
  novoCpf.textContent = cpf;
  novoEmail.textContent = email;
  novosBotoes.innerHTML = btnEditar + btnRemover;

  novaLinha.appendChild(novoNome);
  novaLinha.appendChild(novoTelefone);
  novaLinha.appendChild(novoCpf);
  novaLinha.appendChild(novoEmail);
  novaLinha.appendChild(novosBotoes);

  body.appendChild(novaLinha);

  const botaoRemover = novaLinha.querySelector(".classRemover");
  botaoRemover.addEventListener("click", (evt) => {
    novaLinha.remove();
  });

  const nome2 = document.getElementById("inputNome");
  const telefone2 = document.getElementById("inputTelefone");
  const cpf2 = document.getElementById("inputCpf");
  const email2 = document.getElementById("inputEmail");

  const botaoEditar = novaLinha.querySelector(".classEditar");
  botaoEditar.addEventListener("click", (evt) => {
    const dados = novaLinha.querySelectorAll("td");
    nome2.value = dados[0].textContent;
    telefone2.value = dados[1].textContent;
    cpf2.value = dados[2].textContent;
    email2.value = dados[3].textContent;

    novaLinha.remove();
  });
}

function limparInput() {
  const inputs = document.getElementsByClassName("mainInput");
  for (limpar of inputs) {
    limpar.value = "";
  }
}

btn_inserir.addEventListener("click", (evt) => {
  adicionarDados();
  limparInput();
});

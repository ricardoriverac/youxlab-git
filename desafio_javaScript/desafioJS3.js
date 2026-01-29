function limparInput() {
  const inputs = document.getElementsByClassName("mainInput");
  for (limpar of inputs) {
    limpar.value = "";
  }
}

function inserirPessoa() {
  const nome = document.getElementById("f_nome").value;
  const telefone = document.getElementById("f_numero").value;
  const cpf = document.getElementById("f_cpf").value;
  const email = document.getElementById("f_email").value;

  const tbody = document.getElementById("tbody");

  const novaLinha = tbody.insertRow();
  const celulanome = novaLinha.insertCell(0);
  const celulatelefone = novaLinha.insertCell(1);
  const celulacpf = novaLinha.insertCell(2);
  const celulaemail = novaLinha.insertCell(3);
  const celulaBotao = novaLinha.insertCell(4);

  celulaBotao.innerHTML =
    '<button class="btn_remove">Remover</button> <button class="btn_editar">Editar</button>';
  celulanome.textContent = nome;
  celulatelefone.textContent = telefone;
  celulacpf.textContent = cpf;
  celulaemail.textContent = email;
  (celulasTotal = nome), telefone, cpf, email;

  limparInput();

  const remove = novaLinha.querySelector(".btn_remove");
  remove.addEventListener("click", (evt) => {
    novaLinha.remove();
  });

  const InputNome = document.getElementById("f_nome");
  const InputTelefone = document.getElementById("f_numero");
  const InputCpf = document.getElementById("f_cpf");
  const InputEmail = document.getElementById("f_email");

  const botaoEditar = novaLinha.querySelector(".btn_editar");
  botaoEditar.addEventListener("click", (evt) => {
    const dados = novaLinha.querySelectorAll("td");

    InputNome.value = dados[0].textContent;
    InputTelefone.value = dados[1].textContent;
    InputCpf.value = dados[2].textContent;
    InputEmail.value = dados[3].textContent;

    novaLinha.remove();
  });
}


const btn_inserir = document.getElementById("btn_inserir");
btn_inserir.addEventListener("click", () => {
  inserirPessoa();
});

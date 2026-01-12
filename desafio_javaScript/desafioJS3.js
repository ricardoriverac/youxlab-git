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

  const nomeInput = document.getElementById("f_nome");
  const telefoneInput = document.getElementById("f_numero");
  const cpfInput = document.getElementById("f_cpf");
  const emailInput = document.getElementById("f_email");

  const editar = novaLinha.querySelector(".btn_editar");
  editar.addEventListener("click", (evt) => {
    const dados = novaLinha.querySelectorAll("td");

    nomeInput.value = dados[0].textContent;
    telefoneInput.value = dados[1].textContent;
    cpfInput.value = dados[2].textContent;
    emailInput.value = dados[3].textContent;

    novaLinha.remove();
  });
}

const btn_inserir = document.getElementById("btn_inserir");
btn_inserir.addEventListener("click", () => {
  inserirPessoa();
});

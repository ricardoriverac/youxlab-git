const botaoInserir = document.getElementById("botaoInserir");

function limparcontainer() {
    const inputs = document.getElementsByClassName("informacoes");
    for (limpar of inputs) {
        limpar.value = "";
    }
}


function inserir() {
    const valornome = document.getElementById("input-nome").value
    const valorTelefone = document.getElementById("input-telefone").value
    const valorCPF = document.getElementById("input-cpf").value
    const valorEmail = document.getElementById("input-email").value
    const corpotabela = document.getElementById("tabelaCorpo")

    let novaLinha = document.createElement("tr")
    novaLinha.innerHTML = `
        <td>${valornome}</td>
        <td>${valorTelefone}</td>
        <td>${valorCPF}</td>
        <td>${valorEmail}</td>
        <td>
        <button id="btn_remover" onclick=excluir(this)>Remover</button>
        <button onclick=editar(this)>Editar</button>
        </td>
        `;
    corpotabela.appendChild(novaLinha)
}

function excluir(botao) {
    const novaLinha = botao.closest('tr')
    if (novaLinha) {
        novaLinha.remove()
    }
}

botaoInserir.addEventListener("click", function () {
    inserir()
    limparcontainer()
})

function editar(editarBotao) {
    const editarNome = document.getElementById("input-nome")
    const editarTelefone = document.getElementById("input-telefone")
    const editarCPF = document.getElementById("input-cpf")
    const editarEmail = document.getElementById("input-email")

    const novaLinha2 = editarBotao.closest('tr')

    if (novaLinha2) {
        const dados = novaLinha2.querySelectorAll("td")

        editarNome.value = dados[0].textContent
        editarTelefone.value = dados[1].textContent
        editarCPF.value = dados[2].textContent
        editarEmail.value = dados[3].textContent

        novaLinha2.remove()
    }
}





// NOME

const inputInserir = document.getElementById("botaoInserir")

function inserir() {
    const nome = document.getElementById("inputnome").value
    const Telefone = document.getElementById("inputtelefone").value
    const CPF = document.getElementById("inputcpf").value
    const email = document.getElementById("inputemail").value
    const tabelaCorpo = document.getElementById("corpoTabela")


    let novaLinha = document.createElement("tr")
    novaLinha.innerHTML = `
        <td>${nome}</td>
        <td>${Telefone}</td>
        <td>${CPF}</td>
        <td>${email}</td>
        <td>
        <button id = "editarBotao" class="Editar" onclick=editar(this)>Editar</button>
        <button class="remove" onclick=excluir(this)>Remover</button>
        </td>
    `;

    tabelaCorpo.appendChild(novaLinha)
    inputnome.value = ''
    inputtelefone.value = ''
    inputcpf.value = ''
    inputemail.value = ''
}

inputInserir.addEventListener("click", function () {
    inserir()
})

function excluir(botao) {
    const novaLinha = botao.closest('tr')
    if (novaLinha) {
        novaLinha.remove()
    }
}

function editar(botao){
    
    const nomeInput = document.getElementById("inputnome");
    const telefoneInput = document.getElementById("inputtelefone");
    const cpfInput = document.getElementById("inputcpf");
    const emailInput = document.getElementById("inputemail");

    const novaLinha = botao.closest('tr')

    if(novaLinha){

        const dados = novaLinha.querySelectorAll("td");
        
        nomeInput.value = dados[0].textContent;
        cpfInput.value = dados[2].textContent
        emailInput.value = dados[3].textContent
        telefoneInput.value = dados[1].textContent
        
        novaLinha.remove();
    }

}

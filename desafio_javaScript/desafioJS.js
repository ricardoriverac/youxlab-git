const btn_jogar=document.querySelector("#btn_jogar")
const tabuleiro=document.querySelector("#tabuleiro")

function criarQuadrados() {
    const container = document.getElementById('container-quadrados');

    

    for (let i = 0; i < 3; i++) {
        const novoQuadrado = document.createElement('div');

        novoQuadrado.classList.add('quadrado');

        
        novoQuadrado.textContent = `Q${i + 1}`;
        container.appendChild(novoQuadrado);
    }
}

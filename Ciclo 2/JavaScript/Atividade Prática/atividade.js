let jogadorAtual = "X";
let jogoAtivo = false;
let tabuleiro = ["", "", "", "", "", "", "", "", ""];

const casas = document.querySelectorAll("#tabuleiro div");
const textoJogador = document.getElementById("jogadorDaVez");
const mensagem = document.getElementById("mensagem");
const botaoJogar = document.getElementById("botaoJogar");
const tabuleiroTela = document.getElementById("tabuleiro");

botaoJogar.addEventListener("click", () => {
    jogoAtivo = true;
    tabuleiroTela.style.display = "grid";
    textoJogador.textContent = "Jogador da vez: " + jogadorAtual;
    mensagem.textContent = "";
});

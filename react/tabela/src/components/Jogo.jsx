import { useState, useEffect } from "react";
import Square from "./Square";
import "./Square.css";
import Modal1 from "./Modal1";
import "./Jogo.css";
import ButtonCloseModal from "./ButtonCloseModal";

function Jogo({ funcao }) {
  const [board, setBoard] = useState(Array(9).fill(null));
  const [player, setPlayer] = useState("X");
  const [jogadasJogador1, setJogadasJogador1] = useState([]);
  const [jogadasJogador2, setJogadasJogador2] = useState([]);
  const [isModalOpen, setIsModalOpen] = useState(false);
  const [vencedor, setVencedor] = useState("");
  const [placarJogador1, setPlacarJogador1] = useState(0);
  const [placarJogador2, setPlacarJogador2] = useState(0);
  const [empate, setEmpate] = useState("");

  function boardCompleto(board) {

    for (const event of board) {
      if (event == null) {
        return false
      }
    }
    
    return true;
  }

  function zeraPlacar() {
    setPlacarJogador1(0);
    setPlacarJogador2(0);
  }

  function resetaJogo() {
    setBoard(Array(9).fill(null));
    setJogadasJogador1([]);
    setJogadasJogador2([]);
    setPlayer("X");
  }

  function abrirModal() {
    setIsModalOpen(true);
  }

  function fecharModal() {
    setIsModalOpen(false);
    resetaJogo();
  }

  const combinacoes = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6],
  ];

  useEffect(() => {
    for (let i = 0; i < combinacoes.length; i++) {
      const combinacao = combinacoes[i];

      const venceuJogador1 =
        jogadasJogador1.includes(combinacao[0]) &&
        jogadasJogador1.includes(combinacao[1]) &&
        jogadasJogador1.includes(combinacao[2]);
      const venceuJogador2 =
        jogadasJogador2.includes(combinacao[0]) &&
        jogadasJogador2.includes(combinacao[1]) &&
        jogadasJogador2.includes(combinacao[2]);
      if (venceuJogador1) {
        setPlacarJogador1((valorAtual) => valorAtual + 1);
        setVencedor("Jogador X venceu");
        setIsModalOpen(true);
      } else if (venceuJogador2) {
        setPlacarJogador2((valorAtual) => valorAtual + 1);
        setVencedor("Jogador O venceu");
        setIsModalOpen(true);
      } else if (boardCompleto(board)) {
        setVencedor("O jogo deu velha");
        setIsModalOpen(true);
      }
    }
  }, [board]);

  function handleOnClick(numero) {
    if (board[numero] !== null) return;

    const newBoard = [...board];

    newBoard[numero] = player;
    setBoard(newBoard);

    if (player == "X") {
      setJogadasJogador1((jogadasAntes) => [...jogadasAntes, numero]);
    } else {
      setJogadasJogador2((jogadasAntes) => [...jogadasAntes, numero]);
    }

    setPlayer(player === "X" ? "O" : "X");
  }

  const quadrados = [0, 1, 2, 3, 4, 5, 6, 7, 8];
  return (
    <div className="central">
      <div className="vez">
        <p>Vez do Jogador {player}</p>
      </div>
      <div className="placar">
        <p>Placar Jogador X: {placarJogador1}</p>{" "}
        <p>Placar Jogador O: {placarJogador2}</p>
      </div>
      <div className="zerar">
        <button className="zera" onClick={zeraPlacar}>
          Zerar placar
        </button>
      </div>
      <div className="tabuleiro">
        {quadrados.map((posicao) => {
          return (
            <Square
              numero={posicao}
              board={board[posicao]}
              clicar={handleOnClick}
            />
          );
        })}
        {isModalOpen && (
          <Modal1 fecharModal={fecharModal} vencedor={vencedor} />
        )}
      </div>
    </div>
  );

}

export default Jogo;

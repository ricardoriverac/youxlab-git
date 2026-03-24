import { useState } from "react";
import "./Jogo.css";
import Placar from "./Placar";

const Jogo = ({ onClick, xbola, board, jogadorX, jogadorO }) => {
  const posicoes = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8], // horizontal
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8], // vertical
    [0, 4, 8],
    [2, 4, 6], // diagonal
  ];

  const [vitorias, setVitorias] = useState([[0], [0]]);

  const pontosX = vitorias[0];
  const pontosO = vitorias[1];

  const vencedor = posicoes.reduce((ac, [a, b, c]) => {
    if (ac) return ac;
    if (board[a] && board[a] === board[b] && board[a] === board[c]) {
      if (board[a] === "X") {
        setVitorias((vitorias[0] = vitorias[0] + 1));
      } else {
        setVitorias((vitorias[1] = vitorias[1] + 1));
      }
      return board[a];
    }
    return null;
  }, null);

  const velha =
    !vencedor && board.every((value) => value !== null && value !== "");
  const status = vencedor
    ? `Vencedor: ${vencedor}`
    : velha
      ? "Velha"
      : `Jogador atual:${xbola}`;
  return (
    <>
      <h1 className="jogador">{status}</h1>
      <div className="jogo">
        {board.map((valor, index) => (
          <button
            key={index}
            className="quadrado"
            onClick={() => {
              if (!vencedor && !velha && valor === null) onClick(index);
            }}
          >
            {valor || ""}
          </button>
        ))}
      </div>
      <div className="placar">
        <Placar
          textX={jogadorX}
          pontosX={pontosX}
          textO={jogadorO}
          pontosO={pontosO}
        />
      </div>
    </>
  );
};

export default Jogo;

import React, { useState, useEffect } from "react";
import Square from "./Square";
import "./Square.css";

function Jogo() {
  const [board, setBoard] = useState(Array(9).fill(null));
  const [player, setPlayer] = useState("X");
  const [jogadasJogador1, setJogadasJogador1] = useState([]);
  const [jogadasJogador2, setJogadasJogador2] = useState([]);

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
    console.log("Jogador 1 atualizado:", jogadasJogador1);
    jogadasJogador1.map(numero)
  }, [jogadasJogador1]);

  useEffect(() => {
    console.log("Jogador 2 atualizado:", jogadasJogador2);
  }, [jogadasJogador2]);

  // const [position, setPosition] = useState([]);
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
    console.log(newBoard);

    console.log("jogadasJogador1 :>> ", jogadasJogador1);
    console.log("jogadasJogador2 :>> ", jogadasJogador2);
  }
  // const quadrados = [
  //   [0, 1, 2],
  //   [3, 4, 5],
  //   [6, 7, 8],
  // ];
  const quadrados = [0, 1, 2, 3, 4, 5, 6, 7, 8];
  return (
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
    </div>
  );
  // return (
  //   <div className="tabuleiro">
  //     {quadrados.map((linha) => {
  //       return linha.map((posicao) => {
  //         return (
  //           <Square
  //             numero={posicao}
  //             board={board[posicao]}
  //             clicar={handleOnClick}
  //           />
  //         );
  //       });
  //     })}
  //   </div>
  // );
}

export default Jogo;

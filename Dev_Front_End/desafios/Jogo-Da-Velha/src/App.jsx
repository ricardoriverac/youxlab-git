import { useState } from "react";

import "./App.css";
import Input from "./components/Input";
import Jogo from "./components/Jogo";

function App() {
  const [board, setBoard] = useState(Array(9).fill(null));
  const [ativo, setAtivo] = useState("X");
  const [inputX, setInputX] = useState("");
  const [inputO, setInputO] = useState("");

  function handleOnClick(numero) {
    if (board[numero] !== null) return;
    const newBoard = [...board];
    newBoard[numero] = ativo;
    setBoard(newBoard);
    setAtivo(ativo === "X" ? "O" : "X");
  }

  function handleNewRound() {
    setBoard(Array(9).fill(null));
    setAtivo("X");
  }

  return (
    <div className="App">
      <h1>Jogo da Velha</h1>
      <Input
        placeholder={"X"}
        label={"Jogador X"}
        value={inputX}
        onChange={(e) => setInputX(e.target.value)}
      />
      <Input
        placeholder={"O"}
        label={"Jogador O"}
        value={inputO}
        onChange={(e) => setInputO(e.target.value)}
      />
      <Jogo
        onClick={(numero) => {
          handleOnClick(numero);
        }}
        xbola={ativo}
        board={board}
        jogadorX={inputX}
        jogadorO={inputO}
        onNewRound={handleNewRound}
      />
    </div>
  );
}

export default App;

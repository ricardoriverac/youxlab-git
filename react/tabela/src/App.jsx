import { useState } from "react";
import "./App.css";
import Jogo from "./components/Jogo";

function App() {
  return (
    <div className="back">
      <div className="containerForm">
        <h1>Jogo da velha</h1>
        <label htmlFor="">Jogador 1</label>
        <input type="text" />
        <label htmlFor="">Jogador 2</label>
        <input type="text" />
        <button className="btn">Jogar</button>
        <Jogo />
      </div>
    </div>
  );
}

export default App;

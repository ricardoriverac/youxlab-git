import { useState, useEffect } from "react";
import "./Jogo.css";
import Placar from "./Placar";
import Botao from "./Botao";
import Box from "@mui/material/Box";
import Div from "@mui/material/Divider";
import Button from "@mui/material/Button";

const Jogo = ({ onClick, xbola, board, jogadorX, jogadorO, onNewRound }) => {
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

  const [modalVisible, setModalVisible] = useState(false);

  const [vitoriasX, setVitoriasX] = useState(0);
  const [vitoriasO, setVitoriasO] = useState(0);

  const pontosX = vitoriasX;
  const pontosO = vitoriasO;

  const vencedor = posicoes.reduce((ac, [a, b, c]) => {
    if (ac) return ac;
    if (board[a] && board[a] === board[b] && board[a] === board[c]) {
      return board[a];
    }
    return null;
  }, null);

  useEffect(() => {
    if (vencedor) {
      if (vencedor === "X") {
        setVitoriasX((prev) => prev + 1);
      } else {
        setVitoriasO((prev) => prev + 1);
      }
      setModalVisible(true);
    }
  }, [vencedor]);

  const velha =
    !vencedor && board.every((value) => value !== null && value !== "");

  const status = vencedor
    ? `Vencedor: ${vencedor}`
    : velha
      ? "Velha"
      : `Jogador atual:${xbola}`;

  const refresh = () => {
    setModalVisible(false);
    onNewRound;
  };

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
      <div>
        <Placar
          textX={jogadorX}
          pontosX={pontosX}
          textO={jogadorO}
          pontosO={pontosO}
        />
      </div>

      {modalVisible || velha ? (
        <Box
          sx={{
            width: "100%",
            height: "100%",
            position: "fixed",
            top: "0",
            left: "0",
            backgroundColor: "#000c",
            color: "#fff",
            display: "flex",
            flexDirection: "column",
            justifyContent: "center",
            alignItems: "center",
          }}
        >
          <Div
            sx={{
              backgroundColor: "#000",
              color: "#eee",
              width: "20%",
              height: "10%",
              borderRadius: "15px",
              border: "5px solid #eee",
              padding: "20px",
              fontFamily: "BLinker",
              fontSize: "200%",
              alignItems: "center",
            }}
          >
            {velha
              ? "Velha!"
              : vencedor === "X"
                ? `vencedor: ${jogadorX || "Jogador X"}`
                : `vencedor: ${jogadorO || "Jogador O"}`}
          </Div>
          <Div>
            <Button
              variant="text"
              sx={{
                height: "60px",
                width: "90px",
                fontSize: "larger",
                color: "#fff",
                bgcolor: "#000",
                marginLeft: "100px",
                p: "0",
                border: "1px solid #fff",
                borderRadius: "15px",
                display: "flex",
                right: "50px",
                top: "50px",
              }}
              onClick={() => {
                (refresh(), onNewRound());
              }}
            >
              Ok
            </Button>
          </Div>
        </Box>
      ) : null}
    </>
  );
};

export default Jogo;

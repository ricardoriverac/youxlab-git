import "./Square.css";

function Square({ numero, clicar, board, index }) {

  return (
    <div className="coluna">
      <button className="botao" onClick={() => clicar(numero)}>
        {board}
      </button>
    </div>
  );
}

export default Square;

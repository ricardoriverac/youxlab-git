import React from "react";

function ButtonOpenModal({ text, funcao }) {
  return (
    <button className="btn " onClick={funcao}>
      {text}
    </button>
  );
}

export default ButtonOpenModal;

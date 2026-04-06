import React from "react";
import "./Modal.css";

function ButtonCloseModal({ text, funcao }) {
  return (
    <button className="close-btn " onClick={funcao}>
      {text}
    </button>
  );
}

export default ButtonCloseModal;

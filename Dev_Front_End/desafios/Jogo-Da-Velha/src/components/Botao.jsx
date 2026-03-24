import React from "react";

import "./Botao.css";

const Botao = ({ text, className, onClick }) => {
  return (
    <div>
      <button className={className} onClick={onClick}>{text}</button>
    </div>
  );
};

export default Botao;

import React, { useState } from "react";

function TrocaCor() {
  const [ativo, setAtivo] = useState(false);

  const estilo = {
    backgroundColor: ativo ? "#444" : "#889",
    color: ativo ? "#889" : '#444',
    padding: "8px",
    cursor: "pointer",
  };

  return (
    <button style={estilo} onClick={() => setAtivo(!ativo)}>
      {ativo ? "Ativo" : "Inativo"}
    </button>
  );
}

export default TrocaCor;

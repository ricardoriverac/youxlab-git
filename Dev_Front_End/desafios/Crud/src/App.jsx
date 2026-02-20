import { useState } from "react";
import Table from "./components/table/Table";

function App() {
  // const pessoas = [
  //   { id: 1, nome: "Heron", idade: 17},
  //      { id: 2, nome: "Ana Laura", idade: 16},
  //         { id: 3, nome: "tiburcio", idade: 16}
  // ]

  return (
    <>
      <h1>Tabela Pessoas</h1>
      <Table />
    </>
  );
}

export default App;

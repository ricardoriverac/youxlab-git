import NavBar from "./componets/NavBar.jsx";

import { Route, Router, Routes } from "react-router-dom";
import "./App.css";
import Home from "./routes/Home.jsx";

function App() {
  return (
    <>
      <Home />
      <NavBar />
    </>
  );
}

export default App;

// import React, { useState } from "react";

// function App() {
//   // let is2Numero = 90;
//   const [isNumero, setIsNumero] = useState(0);
//   return (
//     <div>
//       <button
//         onClick={() => {
//           setIsNumero(isNumero + 1);
//           // is2Numero = is2Numero + 1;
//           // console.log(is2Numero);
//         }}
//       >
//         Aumentar
//       </button>
//       {console.log(isNumero)}
//       <h1>{isNumero}</h1>
//     </div>
//   );
// }
// export default App;

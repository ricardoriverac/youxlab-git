import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Home from "./componentes/pages/Home";
import Empresa from "./componentes/pages/Empresa";
import Contato from "./componentes/pages/Contato";

function App() {
  return (
    <div>
      <Router>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/empresa" element={<Empresa />} />
          <Route path="/contato" element={<Contato />} />
        </Routes>
      </Router>
    </div>
  );
}

export default App;

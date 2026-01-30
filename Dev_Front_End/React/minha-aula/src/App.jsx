import { BrowserRouter as Router, Routes, Route, Link } from "react-router-dom";
import Navbar from "./components/layout/Navbar";
import Footer from "./components/layout/Footer";
import Home from "./pages/Home";
import Contato from "./pages/Contato";
import Empresa from "./pages/Empresa";

function App() {
  return (
    <Router>
      <Navbar />
      <Routes>
        <Route className="link" path="/" element={<Home />} />
        <Route className="link" path="/contato" element={<Contato />} />
        <Route className="link" path="/empresa" element={<Empresa />} />
      </Routes>
      <Footer />
    </Router>
  );
}

export default App;

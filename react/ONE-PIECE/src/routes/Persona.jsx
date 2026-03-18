import { useState, useEffect } from "react";
import BotaoVoltar from "../componets/BotaoNavegar";
import "./Persona.css";
import Card from "../componets/Card";
import api from "../services/api";

function Persona() {
  const [dados, setDados] = useState([]);
  const [loading, setLoading] = useState(true);

  const piece = async () => {
    try {
      const response = await api.get("");
      setDados(response.data);
    } catch (error) {
      console.log(error);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    piece();
  }, []);

  if (loading) {
    return (
      <div className="loading">
        <img className="spiner" src="src/image/loading.svg" alt="loading" />
      </div>
    );
  }

  return (
    <>
      <div className="cards-container">
        {dados.slice(0, 10).map((e) => (
          <Card key={e.id} character={e} />
        ))}
      </div>

      <BotaoVoltar className="close" text={"Voltar"} link={"/"} />
    </>
  );
}

export default Persona;

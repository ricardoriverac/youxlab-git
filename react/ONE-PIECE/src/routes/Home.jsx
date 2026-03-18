import { useEffect, useState } from "react";
import axios from "axios";
import "./Home.css";

function Home() {
  const [characters, setCharacters] = useState([]);

  useEffect(() => {
    axios
      .get("https://api.api-onepiece.com/v2/characters/en")
      .then((response) => {
        setCharacters(response.data);
      })
      .catch((error) => {
        console.log(error);
      });
  }, []);

  return (
    <div className="home">
      <img className="img" src="src/assets/logo.png" alt="logo.png" />

      <div className="col">
        <div className="col">
          SÉCULO PERDIDO BR
          <h6>
            One Piece é uma história sobre aventura, amizade e liberdade. A
            trama acompanha Monkey D. Luffy, um jovem pirata que sonha em
            encontrar o lendário tesouro chamado One Piece e se tornar o Rei dos
            Piratas. Para isso, ele reúne uma tripulação chamada Chapéus de
            Palha e viaja pelos mares enfrentando inimigos poderosos, governos
            corruptos e desafios perigosos.
          </h6>
        </div>
      </div>

      <div className="zoro">
        <img className="img2" src="src/assets/enel.png" alt="enel.png" />
        <img className="img3" src="src/assets/jimbe.png" alt="jimbe.png" />
      </div>
    </div>
  );
}

export default Home;

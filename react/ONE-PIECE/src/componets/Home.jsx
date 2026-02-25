import { Link } from "react-router-dom";

import "./Home.css";

function Home() {
  return (
    <div className="home">
      <img className="img" src="src/assets/logo.png" alt="logo.png" />
      <div className="col">
        <div className="col">
          ONE PIECE BR
          <h6>
            **One Piece** é uma história sobre aventura, amizade e liberdade. A
            trama acompanha **Monkey D. Luffy**, um jovem pirata que sonha em
            encontrar o lendário tesouro chamado *One Piece* e se tornar o Rei
            dos Piratas. Para isso, ele reúne uma tripulação chamada **Chapéus
            de Palha** e viaja pelos mares enfrentando inimigos poderosos,
            governos corruptos e desafios perigosos. Ao longo da jornada, cada
            personagem tem seus próprios sonhos, e a série destaca valores como
            lealdade, coragem e nunca desistir dos seus objetivos.
          </h6>
        </div>
      </div>
      <div className="zoro">
        <img className="img2" src="src/assets/enel.png" alt="enel.png" />
      </div>
      <div className="link">
        
      </div>
    </div>
  );
}

export default Home;

import { Link } from "react-router-dom";
import "./NavBar.css";
import BotaoNavegar from "./BotaoNavegar";

function NavBar() {
  return (
    <nav className="nav">
      <ul>
        <li>
          <BotaoNavegar
            className="persona"
            text={"Aba de Personagens"}
            link={"/persona"}
          ></BotaoNavegar>
        </li>
      </ul>
    </nav>
  );
}

export default NavBar;

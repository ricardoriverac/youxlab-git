import { useNavigate } from "react-router-dom";
import "./BotaoNavegar.css";

function BotaoNavegar({ text, link }) {
  const navigate = useNavigate();

  return (
    <button className="btn" onClick={() => navigate(link)}>
      {text}
    </button>
  );
}

export default BotaoNavegar;

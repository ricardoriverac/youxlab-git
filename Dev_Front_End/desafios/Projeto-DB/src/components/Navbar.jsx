import { Link } from "react-router-dom";

import "./Navbar.css";

const Navbar = () => {
  return (
    <nav className="navbar">
      <h2>
        <Link to={`/`}>
          <img className="logo" src="/dragonball.png" alt="dragonball" />
        </Link>
      </h2>
      <h2>
        <img className="title" src="src/assets/db.png" alt="DBS" />
      </h2>
    </nav>
  );
};

export default Navbar;

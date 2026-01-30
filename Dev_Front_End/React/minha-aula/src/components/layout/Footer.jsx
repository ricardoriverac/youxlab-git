import { FaPlaystation, FaXbox, FaSteam } from "react-icons/fa";

import styles from './Footer.module.css'

function Footer() {
  return (
    <footer>
        <ul className={styles.gameList}>
            <li className="ps"><FaPlaystation id="ps"/></li>
            <li className="xb"><FaXbox id="xb"/></li>
            <li className="st"><FaSteam id="st"/></li>
        </ul>
        <p>Nosso rodapé</p>
    </footer>
  );
}

export default Footer;

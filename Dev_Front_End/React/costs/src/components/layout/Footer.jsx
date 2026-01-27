import { FaFacebook, FaInstagram, FaLinkedin } from "react-icons/fa";

import styles from "./Footer.module.css";
import { Link } from "react-router-dom";

function Footer() {
  return (
    <footer className={styles.footer}>
      <ul className={styles.socialList}>
        <li>
          <Link className={styles.socialLink} to="https://facebook.com" target="_blank"><FaFacebook /></Link>
        </li>
        <li>
          <Link className={styles.socialLink} to="https://instagram.com" target="_blank"><FaInstagram /></Link>
        </li>
        <li>
          <Link className={styles.socialLink} to="https://linkedin.com" target="_blank"><FaLinkedin /></Link>
        </li>
      </ul>
      <p className={styles.copyright}>
        <span>Costs</span> &copy; 2026
      </p>
    </footer>
  );
}

export default Footer;

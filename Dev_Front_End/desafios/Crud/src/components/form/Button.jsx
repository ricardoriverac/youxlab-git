import styles from "./Button.module.css";

function Button({ onClick, text, type }) {
  return (
    <>
      <button onClick={onClick} type={type} className={styles.btn}>{text}</button>
    </>
  );
}

export default Button;

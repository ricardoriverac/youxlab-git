import styles from './Frase.module.css'

function Frase() {
  return (
    <div className={styles.fraseContainer}>
      <p className={styles.fraseContent}>Este é um componente com uma frase!</p>
      <p>E esse componente é outra</p>
    </div>
  );
}

export default Frase;

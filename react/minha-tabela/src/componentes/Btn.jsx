import styles from './Btn.module.css'

function Btn({text, funcao}) {
    return (
        <div>
            <button onClick={funcao} className={styles.btn}>
                {text}
            </button>
        </div>
    )
}

export default Btn
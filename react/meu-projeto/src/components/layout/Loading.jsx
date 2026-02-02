import loading from '../../img/loading.svg'

import styles from './Loading.module.css'

function Loanding() {
    return (
        <div className={styles.loader_container}>
            <img  className={styles.loader} src={loading} alt="Loading" />
        </div>
    )
}

export default Loanding
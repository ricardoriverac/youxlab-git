import styles from "./TableHead.module.css";

function TableHead({ th1, th2, th3, th4, th5 }) {
  return (
    <thead>
      <tr>
        <th className={styles.tableHead}>{th1}</th>
        <th className={styles.tableHead}>{th2}</th>
        <th className={styles.tableHead}>{th3}</th>
        <th className={styles.tableHead}>{th4}</th>
        <th className={styles.tableHead}>{th5}</th>
      </tr>
    </thead>
  );
}

export default TableHead;

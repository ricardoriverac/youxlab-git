import styles from "./Input.module.css";

function Input({ value, name, type, placeholder, label, onChange }) {
  return (
    <div className={styles.form}>
      <label>{label}</label>
      <input
        value={value}
        type={type}
        placeholder={placeholder}
        id={name}
        onChange={onChange}
      />
    </div>
  );
}

export default Input;

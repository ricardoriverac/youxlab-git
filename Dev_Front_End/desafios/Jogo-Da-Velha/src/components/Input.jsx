import "./Input.css";

const Input = ({ label, placeholder, value, onChange }) => {
  return (
    <>
      <label className="label">{label}</label>
      <input placeholder={placeholder} className="cadastro" type="text" value={value} onChange={onChange}/>
    </>
  );
};

export default Input;

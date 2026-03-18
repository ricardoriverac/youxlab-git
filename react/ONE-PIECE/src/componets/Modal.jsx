import "./Modal.css";
import ButtonCloseModal from "./ButtonCloseModal";

function Modal({ character, fecharModal }) {
  if (!character) return null;

  const { name, job, age, size, bounty, status, fruit, crew } = character;

  return (
    <div className="modal" onClick={fecharModal}>
      <div className="modal-container" onClick={(e) => e.stopPropagation()}>
        <ButtonCloseModal text={"X"} funcao={fecharModal} />
        <h2>{name}</h2>
        <p>
          <strong>Cargo: {job} </strong>
        </p>
        <p>
          <strong>Idade: {age} </strong>
        </p>
        <p>
          <strong>Altura: {size} </strong>
        </p>
        <p>
          <strong>Recompensa: {bounty} </strong>
        </p>
        <p>
          <strong>Status: {status} </strong>
        </p>

        <p>
          <strong>Fruta: {fruit?.roman_name || "Sem fruta"} </strong>
        </p>
        <p>
          <strong>Tipo: {fruit?.type || "—"} </strong>
        </p>
        <p>
          <strong>Tripulação: {crew?.name} </strong>
        </p>
      </div>
    </div>
  );
}

export default Modal;

import "./Modal.css";
import ButtonCloseModal from "./ButtonCloseModal";

function Modal2({ fecharModal, vencedor}) {
  return (
    <div className="modal" onClick={fecharModal}>
      <div className="modal-container" onClick={(e) => e.stopPropagation()}>
        <ButtonCloseModal text={"X"} funcao={fecharModal} />
        <div className="message1">
          <p>
            {vencedor}
          </p>
        </div>
      </div>
    </div>
  );
}

export default Modal2;

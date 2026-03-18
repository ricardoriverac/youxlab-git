import { useState } from "react";
import "./Card.css";
import Modal from "./Modal";
import ButtonOpenModal from "./ButtonOpenModal";

function Card({ character }) {
  const { name, job, bounty } = character;

  const [isModalOpen, setIsModalOpen] = useState(false);

  function abrirModal() {
    setIsModalOpen(true);
    console.log("isModalOpen :>> ", isModalOpen);
  }

  function fecharModal() {
    setIsModalOpen(false);
  }

  return (
    <div className="card">
      <h3>{name}</h3>

      <p>
        <strong>Cargo: {job} </strong>
      </p>
      <p>
        <strong>Recompensa: {bounty} </strong>
      </p>
      <ButtonOpenModal
        text={"Ver mais informações do personagem"}
        funcao={abrirModal}
      />
      {isModalOpen && <Modal character={character} fecharModal={fecharModal} />}
    </div>
  );
}

export default Card;

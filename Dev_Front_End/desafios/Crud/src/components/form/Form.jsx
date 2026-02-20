import { useEffect, useState } from "react";
import Input from "./Input";
import Button from "./Button";

import styles from "./Form.module.css";

function Form({ valor, editando }) {
  const [formData, setFormData] = useState({
    nome: "",
    telefone: "",
    cpf: "",
    email: "",
  });

  useEffect(() => {
    setFormData({
      nome: valor.nome || "",
      telefone: valor.telefone || "",
      cpf: valor.cpf || "",
      email: valor.email || "",
    });
  }, [valor]);

  const handleChangeNome = (e) => {
    setFormData((prevData) => ({
      ...prevData,
      nome: e.target.value,
    }));
  };

  const handleChangeTelefone = (e) => {
    setFormData((prevData) => ({
      ...prevData,
      telefone: e.target.value,
    }));
  };

  const handleChangeCpf = (e) => {
    setFormData((prevData) => ({
      ...prevData,
      cpf: e.target.value,
    }));
  };

  const handleChangeEmail = (e) => {
    setFormData((prevData) => ({
      ...prevData,
      email: e.target.value,
    }));
  };

  const handleSubmit = () => {
    if (
      formData.nome.trim() === "" ||
      formData.telefone.trim() === "" ||
      formData.cpf.trim() === "" ||
      formData.email.trim() === ""
    ) {
      alert("Preencha todos os campos");
      return;
    }
    if (editando === false) {
      fetch("http://localhost:5000/people", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(formData),
      })
        .then((resp) => resp.json())
        .then((data) => {
          console.log("data", data);
        })
        .catch((err) => console.log(err));
    } else {
      fetch(`http://localhost:5000/people/${valor.id}`, {
        method: "PUT",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(formData),
      })
        .then((response) => response.json())
        .then((data) => console.log(data))
        .catch((error) => console.error("Erro:", error));
    }
    editando = true;
  };

  return (
    <>
      <form onSubmit={handleSubmit}>
        <Input
          type="text"
          label="Nome:"
          name="nome"
          value={formData.nome}
          onChange={handleChangeNome}
          placeholder="Digite seu nome"
        />
        <Input
          type="number"
          label="Telefone:"
          name="telefone"
          value={formData.telefone}
          onChange={handleChangeTelefone}
          placeholder="Digite seu telefone"
        />
        <Input
          type="number"
          label="Cpf:"
          name="cpf"
          value={formData.cpf}
          onChange={handleChangeCpf}
          placeholder="Digite seu cpf"
        />
        <Input
          type="email"
          label="Email:"
          name="email"
          value={formData.email}
          onChange={handleChangeEmail}
          placeholder="Digite seu email"
        />
        <Button type="submit" text="Inserir" />
      </form>
    </>
  );
}

export default Form;

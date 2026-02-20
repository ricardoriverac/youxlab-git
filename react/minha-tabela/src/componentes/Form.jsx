import { useState, useEffect } from "react";

import styles from "./Form.module.css";
import style from "./Input.module.css";
import cor from "./Label.module.css";
import Btn from "./Btn";
import Tabela from "./Tabela";

function Form() {
  const [formDados, setFormDados] = useState({
    nome: "",
    telefone: "",
    cpf: "",
    email: "",
  });

  const [dados, setDados] = useState([]);

  const handleChangeNome = (e) => {
    setFormDados((prevData) => ({
      ...prevData,
      nome: e.target.value,
    }));
  };
  const handleChangeTelefone = (e) => {
    setFormDados((prevData) => ({
      ...prevData,
      telefone: e.target.value,
    }));
  };
  const handleChangeCpf = (e) => {
    setFormDados((prevData) => ({
      ...prevData,
      cpf: e.target.value,
    }));
  };
  const handleChangeEmail = (e) => {
    setFormDados((prevData) => ({
      ...prevData,
      email: e.target.value,
    }));
  };

  const remove = (id) => {
    fetch(`http://localhost:5000/dadosPessoas/${id}`, {
      method: "DELETE",
      headers: {
        "Content-Type": "application/json",
      },

      body: JSON.stringify(id),
    })
      .then((resp) => resp.json())
      .then(() => {
        const novaLista = dados.filter((pessoa) => pessoa.id !== id);  //criei uma lista sem a pessoa com o id que foi passado
        setDados(novaLista);
      })
      .catch((err) => console.log(err));
  };

  function inserirPessoa() {
    fetch("http://localhost:5000/dadosPessoas", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(formDados),
    })
      .then((resp) => resp.json())
      .then((novaPessoa) => {
        setDados([...dados, novaPessoa]);
      })
      .catch((err) => console.log(err));

    setFormDados({
      nome: "",
      telefone: "",
      cpf: "",
      email: "",
    });
  }

  useEffect(() => {
    fetch("http://localhost:5000/dadosPessoas", {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
      },
    })
      .then((resp) => resp.json())
      .then((data) => {
        setDados(data);
      })
      .catch((err) => console.log(err));
  }, []);

  return (
    <>
      <div className={styles.form}>
        <label className={cor.label}>
          Nome:
          <input
            className={style.formInput}
            type="text"
            onChange={handleChangeNome}
            value={formDados.nome}
          />
        </label>
        <label className={cor.label}>
          Telefone:
          <input
            className={style.formInput}
            type="number"
            onChange={handleChangeTelefone}
            value={formDados.telefone}
          />
        </label>
        <label className={cor.label}>
          CPF:
          <input
            className={style.formInput}
            type="number"
            onChange={handleChangeCpf}
            value={formDados.cpf}
          />
        </label>
        <label className={cor.label}>
          Email:
          <input
            className={style.formInput}
            type="text"
            onChange={handleChangeEmail}
            value={formDados.email}
          />
        </label>
        <Btn text="Inserir" funcao={inserirPessoa} />
      </div>

      <Tabela
        th1="NOME"
        th2="TELEFONE"
        th3="CPF"
        th4="EMAIL"
        th5="AÇÕES"
        dados={dados}
        remover={remove}
      />
    </>
  );
}

export default Form;

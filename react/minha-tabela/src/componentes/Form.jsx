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

  const [editar, setEditar] = useState("");
  const [isEditar, setIsEditar] = useState(null);

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
    setEditando;
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
        const novaLista = dados.filter((pessoa) => pessoa.id !== id); //criei uma lista sem a pessoa com o id que foi passado
        setDados(novaLista);
      })
      .catch((err) => console.log(err));
  };

  function limparFormulario() {
  setFormDados({
    nome: "",
    telefone: "",
    cpf: "",
    email: "",
  });
}

  function editarPessoa(pessoa) {
  setFormDados({
    nome: pessoa.nome,
    telefone: pessoa.telefone,
    cpf: pessoa.cpf,
    email: pessoa.email,
  });

  setEditar(pessoa.id);
  setIsEditar(true);
}

  function salvarPessoa() {
    if (
      formDados.nome === "" ||
      formDados.telefone === "" ||
      formDados.cpf === "" ||
      formDados.email === ""
    ) {
      alert("Preencha todas as informações");
      return;
    }

    // SE estiver editando
    if (isEditar) {
      fetch(`http://localhost:5000/dadosPessoas/${editar}`, {
        method: "PUT",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(formDados),
      })
        .then((resp) => resp.json())
        .then((pessoaAtualizada) => {
          const novaLista = dados.map((pessoa) =>
            pessoa.id === editar ? pessoaAtualizada : pessoa,
          );

          setDados(novaLista);
          setIsEditar(false);
          setEditar("");
          limparFormulario();
        })
        .catch((err) => console.log(err));
    } else {
      // SE for cadastro novo
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
          limparFormulario();
        })
        .catch((err) => console.log(err));
    }
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
        <Btn text={isEditar ? "Salvar" : "Inserir"} funcao={salvarPessoa} />
      </div>

      <Tabela
        th1="NOME"
        th2="TELEFONE"
        th3="CPF"
        th4="EMAIL"
        th5="AÇÕES"
        dados={dados}
        remover={remove}
        editar={editarPessoa}
      />
    </>
  );
}

export default Form;

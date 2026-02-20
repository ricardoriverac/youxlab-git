import { useEffect, useState } from "react";
import Button from "../form/Button";
import styles from "./Table.module.css";
import TableHead from "./TableHead.jsx";
import Form from "../form/Form.jsx";

function Table() {
  // PASSAR DADOS PRA TABLE
  const [dados, setDados] = useState([]);
  const [eDados, setEDados] = useState([]);
  const [editando, setEditando] = useState(false);

  useEffect(() => {
    fetch("http://localhost:5000/people", {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
      },
    })
      .then((resp) => resp.json())
      .then((data) => {
        setDados(data);
        console.log(dados);
        console.log(data);
      })
      .catch((err) => console.log(err));
  }, []);

  // const apagar = () => {
  //   console.log('object');
  //   fetch(`http://localhost:5000/people/4114`, {
  //     method: "DELETE",
  //     headers: {
  //       "Content-Typer": "application/json",
  //     },
  //   })
  //     .then((resp) => resp.json())
  //     .then((data) => {
  //       setDados(dados.filter((dados) => dados.id !== id));
  //       console.log(data);
  //     })
  //     .catch((err) => console.log(err));
  // };

  const carregar = () => {
    window.location.reload();
  };

  const apagar = (id) => {
    fetch(`http://localhost:5000/people/${id}`, {
      method: "DELETE",
      headers: {
        "Content-Type": "application/json",
      },
    })
      .then((resp) => resp.json())
      .then(() => {
        setDados((prevDados) => prevDados.filter((item) => item.id !== id));
      })
      .catch((err) => console.log(err));
  };

  const editor = (e) => {
    // console.log("e :>> ", e);
    setEDados(e);
    setEditando(true);
  };

  // const editar = (id) => {
  //   fetch(`http://localhost:5000/people/${id}`, {
  //     method: "PUT",
  //     headers: {
  //       "Content-Type": "application/json",
  //     },
  //   })
  //     .then((resp) => resp.json())
  //     .then(() => {
  //       setDados((prevDados) => prevDados.filter((item) => item.id !== id));
  //     })
  //     .catch((err) => console.log(err));
  // };

  return (
    <>
      <Form valor={eDados} editando={editando}/>
      <table>
        <TableHead
          th1="Nome"
          th2="Telefone"
          th3="Cpf"
          th4="Email"
          th5="Ações"
        />
        <tbody>
          {dados.map((pessoa) => {
            return (
              <tr key={pessoa.id}>
                <td>{pessoa.nome}</td>
                <td>{pessoa.telefone}</td>
                <td>{pessoa.cpf}</td>
                <td>{pessoa.email}</td>
                <td>
                  <Button
                    onClick={() => editor(pessoa)}
                    type="submit"
                    text="Editar"
                  />
                  <Button
                    onClick={() => apagar(pessoa.id)}
                    type="submit"
                    text="Apagar"
                  />
                </td>
              </tr>
            );
          })}
        </tbody>
      </table>
    </>
  );
}

export default Table;

import styles from "./Tabela.module.css";
import Btn from "./Btn";

function Tabela({ th1, th2, th3, th4, th5, dados, remover, editar }) {
  return (
    <div>
      <table>
        <thead>
          <tr>
            <th>{th1}</th>
            <th>{th2}</th>
            <th>{th3}</th>
            <th>{th4}</th>
            <th>{th5}</th>
          </tr>
        </thead>

        <tbody>
          {Array.isArray(dados) &&
            dados.map((pessoa) => (
              <tr key={pessoa.id}>
                <td>{pessoa.nome}</td>
                <td>{pessoa.telefone}</td>
                <td>{pessoa.cpf}</td>
                <td>{pessoa.email}</td>
                <td className={styles.botao}>
                  <Btn text="Remover" funcao={() => remover(pessoa.id)} />
                  <Btn text="Editar" funcao={() => editar(pessoa)}/>
                </td>
              </tr>
            ))}
        </tbody>
      </table>
    </div>
  );
}

export default Tabela;

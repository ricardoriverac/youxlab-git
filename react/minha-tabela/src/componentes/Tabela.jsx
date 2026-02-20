import styles from "./Tabela.module.css";
import Btn from "./Btn";

function Tabela({ th1, th2, th3, th4, th5, dados, remover }) {
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
            dados.map((e) => (
              <tr key={e.id}>
                <td>{e.nome}</td>
                <td>{e.telefone}</td>
                <td>{e.cpf}</td>
                <td>{e.email}</td>
                <td className={styles.botao}>
                  <Btn text="Remover" funcao={() => remover(e.id)} />
                  <Btn text="Editar" />
                </td>
              </tr>
            ))}
        </tbody>
      </table>
    </div>
  );
}

export default Tabela;

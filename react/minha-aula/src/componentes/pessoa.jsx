function Pessoa({nome, idade, profissao, foto}) {
    return (
        <div>
            <img src={foto} alt={nome} className="cr7"/>
            <h2>Nome: {nome}</h2>
            <p>Idade: {idade}</p>
            <p>Profissão: {profissao}</p>
        </div>
    )
}

export default Pessoa

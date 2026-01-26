function Saudacao({ nome }) {

    function gerarSaudação(algumNome) {
        return `Olá ${algumNome}, tudo bem?`
    }

    return (<>{nome && <p>{gerarSaudação(nome)}</p>}</>
    )
}

export default Saudacao
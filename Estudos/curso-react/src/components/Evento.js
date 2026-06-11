import { getDefaultNormalizer } from "@testing-library/dom"

function Evento({numero}) {

    function meuEvento() {
        console.log(`Opa, foi ativado! ${numero}`)
    }
    
    return(
        <div>
            <p>CLique para disparar um evento: </p>
            <button onClick={meuEvento}> Ativar|</button>
        </div>
    )
}

export default Evento;
import Button from "./eventos/Button"
function Evento() {

    function meuEvento() {
        console.log(`Ativando primeiro evento`)
    }

    function segundoEvento() {
        console.log("Ativndo o segundo evento")
    }

    return (
        <div>
            <p>CLique para disparar um evento: </p>
            <Button  event={meuEvento} text="Primeiro evento" />
            <Button event={segundoEvento} text="Segundo evento" />
        </div>
    )
}

export default Evento
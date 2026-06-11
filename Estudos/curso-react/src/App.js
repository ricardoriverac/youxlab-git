import './App.css'
import HelloWorld from './components/HelloWorld'
import SayMyName from './components/SayMyName';
import Pessoa from './components/Pessoa';
import Frase from './components/Frase'
function App() {

  const nome = "Maria"
  return (
    <div className='App'>
      <Frase />
      <Frase />
      <SayMyName nome='Pedro' />
      <SayMyName nome='Couto' />
      <SayMyName nome={nome} />
      <Pessoa nome="Rodrigo" idade="28" profissao="Programador" />
    </div>
  )
}

export default App;
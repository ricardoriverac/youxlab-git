import './App.css'
import HelloWorld from './components/HelloWorld'
import SayMyName from './components/SayMyName';
import Pessoa from './components/Pessoa';
function App() {

  const nome = "Maria"
  return (
    <div className='App'>
      <HelloWorld />
      <SayMyName nome='Pedro' />
      <SayMyName nome='Couto' />
      <SayMyName nome={nome} />
      <Pessoa nome="Rodrigo" idade="28" profissao="Programador" />
    </div>
  )
}

export default App;
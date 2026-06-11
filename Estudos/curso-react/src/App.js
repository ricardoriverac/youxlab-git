import './App.css'
import HelloWorld from './components/HelloWorld'
import SayMyName from './components/SayMyName';
import Pessoa from './components/Pessoa';
import Frase from './components/Frase'
import List  from './components/List';
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
      <List />
    </div>
  )
}

export default App;
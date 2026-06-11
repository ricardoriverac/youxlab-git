import './App.css'
import Condicional from './components/Condicional';
import Evento from './components/Evento'
import Form from './components/Form';
import OutraLIsta from './components/OutraLIsta';
function App() {

  const meusItens = ['React', 'Vue', 'Angular']

  return (
  <div className='App'>
    <h1>Renderização de listas</h1>
    <OutraLIsta  itens={meusItens}/>
  </div>
  )
}

export default App;
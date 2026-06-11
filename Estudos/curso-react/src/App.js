import './App.css'
import HelloWorld from './components/HelloWorld'
function App(){
  const name = 'Pedro'

  const newName = name.toUpperCase()

  function sum(a,b){
    return a + b
  }

  const url = "https://institutoyoux.org.br/wp-content/uploads/2025/07/textur.png"
  return (
    <div className='App'>
      <h2>Alterando o JSX</h2>
      <p>Olá, {newName}</p>
      <p>Soma: {sum(1, 2)}</p>
      <img src={url} alt="Minha imagem" />
      <HelloWorld />
    </div>
  )
}

export default App;
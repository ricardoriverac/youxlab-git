import { useState } from "react";
import "./App.css";
import Modal from "./componets/Modal";

function App() {
  const [isModalVisible, setIsModalVisible] = useState(false);

  return (
    <>
      <div className="App">
        <button onClick={() => setIsModalVisible(true)}>Open</button>
        {isModalVisible ? (
          <Modal>
            <h2>Modal do App</h2>
          </Modal>
        ) : null}
        {/* 👇 Pode ser desse jeito tambem
        {isModalVisible ? <h1>Modal</h1> : null} */}
      </div>
    </>
  );
}

export default App;

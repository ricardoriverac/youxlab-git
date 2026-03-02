function Modal({ children }) {
  return (
    // 👇 Esse deixa o fundo preto transparente 
    <div className="modal">
      {/* 👇 Esse vai fazer a modal aparecer */}
      <div className="container">
        <button className="close">close</button>
        <div className="content">{children}</div>
      </div>
    </div>
  );
}

export default Modal;

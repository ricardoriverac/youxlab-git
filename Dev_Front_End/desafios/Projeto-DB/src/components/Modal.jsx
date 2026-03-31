const Modal = ({ id="modal", children, onClose = () => {} }) => {

    const handleOutsideClick = (e) => {
        if(e.target.id == id) onClose();
    }

  return (
    <div id={id} className="modal" onClick={handleOutsideClick}>
      <div className="modal-container">
        <button className="close" onClick={onClose}/>
        <div className="content">{children}</div>
      </div>
    </div>
  );
};

export default Modal;

import "./Placar.css"

const Placar = ({ textX, pontosX, textO, pontosO }) => {
  return (
    <div className="placar">
      <h1>
        {textX}: {pontosX}
      </h1>
      <h1>
        {textO}: {pontosO}
      </h1>
    </div>
  );
};

export default Placar;

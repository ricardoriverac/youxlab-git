const Placar = ({ textX, pontosX, textO, pontosO }) => {
  return (
    <div>
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

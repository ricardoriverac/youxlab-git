import { useEffect, useState } from "react";
import "./Card.css";
import Modal from "./Modal";
import dbFetch from "../axios/api";
import FormCard from "./FormCard";

const Card = ({
  id,
  name,
  race,
  affiliation,
  gender,
  image,
  ki,
  maxKi,
  description,
}) => {
  const [modalVisible, setModalVisible] = useState(false);

  const [transformations, setTransformations] = useState();

  const getData = async () => {
    try {
      const response = await dbFetch.get(`/characters/${id}`);

      const data = response.data.transformations;

      console.log(data);
      setTransformations(data);
    } catch (error) {
      console.log(error);
    }
  };

  useEffect(() => {
    getData();
  }, []);

  return (
    <div className="box">
      <h1 className="name">{name}</h1>
      <h2 className="race">{race}</h2>
      <h2>{gender}</h2>
      <h2 className="affiliation">{affiliation}</h2>
      <img className="image" src={image} alt="image" />
      <h2 className="ki">{ki}</h2>
      <h2 className="maxki">{maxKi}</h2>
      <button className="btn" onClick={() => setModalVisible(true)}>
        Descrição
      </button>
      {modalVisible ? (
        <Modal onClose={() => setModalVisible(false)}>
          <h3 className="description">{description}</h3>
          {transformations != 0 ? <h4>Forms:</h4> : null}
          <div className="manyBox">
            {transformations.map((form) => {
              return (
                <div key={form.id}>
                  <FormCard
                    id={id}
                    name={form.name}
                    image={form.image}
                    ki={form.ki}
                  />
                </div>
              );
            })}
          </div>
        </Modal>
      ) : null}
    </div>
  );
};

export default Card;

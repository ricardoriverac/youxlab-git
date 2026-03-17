import dbFetch from "../axios/api";

import Card from "../components/Card";
import { useEffect, useState } from "react";

const Characters = ({ endpoint = "page=1&limit=58" }) => {
  const [characters, setCharacters] = useState([]);
  console.log(endpoint);
  const getData = async () => {
    try {
      const response = await dbFetch.get(`/characters?${endpoint}`);

      let data;
      if (!!response.data.items) {
        data = response.data.items;
      } else {
        data = response.data;
      }

      console.log(data);
      setCharacters(data);
    } catch (error) {
      console.log(error);
    }
  };

  useEffect(() => {
    getData();
  }, [endpoint]);

  return (
    <>
      <div className="charactersPage">
        <h1>Characters</h1>
        {characters.length === 0 ? (
          <h1>Vazio até futura atualização...</h1>
        ) : (
          characters.map((characters) => {
            return (
              <div key={characters.id}>
                <Card
                  id={characters.id}
                  name={characters.name}
                  gender={characters.gender}
                  race={characters.race}
                  affiliation={characters.affiliation}
                  image={characters.image}
                  ki={characters.ki}
                  maxKi={characters.maxKi}
                  description={characters.description}
                />
              </div>
            );
          })
        )}
      </div>
    </>
  );
};

export default Characters;

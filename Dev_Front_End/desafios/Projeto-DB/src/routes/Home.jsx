import Characters from "./Characters";
import { useEffect, useState } from "react";

const Home = () => {
  const [listaGenero, setListaGenero] = useState([]);
  const [listaRaca, setListaRaca] = useState([]);
  const [listaAfiliacao, setListaAfiliacao] = useState([]);

  const deParaGenero = [
    { Todos: "" },
    { masculino: "gender=male&" },
    { feminino: "gender=female&" },
  ];
  const deParaRaca = [
    { Todos: "" },
    { humano: "race=human&" },
    { sayajin: "race=saiyan&" },
    { namekuseijin: "race=namekian&" },
    { majin: "race=majin&" },
    { freeza: "race=frieza race&" },
    { android: "race=android&" },
    { jiren: "race=jiren race&" },
    { deus: "race=god&" },
    { anjo: "race=angel&" },
    { maligno: "race=evil&" },
    { nucleico: "race=nucleico&" },
    { nucleicoBenigno: "race=nucleico benigno&" },
    { desconhecido: "race=unknown&" },
  ];
  const deParaAffiliação = [
    { Todos: "" },
    { Guerreiro_Z: "affiliation=z fighter" },
    { Organizacao_Red_Ribbon: "affiliation=red ribbon army" },
    { Guerreiro_Namekuseijin: "affiliation=namekian warrior" },
    { Freelancer: "affiliation=freelancer" },
    { Tropa_Do_freeza: "affiliation=army of frieza" },
    { Soldados_Do_Orgulho: "affiliation=pride troopers" },
    { Assistente_Do_Vermound: "affiliation=assistant of vermound" },
    { Deus_Da_Destruicao: "affiliation=god" },
    { Assistente_Do_Bills: "affiliation=assistant of beerus" },
    { Vilõo: "affiliation=villain" },
    { Outro: "affiliation=other" },
  ];

  useEffect(() => {
    const generos = deParaGenero.map((e) => {
      const key = Object.keys(e)[0];
      const value = Object.values(e)[0];

      return { key, value };
    });

    const racas = deParaRaca.map((e) => {
      const key = Object.keys(e)[0];
      const value = Object.values(e)[0];

      return { key, value };
    });

    const afiliacoes = deParaAffiliação.map((e) => {
      const key = Object.keys(e)[0];
      const value = Object.values(e)[0];

      return { key, value };
    });

    setListaGenero(generos);
    setListaRaca(racas);
    setListaAfiliacao(afiliacoes);
  }, []);

  const [gender, setGender] = useState("");
  const [race, setRace] = useState("");
  const [affiliation, setAffiliation] = useState("");

  const buildEndpoint = () => {
    return `page=1&limit=58&${gender}${race}${affiliation}`;
  };

  return (
    <>
      <div className="linha">
        <div className="sentence">
          Filter the characters you want to see by: Gender:
          <select
            name="selectGender"
            value={gender}
            onChange={(e) => setGender(e.target.value)}
          >
            {listaGenero.map((g) => {
              return (
                <option key={g.key} value={g.value}>
                  {g.key}
                </option>
              );
            })}
          </select>
          Race:{" "}
          <select
            name="selectRace"
            value={race}
            onChange={(e) => setRace(e.target.value)}
          >
            {listaRaca.map((r) => {
              return (
                <option key={r.key} value={r.value}>
                  {r.key}
                </option>
              );
            })}
          </select>
          Affiliation:{" "}
          <select
            name="selectAffiliation"
            value={affiliation}
            onChange={(e) => setAffiliation(e.target.value)}
          >
            {listaAfiliacao.map((a) => {
              return (
                <option key={a.key} value={a.value}>
                  {a.key}
                </option>
              );
            })}
          </select>
        </div>
      </div>
      <div>
        <Characters endpoint={buildEndpoint()} />
      </div>
    </>
  );
};

export default Home;

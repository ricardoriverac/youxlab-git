import { Link } from "react-router-dom";

const Home = () => {

  const gender = ["", "male", "female"];
  const race = [
    "",
    "human",
    "saiyan",
    "namekian",
    "majin",
    "friezaRace",
    "android",
    "jirenRace",
    "god",
    "angel",
    "evil",
    "nucleico",
    "nucleicoBenigno",
    "unknown",
  ];
  const affiliation = [
    "",
    "z_fighter",
    "red_ribbon_army",
    "namekian_warrior",
    "freelancer",
    "frieza's_army",
    "pride_troopers",
    "vermound's_assistant",
    "g_o_d",
    "beerus'assistant",
    "villain",
    "other",
  ];

  return (
    <div className="linha">
      <div className="sentence">
        Filter the{" "}
        <Link className="link" to={`/all`}>
          Characters
        </Link>{" "}
        you want to see: By Gender:
        <select name="select">
          {gender.map((bg) => (
            <option>{bg}</option>
          ))}
        </select>
        By Race:
        <select name="select">
          {race.map((bg) => (
            <option>{bg}</option>
          ))}
        </select>
        By Affiliation:
        <select name="select">
          {affiliation.map((bg) => (
            <option>{bg}</option>
          ))}
        </select>
      </div>
      <div></div>
    </div>
  );
};

export default Home;

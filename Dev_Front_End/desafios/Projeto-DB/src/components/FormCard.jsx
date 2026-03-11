import { useEffect, useState } from "react";
import "./FormCard.css";
import Modal from "./Modal";
import dbFetch from "../axios/api";

const FormCard = ({ name, image, ki }) => {
  return <div className="formBox">
    <h1 className="formName">{name}</h1>
    <img className="formImage" src={image} alt="image" />
    <h2 className="formKi">{ki}</h2>
  </div>;
};

export default FormCard;

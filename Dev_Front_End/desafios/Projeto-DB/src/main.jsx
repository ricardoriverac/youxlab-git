// import { StrictMode } from 'react'
import { createRoot } from "react-dom/client";
import "./index.css";
import App from "./App.jsx";

import { createBrowserRouter, RouterProvider } from "react-router-dom";

import "./styles.scss";

import Characters from "./routes/Characters.jsx";
import Home from "./routes/Home.jsx";

const pathsElements = [
  {
    path: "/male",
    link: "gender=Male",
  },
  {
    path: "/female",
    link: "gender=Female",
  },
  {
    path: "/human",
    link: "race=Human"
  },
  {
    path: "/saiyan",
    link: "race=Saiyan",
  },
  {
    path: "/namekian",
    link: "race=Namekian",
  },
  {
    path: "/majin",
    link: "race=Majin",
  },
  {
    path: "/friezaRace",
    link: "race=Frieza Race",
  },
  {
    path: "/android",
    link: "race=Android",
  },
  {
    path: "/jirenRace",
    link: "race=Jiren Race",
  },
  {
    path: "/god",
    link: "race=God",
  },
  {
    path: "/angel",
    link: "race=Angel",
  },
  {
    path: "/evil",
    link: "race=Evil",
  },
  {
    path: "/nucleico",
    link: "race=Nucleico",
  },
  {
    path: "/nucleicoBenigno",
    link: "race=Bening Nucleico",
  },
  {
    path: "/unknown",
    link: "race=Unknown",
  },
  {
    path: "/z_fighter",
    link: "affiliation=Z Fighter",
  },
  {
    path: "/red_ribbon_army",
    link: "affiliation=Red Ribbon Army",
  },
  {
    path: "/namekian_warrior",
    link: "affiliation=Namekian Warrior"
  },
  {
    path: "/freelancer",
    link: "affiliation=Freelancer"
  },
  {
    path: "/frieza's_army",
    link: "affiliation=Army of Frieza"
  },
  {
    path: "/pride_troopers",
    link: "affiliation=Pride Troopers"
  },
  {
    path: "/vermound's_assistant",
    link: "affiliation=Assistant of Vermoud"
  },
  {
    path: "/g_o_d",
    link: "affiliation=God"
  },
  {
    path: "/beerus'assistant",
    link: "affiliation=Assistant of Beerus"
  },
  {
    path: "/villain",
    link: "affiliation=Villain"
  },
  {
    path: "/other",
    link: "affiliation=Other"
  }
];

const router = createBrowserRouter([
  {
    element: <App />,
    children: [
      {
        path: "/",
        element: <Home />,
      },
      {
        path: "/all",
        element: <Characters />,
      },
      ...pathsElements.map((e) => ({
        path: e.path,
        element: <Characters endpoint={e.link} />,
      })),
    ],
  },
]);

createRoot(document.getElementById("root")).render(
  // <StrictMode>
  <RouterProvider router={router} />,
  // </StrictMode>,
);

import {
  FaBullseye,
  FaLayerGroup,
  FaBook,
  FaPalette,
  FaFileAlt
} from "react-icons/fa";

import "../styles/Card.css";

function format(text) {

  if (!text) return "-";

  return text
    .replaceAll("_", " ")
    .replace(/\b\w/g, c => c.toUpperCase());

}

function StrategyCard({ strategy }) {

  if (!strategy) return null;

  const items = [
    {
      icon: <FaFileAlt />,
      title: "Topic",
      value: strategy.topic
    },
    {
      icon: <FaBullseye />,
      title: "Goal",
      value: strategy.goal
    },
    {
      icon: <FaBook />,
      title: "Pillar",
      value: strategy.pillar
    },
    {
      icon: <FaPalette />,
      title: "Tone",
      value: strategy.tone
    },
    {
      icon: <FaLayerGroup />,
      title: "Template",
      value: strategy.template
    }
  ];

  return (

    <section className="card">

      <h2>

        <FaLayerGroup />

        Strategy Overview

      </h2>

      <div className="strategy-grid">

        {

          items.map((item,index)=>(

            <div key={index}>

              {item.icon}

              <strong>{item.title}</strong>

              <p>{format(item.value)}</p>

            </div>

          ))

        }

      </div>

    </section>

  );

}

export default StrategyCard;
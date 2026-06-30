import "../styles/Hero.css";
import { FaRobot } from "react-icons/fa";

function Hero() {
  return (
    <section className="hero">
      <div className="version-badge">

          v1.0

          <br/>

          by Apoorv

      </div>

      <div className="badge">

        <FaRobot />

        Multi-Agent AI Platform

      </div>

      <h1>

        JobInGen's AI Content Generator
        "ORCA"

      </h1>

      <p>

        Intelligent content generation powered by
        Planner, Copywriter and Critic Agents.

      </p>

      <div className="chips">

        <span>Planner</span>

        <span>Copywriter</span>

        <span>Critic</span>

        <span>Rewrite</span>

      </div>

    </section>
  );
}

export default Hero;
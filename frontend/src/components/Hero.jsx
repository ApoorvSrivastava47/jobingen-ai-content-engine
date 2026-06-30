import { FaBrain, FaMagic, FaBolt } from "react-icons/fa";
import "../styles/Hero.css";

function Hero() {
  return (
    <section className="hero">

      <div className="hero-badge">
        <span className="status-dot"></span>
        Enterprise Multi-Agent AI Platform
      </div>

      <h1>
        JobInGen's
        <br />
        <span>Intelligent Content Engine</span>
      </h1>

      <h2>ORCA</h2>

      <p>
        Generate premium, high-quality content using a modular
        Multi-Agent AI architecture powered by Planner,
        Copywriter, Critic and Review agents.
      </p>

      <div className="hero-tags">

        <div className="hero-tag">
          <FaBrain />
          Planner Agent
        </div>

        <div className="hero-tag">
          <FaMagic />
          AI Copywriter
        </div>

        <div className="hero-tag">
          <FaBolt />
          Quality Critic
        </div>

      </div>

    </section>
  );
}

export default Hero;
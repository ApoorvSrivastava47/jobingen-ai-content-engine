import {
  FaGithub,
  FaReact,
  FaPython,
  FaServer,
  FaRobot
} from "react-icons/fa";

import "../styles/Footer.css";

function Footer() {

  return (

    <footer className="footer">

      <div className="footer-brand">

        <h2>ORCA</h2>

        <p>

          JobInGen's Intelligent Content Engine

        </p>

      </div>

      <div className="footer-stack">

        <div>

          <FaReact />

          React

        </div>

        <div>

          <FaServer />

          FastAPI

        </div>

        <div>

          <FaRobot />

          Ollama

        </div>

        <div>

          <FaPython />

          Python

        </div>

      </div>

      <div className="footer-bottom">

        <p>

          Designed & Developed by

          <strong> Apoorv Srivastava</strong>

        </p>

        <a

          href="https://github.com/ApoorvSrivastava47"

          target="_blank"

          rel="noreferrer"

        >

          <FaGithub />

          GitHub

        </a>

      </div>

      <small>

        © 2026 ORCA • Multi-Agent AI Content Platform

      </small>

    </footer>

  );

}

export default Footer;
import { FaRobot } from "react-icons/fa";
import "../styles/EmptyState.css";

function EmptyState() {
  return (
    <section className="empty-state">

      <FaRobot className="empty-icon"/>

      <h2>Ready to Generate</h2>

      <p>

        Enter any topic above and experience our
        Multi-Agent AI workflow.

      </p>

      <div className="flow">

        <span>Planner</span>

        →

        <span>Copywriter</span>

        →

        <span>Critic</span>

        →

        <span>Rewrite</span>

      </div>

    </section>
  );
}

export default EmptyState;
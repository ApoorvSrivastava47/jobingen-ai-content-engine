import { FaCheckCircle } from "react-icons/fa";
import "../styles/WorkflowStatus.css";

function WorkflowStatus({ result }) {

  if (!result) return null;

  return (
    <section className="workflow">

      <h2>⚙ AI Workflow</h2>

      <div className="workflow-grid">

        <div className="step">
          <FaCheckCircle />
          <span>Planner Completed</span>
        </div>

        <div className="step">
          <FaCheckCircle />
          <span>Copywriter Completed</span>
        </div>

        <div className="step">
          <FaCheckCircle />
          <span>Critic Completed</span>
        </div>

        <div className="step">
          <FaCheckCircle />
          <span>Rewrite Completed</span>
        </div>

      </div>

    </section>
  );
}

export default WorkflowStatus;
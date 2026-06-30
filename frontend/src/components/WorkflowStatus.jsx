import {
  FaCheckCircle,
  FaArrowRight,
  FaBrain,
  FaPenNib,
  FaSearch,
  FaRocket
} from "react-icons/fa";

import "../styles/WorkflowStatus.css";

function WorkflowStatus({ result }) {

  if (!result) return null;

  const workflow = [
    {
      icon: <FaBrain />,
      title: "Planner",
      desc: "Strategy Created"
    },
    {
      icon: <FaPenNib />,
      title: "Copywriter",
      desc: "Draft Generated"
    },
    {
      icon: <FaSearch />,
      title: "Critic",
      desc: "Quality Checked"
    },
    {
      icon: <FaRocket />,
      title: "Publish",
      desc: "Ready"
    }
  ];

  return (

    <section className="workflow">

      <div className="workflow-header">

        <h2>⚙ AI Workflow</h2>

        <span className="workflow-status">

          <FaCheckCircle />

          Completed

        </span>

      </div>

      <div className="workflow-grid">

        {workflow.map((item, index) => (

          <div className="step" key={index}>

            <div className="step-icon">

              {item.icon}

            </div>

            <h3>{item.title}</h3>

            <p>{item.desc}</p>

            {index !== workflow.length - 1 && (

              <div className="workflow-arrow">

                <FaArrowRight />

              </div>

            )}

          </div>

        ))}

      </div>

    </section>

  );

}

export default WorkflowStatus;
import {
  FaCheckCircle,
  FaRobot,
  FaBrain,
  FaImage,
  FaPenNib,
  FaSearch,
} from "react-icons/fa";

import "../styles/WorkflowStatus.css";

function WorkflowStatus({ result }) {

  if (!result) return null;

  const steps = [

    {
      icon: <FaBrain />,
      title: "Planner Agent",
      status: "Completed",
    },

    {
      icon: <FaPenNib />,
      title: "Copywriter Agent",
      status: "Completed",
    },

    {
      icon: <FaSearch />,
      title: "Critic Agent",
      status: "Completed",
    },

    {
      icon: <FaRobot />,
      title: "Image Prompt Agent",
      status: "Completed",
    },

    {
      icon: <FaImage />,
      title: "Image Generator",
      status: "Completed",
    },

  ];

  return (

    <section className="workflow-card">

      <h2>Workflow Status</h2>

      {

        steps.map((step) => (

          <div
            className="workflow-item"
            key={step.title}
          >

            <div className="workflow-left">

              {step.icon}

              <span>

                {step.title}

              </span>

            </div>

            <div className="workflow-right">

              <FaCheckCircle />

              {step.status}

            </div>

          </div>

        ))

      }

    </section>

  );

}

export default WorkflowStatus;
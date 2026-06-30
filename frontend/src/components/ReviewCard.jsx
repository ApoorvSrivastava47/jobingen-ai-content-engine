import ReactMarkdown from "react-markdown";

import { FaClipboardCheck } from "react-icons/fa";

import "../styles/Card.css";

function ReviewCard({ review }) {

  if (!review) return null;

  return (

    <section className="card">

      <h2>

        <FaClipboardCheck />

        AI Quality Review

      </h2>

      <div className="markdown-body">

        <ReactMarkdown>

          {review}

        </ReactMarkdown>

      </div>

    </section>

  );

}

export default ReviewCard;
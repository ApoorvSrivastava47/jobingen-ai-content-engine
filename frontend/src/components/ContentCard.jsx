import ReactMarkdown from "react-markdown";
import { FaPenNib, FaCopy, FaDownload, FaRedo } from "react-icons/fa";
import "../styles/Card.css";

function ContentCard({ content }) {

  if (!content) return null;

  function copyContent() {
    navigator.clipboard.writeText(content);
    alert("Content copied!");
  }

  function downloadContent() {
    const blob = new Blob([content], { type: "text/plain" });

    const url = URL.createObjectURL(blob);

    const a = document.createElement("a");

    a.href = url;

    a.download = "generated-content.txt";

    a.click();

    URL.revokeObjectURL(url);
  }

  return (
    <section className="card">

      <h2>
        <FaPenNib />
        AI Generated Content
      </h2>

      <div className="markdown-body">
        <ReactMarkdown>
          {content}
        </ReactMarkdown>
      </div>

      <div className="action-bar">

        <button onClick={copyContent}>
          <FaCopy />
          Copy
        </button>

        <button onClick={downloadContent}>
          <FaDownload />
          Download
        </button>

        <button disabled>
          <FaRedo />
          Regenerate
        </button>

      </div>

    </section>
  );
}

export default ContentCard;
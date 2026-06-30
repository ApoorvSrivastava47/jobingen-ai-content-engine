import { useState } from "react";
import "../styles/TopicInput.css";
import { generateContent } from "../services/api";

function TopicInput({ onGenerate }) {
  const [topic, setTopic] = useState("");
  const [loading, setLoading] = useState(false);

  async function handleGenerate() {
    if (!topic.trim()) {
      alert("Please enter a topic.");
      return;
    }

    try {
      setLoading(true);

      const result = await generateContent(topic);

      onGenerate(result);


      setTimeout(() => {

          window.scrollTo({

          top:700,

          behavior:"smooth"

          });

          },300);

    } catch (error) {
      console.error(error);
      alert("Failed to generate content.");
    } finally {
      setLoading(false);
    }
  }

  return (
    <div className="topic-wrapper">
      <div className="topic-box">

        <input
          
          className="topic-input"
          autoFocus
          type="text"
          placeholder="Enter any content topic..."
          value={topic}
          onChange={(e) => setTopic(e.target.value)}
          onKeyDown={(e) => {
            if (e.key === "Enter") {
              handleGenerate();
            }
          }}
        />

        <button
          className="generate-btn"
          onClick={handleGenerate}
          disabled={loading}
        >
          {loading ? "Generating..." : "🚀 Generate"}
        </button>

      </div>
    </div>
  );
}

export default TopicInput;
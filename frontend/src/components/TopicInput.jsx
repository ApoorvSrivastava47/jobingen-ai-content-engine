import { useState } from "react";
import "../styles/TopicInput.css";
import { generateContent } from "../services/api";

function TopicInput() {
  const [topic, setTopic] = useState("");

  async function handleGenerate() {
    if (!topic.trim()) {
      alert("Please enter a topic.");
      return;
    }

    try {
      const result = await generateContent(topic);

      console.log(result);

      alert("Content generated successfully!");
    } catch (error) {
      console.error(error);

      alert("Failed to generate content.");
    }
  }

  return (
    <div className="topic-container">
      <input
        className="topic-input"
        type="text"
        placeholder="Enter any topic..."
        value={topic}
        onChange={(e) => setTopic(e.target.value)}
      />

      <button
        className="generate-btn"
        onClick={handleGenerate}
      >
        🚀 Generate
      </button>
    </div>
  );
}

export default TopicInput;
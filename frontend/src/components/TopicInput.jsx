import { useState } from "react";
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

      alert("Content Generated! Check the console.");
    } catch (error) {
      console.error(error);

      alert("Something went wrong.");
    }
  }

  return (
    <div>
      <input
        type="text"
        placeholder="Enter Topic..."
        value={topic}
        onChange={(e) => setTopic(e.target.value)}
      />

      <button onClick={handleGenerate}>
        Generate Content
      </button>
    </div>
  );
}

export default TopicInput;
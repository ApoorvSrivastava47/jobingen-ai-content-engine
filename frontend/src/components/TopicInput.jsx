import { useState } from "react";
import { FaWandMagicSparkles } from "react-icons/fa6";
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

    setLoading(true);

    try {

      const result = await generateContent(topic);

      onGenerate(result);

    } catch (error) {

      console.error(error);

      alert("Failed to generate content.");

    } finally {

      setLoading(false);

    }

  }

  function handleKeyDown(e) {

    if (e.key === "Enter") {

      handleGenerate();

    }

  }

  return (

    <section className="topic-section">

      <div className="topic-box">

        <div className="topic-icon">

          <FaWandMagicSparkles />

        </div>

        <input

          type="text"

          className="topic-input"

          placeholder="Describe the content you want to generate..."

          value={topic}

          onChange={(e) => setTopic(e.target.value)}

          onKeyDown={handleKeyDown}

        />

        <button

          className="generate-btn"

          onClick={handleGenerate}

          disabled={loading}

        >

          {loading ? "Generating..." : "Generate"}

        </button>

      </div>

    </section>

  );

}

export default TopicInput;
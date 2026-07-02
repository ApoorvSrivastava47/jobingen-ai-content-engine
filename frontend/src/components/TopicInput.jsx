import { useState } from "react";
import { FaWandMagicSparkles } from "react-icons/fa6";

import "../styles/TopicInput.css";

import { generateContent } from "../services/api";

function TopicInput({ onGenerate }) {

  const [topic, setTopic] = useState("");
  const [platform, setPlatform] = useState("linkedin");
  const [loading, setLoading] = useState(false);

  async function handleGenerate() {

    if (!topic.trim()) {
      alert("Please enter a topic.");
      return;
    }

    setLoading(true);

    try {

      const result = await generateContent(
        topic,
        platform,
      );

      // 👇 DEBUG
      console.log("========== BACKEND RESPONSE ==========");
      console.log(result);
      console.log("Image Path:", result.image_path);
      console.log("======================================");

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

      <div
        style={{
          display: "flex",
          gap: "12px",
          marginBottom: "16px",
        }}
      >

        <div className="platform-selector">

          {[
            ["linkedin", "LinkedIn"],
            ["instagram", "Instagram"],
            ["twitter", "X"],
            ["facebook", "Facebook"],
            ["blog", "Blog"],
          ].map(([value, label]) => (

            <button
              key={value}
              type="button"
              className={
                platform === value
                  ? "platform-pill active"
                  : "platform-pill"
              }
              onClick={() => setPlatform(value)}
            >
              {label}
            </button>

          ))}

        </div>

      </div>

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
const API_URL = "http://127.0.0.1:8000/generate";

export async function generateContent(topic) {
  const response = await fetch(API_URL, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      topic,
    }),
  });

  if (!response.ok) {
    throw new Error("Failed to generate content");
  }

  return await response.json();
}
function ContentCard({ content }) {
  if (!content) return null;

  return (
    <div className="card">
      <h2>📝 Generated Content</h2>

      <pre>{content}</pre>
    </div>
  );
}

export default ContentCard;
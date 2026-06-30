function ReviewCard({ review }) {
  if (!review) return null;

  return (
    <div className="card">
      <h2>⭐ Critic Review</h2>

      <pre>{review}</pre>
    </div>
  );
}

export default ReviewCard;
function StrategyCard({ strategy }) {
  if (!strategy) return null;

  return (
    <div className="card">
      <h2>📋 Strategy</h2>

      <p><strong>Topic:</strong> {strategy.topic}</p>
      <p><strong>Pillar:</strong> {strategy.pillar}</p>
      <p><strong>Goal:</strong> {strategy.goal}</p>
      <p><strong>Tone:</strong> {strategy.tone}</p>
      <p><strong>Template:</strong> {strategy.template}</p>
    </div>
  );
}

export default StrategyCard;
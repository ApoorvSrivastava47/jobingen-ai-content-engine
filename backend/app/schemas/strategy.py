from dataclasses import dataclass


@dataclass
class StrategySchema:
    topic: str

    pillar: str

    goal: str

    tone: str

    template: str

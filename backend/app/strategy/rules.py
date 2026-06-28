TOPIC_RULES = {
    "resume": {
        "pillar": "placement",
        "goal": "educate",
        "tone": "student_first",
        "template": "checklist",
    },
    "ats": {
        "pillar": "placement",
        "goal": "educate",
        "tone": "professional",
        "template": "how_to",
    },
    "github": {
        "pillar": "coding",
        "goal": "educate",
        "tone": "professional",
        "template": "checklist",
    },
    "rag": {
        "pillar": "ai",
        "goal": "educate",
        "tone": "authoritative",
        "template": "carousel",
    },
    "bootcamp": {
        "pillar": "jobingen",
        "goal": "promote",
        "tone": "friendly",
        "template": "announcement",
    },
    "success": {
        "pillar": "career",
        "goal": "inspire",
        "tone": "inspirational",
        "template": "story",
    },
}


def get_strategy(topic: str):

    topic = topic.lower()

    for keyword, strategy in TOPIC_RULES.items():
        if keyword in topic:
            return {
                "topic": topic,
                **strategy,
            }

    return {
        "topic": topic,
        "pillar": "career",
        "goal": "educate",
        "tone": "student_first",
        "template": "carousel",
    }

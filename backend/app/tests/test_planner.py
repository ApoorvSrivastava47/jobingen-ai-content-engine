from app.engine.planner import Planner


def main():

    planner = Planner()

    response = planner.generate_plan("AI Resume Building Tips")

    print("=" * 60)
    print("PLANNER RESPONSE")
    print("=" * 60)

    print(response)


if __name__ == "__main__":
    main()

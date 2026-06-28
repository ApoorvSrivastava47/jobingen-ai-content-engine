from app.persona.loader import PersonaLoader


def main():
    loader = PersonaLoader()

    print("=" * 50)
    print("ACTIVE VERSION")
    print("=" * 50)
    print(loader.active_version)

    print("\n" + "=" * 50)
    print("PLANNER")
    print("=" * 50)
    print(loader.load_prompt("planner"))

    print("\n" + "=" * 50)
    print("COPYWRITER")
    print("=" * 50)
    print(loader.load_prompt("copywriter"))

    print("\n" + "=" * 50)
    print("CRITIC")
    print("=" * 50)
    print(loader.load_prompt("critic"))


if __name__ == "__main__":
    main()

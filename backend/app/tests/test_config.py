from app.config.config import Config


def main():
    print("=" * 50)
    print("CONFIGURATION")
    print("=" * 50)

    print(f"Model       : {Config.DEFAULT_MODEL}")
    print(f"Temperature : {Config.TEMPERATURE}")
    print(f"Debug Mode  : {Config.DEBUG}")

    if Config.OPENAI_API_KEY:
        print("API Key     : Loaded ✅")
    else:
        print("API Key     : Not Set ❌")


if __name__ == "__main__":
    main()

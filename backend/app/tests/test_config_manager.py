from app.core.config_manager import ConfigManager


def main():
    config = ConfigManager.get()

    print("=" * 50)
    print("CONFIG MANAGER")
    print("=" * 50)

    print(f"Model       : {config.DEFAULT_MODEL}")
    print(f"Temperature : {config.TEMPERATURE}")
    print(f"Debug Mode  : {config.DEBUG}")

    if config.OPENAI_API_KEY:
        print("API Key     : Loaded ✅")
    else:
        print("API Key     : Not Set ❌")


if __name__ == "__main__":
    main()

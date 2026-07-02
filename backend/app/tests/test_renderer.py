from app.renderer.gemini_renderer import GeminiRenderer


def main():

    renderer = GeminiRenderer()

    prompt = """
A premium LinkedIn illustration of an AI engineer
working with futuristic dashboards,
minimal blue and white theme,
professional corporate style,
no text.
"""

    image_path = renderer.render(
        prompt,
        "test_render.png",
    )

    print("=" * 50)
    print("IMAGE SAVED")
    print(image_path)
    print("=" * 50)


if __name__ == "__main__":
    main()

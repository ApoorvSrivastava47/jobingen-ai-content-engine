from app.core.renderer_service import RendererService


def main():

    renderer = RendererService()

    prompt = """
A premium LinkedIn illustration of an AI engineer working
with futuristic dashboards,
blue and white corporate colors,
minimal,
professional,
no text,
isometric style.
"""

    path = renderer.render(
        prompt,
        "flux_test.png",
    )

    print("=" * 60)
    print("IMAGE GENERATED")
    print(path)
    print("=" * 60)


if __name__ == "__main__":
    main()

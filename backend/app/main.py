from fastapi import FastAPI

app = FastAPI(
    title="JobInGen AI Engine",
    version="1.0.0",
    description="AI Content Creation Engine",
)


@app.get("/")
def home():
    return {"message": "JobInGen AI Engine Running 🚀"}


@app.get("/health")
def health():
    return {"status": "healthy"}

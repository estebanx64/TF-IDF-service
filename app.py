import uvicorn  # For debug porpuses
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from apps import tf_idf


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(tf_idf.router)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000)

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routers import minor_planets, cutouts, stars

# https://fastapi.tiangolo.com/tutorial/sql-databases/

app = FastAPI(
    title="UCAC4 FastAPI",
    description="UCAC4 FastAPI",
    version="0.0.1",
    contact={
        "name": "Nico Vermaas",
        "url": "https://uilennest.net",
        "email": "nvermaas@xs4all.nl",
    },
    license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    },)

app.include_router(minor_planets.router)
app.include_router(cutouts.router)
app.include_router(stars.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
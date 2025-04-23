from fastapi import FastAPI

from api.users import router as users_router
from api.trips import router as trips_router
from api.companions import router as companions_router
from api.itineraries import router as itineraries_router
from api.messages import router as messages_router

app = FastAPI()

app.include_router(users_router)
app.include_router(trips_router)
app.include_router(companions_router)
app.include_router(itineraries_router)
app.include_router(messages_router)

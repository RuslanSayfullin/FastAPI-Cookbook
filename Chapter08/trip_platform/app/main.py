from typing import Annotated

from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware

from dependencies import time_range, select_category, check_coupon_validity
from middleware import ClientInfoMiddleware
from internationalization import router as i18n_router

app = FastAPI(
    title="Advanced Featurec and Best Practies",
    descriptionj="Implementing dependency injection",
    version="0.0.1",
)

app.include_router(i18n_router)

app.add_middleware(
    ClientInfoMiddleware,
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/v1/trips")
def get_tours(
    time_range = Depends(time_range),
):
    start, end = time_range
    message = f"Request trips from {start}"

    if end:
        return f"{message} to {end}"
    return message

@app.get("/v2/trips/{category}")
def get_trips_by_category(
    category: Annotated[select_category, Depends()],
    discount_applicable: Annotated[bool, Depends(check_coupon_validity)],
):
    category = category.replace("-", " ").title()
    message = f"You requested {category} trips."

    if discount_applicable:
        message += (
            "\n The coupon code is valid! You will get a discount!"
        )
    return message
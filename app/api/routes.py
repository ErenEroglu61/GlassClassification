from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from app.ml.model import GlassClassifier
from app.api.schemas import GlassInput, PredictionResult


router = APIRouter()
classifier = GlassClassifier()
templates = Jinja2Templates(directory="app/templates")


@router.post("/predict", response_model=PredictionResult)
async def predict(glass_data: GlassInput):
    result = classifier.predict(glass_data.model_dump())
    return result


@router.get("/")
async def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html"
    )


@router.get("/predict-page")
async def predict_page(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="predict.html"
    )
from fastapi import APIRouter


router = APIRouter(prefix="/api")


@router.get("/helloworld")
async def hello_world():
    return {"hello world!"}
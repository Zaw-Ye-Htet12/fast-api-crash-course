import fastapi

router = fastapi.APIRouter()

@router.get("/sections/{id}")
async def read_section():
    return {"sections": []}


@router.get("/sections/{id}/content-blocks")
async def read_section_content_blocks():
    return {"sections": []}

@router.get("/content-blocks/{id}")
async def read_content_block():
    return {"sections": []}
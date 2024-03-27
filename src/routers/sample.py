from fastapi import APIRouter

router = APIRouter()

@router.get('/', summary="サンプルメッセージ")

def sample():
    """
    sample
    """

    return {"message": "Success"}
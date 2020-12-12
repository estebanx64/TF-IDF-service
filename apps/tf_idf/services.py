from fastapi import APIRouter, HTTPException

from apps.tf_idf.utils import tfidf_url


router = APIRouter()


@router.get("/v1/tfidf", tags=["tf-idf-url"])
async def get_tfidf_by_url(url: str, limit: int):
    try:
        tf_idf_results = tfidf_url(url)
        return {"terms": tf_idf_results[:limit]}
    except Exception:
        return HTTPException(status_code=500, detail="Unproccesable url")

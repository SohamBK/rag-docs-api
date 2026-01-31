from fastapi import APIRouter, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.domains.documents.schemas import DocumentCreate
from app.domains.documents.service import DocumentService
from app.domains.documents.ingestion.factory import get_extractor
from fastapi import UploadFile
from app.api.deps.db import get_db_session
from app.core.responses import SuccessResponse

router = APIRouter(prefix="/documents", tags=["documents"])


@router.post(
    "",
    status_code=status.HTTP_201_CREATED,
    response_model=SuccessResponse[dict],
)
async def ingest_document(
    payload: DocumentCreate,
    db: AsyncSession = Depends(get_db_session),
):
    document_id = await DocumentService.ingest_document(
        db=db,
        payload=payload,
    )

    return SuccessResponse(
        data={"document_id": document_id},
        message="Document created successfully",
    )

@router.post("/documents/upload")
async def upload_document(
    file: UploadFile,
    source: str,
    title: str,
    db: AsyncSession = Depends(get_db_session),
):
    document_id = await DocumentService.ingest_file(
        db=db,
        file=file,
        source=source,
        title=title,
    )

    return SuccessResponse(
        data={"document_id": document_id},
        message="Document uploaded successfully",
    )


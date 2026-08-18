from fastapi import UploadFile, HTTPException

from app.config import settings


ALLOWED_MIME_TYPES = {
    "application/pdf",
}

ALLOWED_EXTENSIONS = {
    ".pdf",
}


async def validate_document(file: UploadFile) -> None:

    if not file.filename:
        raise HTTPException(
            status_code=400,
            detail="A file must be provided.",
        )

    filename = file.filename.lower()

    if not any(filename.endswith(extension) for extension in ALLOWED_EXTENSIONS):
        raise HTTPException(
            status_code=400,
            detail="Only PDF files are allowed.",
        )

    if file.content_type not in ALLOWED_MIME_TYPES:
        raise HTTPException(
            status_code=400,
            detail="Invalid file type. Only PDF files are allowed.",
        )

    max_size = settings.MAX_DOCUMENT_SIZE_MB * 1024 * 1024

    file.file.seek(0)

    content = await file.read(max_size + 1)

    file.file.seek(0)

    if len(content) > max_size:
        raise HTTPException(
            status_code=413,
            detail=f"File size exceeds the {settings.MAX_DOCUMENT_SIZE_MB} MB limit.",
        )

    if not content.startswith(b"%PDF-"):
        raise HTTPException(
            status_code=400,
            detail="Invalid PDF file.",
        )
# from fastapi import FastAPI, UploadFile, File, HTTPException, Depends
# from fastapi.security.api_key import APIKeyHeader, APIKey
# import os
# from services import ocr_image, extract_receipt
# from dotenv import load_dotenv
# import uvicorn

# load_dotenv()
# API_KEY = os.getenv("RECEIPT_API_KEY")

# app = FastAPI()

# api_key_header = APIKeyHeader(name="api_key", auto_error=True)

# def get_api_key(api_key_header: str = Depends(api_key_header)) -> APIKey:
#     if api_key_header != API_KEY:
#         raise HTTPException(status_code=401, detail="Unauthorized")
#     return api_key_header
# @app.get("/")
# def home(api_key: APIKey = Depends(get_api_key)):
#     return {"message": "Receipt OCR API is running!"}

# @app.post("/process-receipt/")
# async def process_receipt(file: UploadFile = File(...), api_key: APIKey = Depends(get_api_key)):
#     temp_file = file.filename
#     with open(temp_file, "wb") as f:
#         f.write(await file.read())

#     ocr_text = ocr_image(temp_file)
#     extracted_data = extract_receipt(ocr_text)
#     return extracted_data
from fastapi import FastAPI, UploadFile, File, Header, HTTPException
from dotenv import load_dotenv
import os
from services import ocr_image, extract_receipt
import uvicorn

load_dotenv()  # Load .env file
API_KEY = os.getenv("RECEIPT_API_KEY")  # Get API key from .env file

app = FastAPI()

#function to verify API key
def verify_api_key(api_key: str):
    if api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Unauthorized")

# Health check
@app.get("/")
def home(api_key: str = Header(..., alias="api_key")):
    verify_api_key(api_key)
    return {"message": "Receipt OCR API is running!"}

# Process receipt
@app.post("/process-receipt/")
async def process_receipt(file: UploadFile = File(...), api_key: str = Header(..., alias="api_key")):
    verify_api_key(api_key)

    temp_file = file.filename
    with open(temp_file, "wb") as f:
        f.write(await file.read())

    ocr_text = ocr_image(temp_file)
    extracted_data = extract_receipt(ocr_text)
    return extracted_data

# if __name__ == "__main__":
#     uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)

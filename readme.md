# Receipt OCR API
A FastAPI-based service that extracts structured data from receipt images using OCR + LLM.

#  Features
- Upload a receipt image and get structured JSON output
- OCR extraction from image using `ImgOcr`
- LLM-based extraction into clean JSON format
- Separation of API (FastAPI) and business logic (services.py)

# 📂 Project Structure
/OCR-LLM-PRODUCTION-READY
│
├── main.py # FastAPI application
├── services.py # Contains OCR and LLM extraction logic
├── .env # Stores API key
├── requirements.txt # Python dependencies
└── README.md # Project documentation


## ⚙️ Setup Instructions

### 1️⃣ Clone the repo
```bash
git clone <your-repo-url>
cd OCR-LLM-PRODUCTION-READY


Create a virtual environment

python -m venv .venv
source .venv/bin/activate    # Linux/Mac
.venv\Scripts\activate       # Windows

2️⃣ Install dependencies

pip install -r requirements.txt


Create a .env file in the root directory:

RECEIPT_API_KEY=""


This key will be used to authenticate API requests.

Running the API
uvicorn main:app --host 127.0.0.1 --port 8000 --reload


Swagger UI: Open http://127.0.0.1:8000/docs

API Endpoints
1. Health Check

GET /
Headers:
api_key: <your_api_key>

Response:

{
  "message": "Receipt OCR API is running!"
}

2. Process Receipt

POST /process-receipt/
Headers:
api_key: <your_api_key>

Body:
Upload a receipt image as multipart/form-data.

Response:

{
  "store_name": "Walmart",
  "customer_name": null,
  "date": "2022-06-29",
  "order_time": "19:45",
  "final_total": "50.00",
  "payment_method": "DEBIT"

}

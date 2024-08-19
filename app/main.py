from fastapi import FastAPI, HTTPException, File, UploadFile
from pydantic import BaseModel
from typing import List
import pandas as pd
import uuid

from app import services, schemas

app = FastAPI()

@app.post("/upload-csv/")
async def upload_csv(file: UploadFile = File(...)):
    try:
        contents = await file.read()
        df = pd.read_csv(pd.compat.StringIO(contents.decode('utf-8')))
        data = df.to_dict(orient='records')
        if not all(col in df.columns for col in ["name", "governmentId", "email", "debtAmount", "debtDueDate", "debtID"]):
            raise HTTPException(status_code=400, detail="CSV file missing required columns")
        await services.process_debt_records(data)
        return {"message": "CSV processed successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/generate-bills/")
async def generate_bills():
    try:
        await services.generate_and_send_bills()
        return {"message": "Bills generated and sent"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

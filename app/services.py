import pandas as pd
from typing import List
from app import models
import smtplib
from email.mime.text import MIMEText

debt_records: List[models.DebtRecord] = []

async def process_debt_records(data: List[dict]):
    global debt_records
    debt_records = [models.DebtRecord(**record) for record in data]

async def generate_and_send_bills():
    for record in debt_records:
        # Generate bill here
        bill = f"Boleto para {record.name}, valor {record.debtAmount}, vencimento {record.debtDueDate.strftime('%Y-%m-%d')}"
        
        # Send email
        msg = MIMEText(bill)
        msg['Subject'] = 'Seu Boleto'
        msg['From'] = 'no-reply@example.com'
        msg['To'] = record.email

        with smtplib.SMTP('localhost') as server:
            server.send_message(msg)

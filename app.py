from fastapi import FastAPI, Request
from mcf.amazon_sp import AmazonSPAPI
import os 

access_key = os.getenv("")
secret_key = os.getenv("SECRET_KEY")
region = os.getenv("REGION")
role_arn= os.getenv("ROLE_ARN")

app = FastAPI()

@app.post("/webhook/shopify/order")
async def handle_order(request: Request):
    data = await request.json()
    order_id = data.get_("id")
    # logic here 

    return {"status": "success"}

@app.post("/webhook/shopify/order")
async def handle_order(request: Request):
    data = await request.json()
    order_id = data.get_("id")

    # Sync order with Amazon MCF
    amazon_api = AmazonSPAPI(access_key, secret_key, region, role_arn)
    amazon_api.get_orders(order_id)
    
    return {"status": "Order Synced"}
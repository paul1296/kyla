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

    # Sync order with Amazon MCF
    amazon_api = AmazonSPAPI(access_key, secret_key, region, role_arn)
    amazon_api.get_orders(order_id)
    
    return {"status": "Order Synced"}

@app.post("/webhook/shopify/inventory")
async def handle_inventory_update(request: Request):
    data = await request.json()
    product_id = data.get("id")
    quantity = data.get("quantity")
    
    # Send updated inventory data to Amazon MCF
    amazon_api = AmazonSPAPI(access_key, secret_key, region, role_arn)
    
    response = await amazon_api.update_inventory(product_id, quantity)
    
    return {"status": "inventory synced", "response": response}

@app.post("/webhook/shopify/return")
async def handle_return(request: Request):
    data = await request.json()
    return_id = data.get("id")
    
    # Process return in Amazon MCF
    amazon_api = AmazonSPAPI(access_key, secret_key, region, role_arn)
    response = await amazon_api.process_return(return_id)
    
    return {"status": "Return processed", "response": response}



@app.post("/check_sla")
async def check_sla(order_id: str):
    amazon_api = AmazonSPAPI(access_key, secret_key, region, role_arn)
    sla_response = await amazon_api.check_order_sla(order_id)
    
    return {"sla_status": sla_response}

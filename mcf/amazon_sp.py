import boto3
import httpx

class AmazonSPAPI:
    def __init__(self, access_key, secret_key, region, role_arn):
        self.access_key = access_key
        self.secret_key = secret_key
        self.region = region
        self.role_arn = role_arn

    def get_orders(self, order_id):
        # Create a signed request using boto3
        session = boto3.Session(
            aws_access_key_id=self.access_key,
            aws_secret_access_key=self.secret_key,
            region_name=self.region
        )

        client = session.client('sts')
        credentials = client.assume_role(RoleArn=self.role_arn, RoleSessionName="SPAPI")

        headers = {
            "x-amz-access-token": credentials["Credentials"]["SessionToken"]
        }

        response = httpx.get(
            f"https://sellingpartnerapi-eu.amazon.com/orders/v0/orders/{order_id}",
            headers=headers
        )

        return response.json()

from pydantic import BaseModel, Field, ValidationError


class OrderSchema(BaseModel):
    client_name: str = Field(min_length=1)
    table_number: str = Field(min_length=1)
    order_details: str = Field(min_length=1)
    order_time: str = Field(min_length=1)
    client_email: str = Field(min_length=1)
    status: str = Field(min_length=1)

class CheckOrder():
    def check_order(order):
        if(order['client_name'].isspace() or order['table_number'].isspace() or order['order_details'].isspace() or order['order_time'].isspace() or order['client_email'].isspace()):
            return None
        return True

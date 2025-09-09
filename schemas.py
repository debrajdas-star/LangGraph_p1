from pydantic import BaseModel,Field
from typing import Optional


class Products(BaseModel):

    name: str = Field(description="This is the product or item name")
    inclusive_price: Optional[float] = Field(default=None, description="This is the price of the product in deceimal field")
    sku: str = Field(description="This is the SKU(Stock Keeping Unit) is a unique, \
                     alphanumeric identifier assigned by a business to its products \
                     to track and manage inventory internally")
    internal_sku: str = Field(description="An internal SKU code (Stock Keeping Unit) \
                              is a unique alphanumeric identifier that a specific business \
                              creates to track and manage its own inventory of products")
    description: str = Field(description="description of the product")
    style: str = Field(description="This is the style of the product")
    color: str = Field(description="This is the color of the product")
    uom: str = Field(description="Unit of measurement")
    coverage: Optional[float] = Field(default=None, description="Refers to the surface area (in square feet or sq ft)\
                            that a specific amount of that productcoverage in sq ft")
    cut_price: Optional[float] = Field(default=None,description="A price or rate per square foot")
    vendor_name: Optional[str] = Field(default=None,
                                       description="Name of the vendor of the product")
    is_discontinued: Optional[bool] = Field(default=True, description="If it is discontinued or note")

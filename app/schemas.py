from pydantic import BaseModel

class BaseURL(BaseModel):
#  Shouldn't this be default valued at None?
    target_url: str 


class URL(BaseURL):
    is_active: bool = True
    clicks: int = 0

    class Config:
        orm_mode = True

"""
By adding url and admin_url to the URLInfo subclass, 
you can use the data in your API without storing it in your database. 
"""
class URLInfo(URL):
    url: str
    admin_url: str
    
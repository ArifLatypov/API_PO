import aiohttp
import asyncio
from pydantic import BaseModel
from enum import Enum



class APIClient:
    def __init__(self, base_url, headers):
        self.base_url = base_url
        self.headers = headers

    async def request(self, method, url, data=None):
        async with aiohttp.ClientSession() as session:
            session.headers.update(self.headers)
            async with session.request(method, url, json=data) as response:
                return await response.json()


class product_list_filter(BaseModel):
    offer_id: list[str] = []
    product_id: list[str] = []
    visibility: str = "ALL"

class product_list_request(BaseModel):
    filter: product_list_filter
    last_id: str
    limit: int = 100

    def to_dict(self):
        return self.dict()

class product_info_request(BaseModel):
    offer_id: str
    product_id: int
    sku: int=0

    def to_dict(self):
        return self.dict()

class product_info_description_request(BaseModel):
    offer_id: str
    product_id: int

    def to_dict(self):
        return self.dict()

class product_import_info_request(BaseModel):
    task_id: int

    def to_dict(self):
        return self.dict()

class product_description_category_tree_languages_request(str, Enum):
    DEFAULT = 'DEFAULT'
    EN  = 'EN',
    RU =  'RU',
    TR = 'TR',
    ZH_HANS = 'ZH_HANS'
    
    
class product_description_category_tree_request(BaseModel):
    language: product_description_category_tree_languages_request 

    def to_dict(self):
        return self.dict()

class warehouse_list_request(BaseModel):
    pass

    def to_dict(self):
        return self.dict()

class report_info_request(BaseModel):
    code: str
    
    def to_dict(self):
        return self.dict()



class report_list_report_type(str, Enum):
    DEFAULT = 'DEFAULT'
    ALL = 'ALL',
    SELLER_PRODUCTS  =  'SELLER_PRODUCTS ',
    SELLER_TRANSACTIONS  = 'SELLER_TRANSACTIONS ',
    SELLER_PRODUCT_PRICES  = 'SELLER_PRODUCT_PRICES ',
    SELLER_STOCK = 'SELLER_STOCK ',
    SELLER_RETURNS = 'SELLER_RETURNS ',
    SELLER_POSTINGS = 'SELLER_POSTINGS ',
    SELLER_FINANCE = 'SELLER_FINANCE ',
    SELLER_PRODUCT_DISCOUNTED = 'SELLER_PRODUCT_DISCOUNTED '



class report_list_request(BaseModel):
    
    page: int
    page_size: int=100
    report_type: report_list_report_type

    def to_dict(self):
        return self.dict()



async def report_list(page, page_size, report_type, api_client):
    """Функции для просмотра отчётов сформированных ранее 
        !page_size - НЕ БОЛЬШЕ 1000!                """
    request_data = report_list_request(page=page, page_size=page_size, report_type=report_type)
    response = await api_client.request('POST','https://api-seller.ozon.ru/v1/report/list', request_data.to_dict())
    print(response)



async def report_info(code, api_client):
    """Функции для просмотра ифнормации об отчётах"""
    request_data = report_info_request(code=code)
    response = await api_client.request('POST','https://api-seller.ozon.ru/v1/report/info', request_data.to_dict())
    print(response)



async def warehouse_list(api_client):
    """Функции для просмотра списка складов"""
    request_data = warehouse_list_request()
    response = await api_client.request('POST','https://api-seller.ozon.ru/v1/warehouse/list', request_data.to_dict())
    print(response)



async def product_description_category_tree(language, api_client):
    """Дерево категорий товаров"""
    request_data = product_description_category_tree_request(language=language)
    response = await api_client.request('POST','https://api-seller.ozon.ru/v1/description-category/tree', request_data.to_dict())
    print(response)



async def product_import_info(task_id, api_client):
    """Информация о состоянии статуса создания карточки"""
    request_data = product_import_info_request(task_id=task_id)
    response = await api_client.request('POST','https://api-seller.ozon.ru/v1/product/import/info', request_data.to_dict())
    print(response)



async def product_info_description(offer_id, product_id, api_client):
    """Описание товара продавца"""
    request_data = product_info_description_request(offer_id=offer_id, product_id=product_id)
    response = await api_client.request('POST','https://api-seller.ozon.ru/v1/product/info/description', request_data.to_dict())
    print(response)



async def product_info(offer_id, product_id, sku, api_client):
    """Информация о товаре продавца"""
    request_data = product_info_request(offer_id=offer_id, product_id=product_id, sku=sku)
    response = await api_client.request('POST','https://api-seller.ozon.ru/v2/product/info', request_data.to_dict())
    print(response)



async def product_list(offer_id, product_id, visibility, last_id, limit, api_client):
    """Список товаров продавца"""
    request_data = product_list_request(filter=product_list_filter(offer_id=offer_id, product_id=product_id, visibility=visibility), last_id=last_id, limit=limit)
    response = await api_client.request('POST', 'https://api-seller.ozon.ru/v2/product/list', request_data.to_dict())
    print(response)



async def main():
    api_client = APIClient('https://api-seller.ozon.ru', {'Client-Id': "", 'Api-Key': ""})
    await product_info("Z00016",0,654078431,api_client)

asyncio.run(main())




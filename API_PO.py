# 3 alfa made by Lock

import aiohttp
import asyncio
from pydantic import BaseModel
from enum import Enum
from typing import List


class APIClient:
    def __init__(self, base_url, headers):
        self.base_url = base_url
        self.headers = headers

    async def request(self, method, url, data=None):
        async with aiohttp.ClientSession() as session:
            session.headers.update(self.headers)
            async with session.request(method, url, json=data) as response:
                return await response.json()



class Value(BaseModel):
    dictionary_value_id: int
    value: str

 

class Attribute(BaseModel):
    complex_id: int
    id: int
    values: list[Value]
    
    def to_dict(self):
        return self.dict()



class Item(BaseModel):
    attributes: list[Attribute]
    offer_id: str

class ArrayData(BaseModel):
    items: list[Item]
  

class warehouse_delivery_methods_status(str, Enum):
    NEW  = 'NEW'
    EDITED  = 'EDITED',
    ACTIVE   =  'ACTIVE',
    DISABLED   = 'DISABLED'


class fbs_company_returns_last_free_waiting_day(BaseModel):
    time_from: str 
    time_to: str
    


class fbs_company_returns_filter(BaseModel):
    last_free_waiting_day: fbs_company_returns_last_free_waiting_day
    order_id: int
    posting_number: list[str]
    product_name: str
    product_offer_id: str
    status: str

class fbs_company_returns_request(BaseModel):
    filter: fbs_company_returns_filter
    limit: int
    last_id: int

class supply_order_list_request(BaseModel):
    page: int
    page_size: int
    states: list[str]

class supply_order_get_request(BaseModel):
    supply_order_id: int


class supply_order_items_request(BaseModel):
    page: int
    page_size: int
    supply_order_id: int


class fbo_company_returns_filter(BaseModel):
    posting_number: str
    status: list[str] = ['Created','ReturnedToOzon','Cancelled','CancelledWithCompensation','Deleted','TechnicalReturn','RemovedFromRms']


class fbo_company_returns_request(BaseModel):
    filter: fbo_company_returns_filter
    last_id: int
    limit: int 


class product_attributes_filter(BaseModel):
    offer_id: list[str] = []
    product_id: list[str] = []
    visibility: str = "ALL"

class product_attributes_request(BaseModel):
    filter: product_attributes_filter
    last_id: str
    limit: int = 100
    sort_by: str = ""
    sort_dir: str = "ASC"


    def to_dict(self):
        return self.dict()


class direction_class(str, Enum):
    DIRECTION_UNKNOWN = 'DIRECTION_UNKNOWN'
    DIRECTION_NONE = 'DIRECTION_NONE'
    DIRECTION_RISE = 'DIRECTION_RISE'
    DIRECTION_FALL = 'DIRECTION_FALL'


class meaning_class(str, Enum):
    MEANING_UNKNOWN = 'MEANING_UNKNOWN'
    MEANING_NONE = 'MEANING_NONE'
    MEANING_GOOD  = 'MEANING_GOOD'
    MEANING_BAD = 'MEANING_BAD'



class change_class(BaseModel):
    direction: direction_class
    meaning: meaning_class


class rating_direction_class(str, Enum):
    UNKNOWN_DIRECTION = 'UNKNOWN_DIRECTION'
    NEUTRAL = 'NEUTRAL'
    HIGHER_IS_BETTER = 'HIGHER_IS_BETTER'
    LOWER_IS_BETTER = 'LOWER_IS_BETTER'

    
class status_class(str, Enum):
    UNKNOWN_STATUS = 'UNKNOWN_STATUS'
    OK = 'OK'
    WARNING = 'WARNING'
    CRITICAL = 'CRITICAL'

class value_type_class(str, Enum):
    UNKNOWN_VALUE = 'UNKNOWN_VALUE'
    INDEX = 'INDEX'
    PERCENT = 'PERCENT'
    TIME = 'TIME'
    RATIO = 'RATIO'
    REVIEW_SCORE = 'REVIEW_SCORE'
    COUNT = 'COUNT'


class company_certification_info_request(BaseModel):
    certificate_number: str

class company_certificate_delete_request(BaseModel):
    certificate_id: int

class seller_rating_summary_items(BaseModel):
    change: change_class
    current_value: float|int
    name: str
    past_value: float|int
    rating: str
    rating_direction: rating_direction_class
    status: status_class
    value_type: value_type_class




class seller_rating_summary_group(BaseModel):
    group_name: str
    items: list[seller_rating_summary_items]

class seller_rating_summary_request(BaseModel):
    groups: seller_rating_summary_group
    penalty_score_exceeded: bool
    premium: bool




class product_certification_bind_request(BaseModel):
    certificate_id: int
    product_id: list[int] 

class product_certification_unbind_request(BaseModel):
    certificate_id: int
    product_id: list[str] 

class product_certification_list_request(BaseModel):
    certificate_id: int 
    product_status_code: str
    page: int
    page_size: int


class company_certification_list_request(BaseModel):
    offer_id: str
    status: str
    type_: str
    page: int = 1
    page_size: int = 1000


class fbs_act_get_postings_request(BaseModel):
    id: int


class product_info_prices_filter(BaseModel):
    offer_id: list[str] = []
    product_id: list[str] = []
    visibility: str = "ALL"

class product_info_prices_request(BaseModel):
    filter: product_info_prices_filter
    last_id: str
    limit: int = 100

    def to_dict(self):
        return self.dict()

class company_certification_types_request(BaseModel):
    pass


class company_certification_brands_list_request(BaseModel):
    page: int
    page_size: int



class stocks(BaseModel):
    offer_id: str
    product_id: int
    stock: int    


class warehouse_delivery_methods_status(str, Enum):
    NEW  = 'NEW'
    EDITED  = 'EDITED',
    ACTIVE   =  'ACTIVE',
    DISABLED   = 'DISABLED'


class warehouse_delivery_methods_filter(BaseModel):
    provider_id: int
    status: warehouse_delivery_methods_status
    warehouse_id: int
    


class warehouse_delivery_methods_request(BaseModel):
    filter: warehouse_delivery_methods_filter
    limit: int = 50
    offset: int


class product_stocks_filter(BaseModel):
    offer_id: list[str] = []
    product_id: list[str] = []
    visibility: str = "ALL"

class product_stocks_request(BaseModel):
    filter: product_stocks_filter
    last_id: str
    limit: int = 100

    def to_dict(self):
        return self.dict()


class rating_history_request(BaseModel):
    date_from: str
    date_to: str
    ratings: list[str] = ['rating_on_time', 
                          'rating_review_avg_score_total', 
                          'rating_price', 
                          'rating_order_cancellation', 
                          'rating_shipment_delay', 
                          'rating_ssl', 
                          'rating_on_time_supply_delivery', 
                          'rating_order_accuracy', 
                          'rating_on_time_supply_cancellation', 
                          'rating_reaction_time',
                          'rating_average_response_time',
                          'rating_replied_dialogs_ratio',
                          'rating_on_time']
    with_premium_scores: bool


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

class report_product_create_language(str, Enum):
    RU = 'RU' 
    EN = 'EN'

class report_product_create_visibility(str, Enum):
    ALL = 'ALL'
    VISIBLE = 'VISIBLE'
    INVISIBLE = 'INVISIBLE'
    EMPTY_STOCK = 'EMPTY_STOCK'
    NOT_MODERATED = 'NOT_MODERATED'
    MODERATED = 'MODERATED'
    DISABLED = 'DISABLED'
    STATE_FAILED = 'STATE_FAILED'
    READY_TO_SUPPLY = 'READY_TO_SUPPLY'
    VALIDATION_STATE_PENDING = 'VALIDATION_STATE_PENDING'
    VALIDATION_STATE_FAIL = 'VALIDATION_STATE_FAIL'
    VALIDATION_STATE_SUCCESS = 'VALIDATION_STATE_SUCCESS'
    TO_SUPPLY = 'TO_SUPPLY'
    IN_SALE = 'IN_SALE'
    REMOVED_FROM_SALE = 'REMOVED_FROM_SALE'
    BANNED = 'BANNED'
    OVERPRICED = 'OVERPRICED'
    CRITICALLY_OVERPRICED = 'CRITICALLY_OVERPRICED'
    EMPTY_BARCODE = 'EMPTY_BARCODE'
    BARCODE_EXISTS = 'BARCODE_EXISTS'
    QUARANTINE = 'QUARANTINE'


class report_product_create_request(BaseModel):
    language: report_product_create_language
    offer_id: list[str]
    search: str
    sku: list[int]
    visibility: report_product_create_visibility


class report_returns_create_language(str, Enum):
    RU = 'RU' 
    EN = 'EN'

class report_returns_create_request(BaseModel):
    delivery_schema:str
    order_id: int
    status: str
    language: report_returns_create_language


class report_postings_create_delivery_schema(str, Enum):
    fbo = 'fbo'
    fbs = 'fbs'


class report_postings_creater_language(str, Enum):
    DEFAULT = 'DEFAULT'
    RU = 'RU' 
    EN = 'EN'

class report_postings_creater_filter(BaseModel):
    cancel_reason_id: list[int]
    delivery_schema: list[report_postings_create_delivery_schema]
    offer_id: str
    processed_at_from: str
    processed_at_to: str
    sku: list[int]
    status_alias: list[str]
    statuses: list[int]
    title: str


class report_postings_create_request(BaseModel):
    
    filter : report_postings_creater_filter
    language : report_postings_creater_language


class finance_statement_list_date(BaseModel):
    from_: str
    to: str


class finance_statement_list_request(BaseModel):
    date: finance_statement_list_date
    page: int
    with_details: bool
    page_size: int


class invoice_create_or_update_price_currency(str, Enum):
    USD = 'USD'
    EUR = 'EUR'
    TRY = 'TRY'
    CNY = 'CNY'
    RUB = 'RUB'
    GBP = 'GBP'


class invoice_create_or_update_request(BaseModel):
    HS_code: str
    date: str
    number : str
    posting_number: str
    price: float
    price_currency: invoice_create_or_update_price_currency 
    url: str
    

class invoice_get_request(BaseModel):
    posting_number: str


class invoice_delete_request(BaseModel):
    posting_number: str


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

async def product_info_prices(offer_id, product_id, visibility, last_id, limit, api_client):
    """Информация о ценах за товар"""
    request_data = product_info_prices_request(filter=product_info_prices_filter(offer_id=offer_id, product_id=product_id, visibility=visibility), last_id=last_id, limit=limit)
    response = await api_client.request('POST', 'https://api-seller.ozon.ru/v4/product/info/prices', request_data.to_dict())
    print(response)

#ПОПЫТКИ:
# async def product_attributes_update(offer_id:list[str], complex_id:int, id:int, dictionary_value_id:int, value:str, api_client):
#     """Обновление характеристик товара"""  
    # request_data = ArrayData(items=list[Item(attributes=list[Attribute(complex_id=complex_id, id=id, values=[Value(dictionary_value_id=dictionary_value_id, value=value)])],offer_id=offer_id)])
#     #request_data = ArrayData(items=list(Item(attributes=list(Attribute(complex_id=complex_id, id=id, values=list(Value(dictionary_value_id=dictionary_value_id, value=value)))),offer_id=offer_id)))
#     response = await api_client.request('POST', 'https://api-seller.ozon.ru/v1/product/attributes/update', request_data.model_dump())
#     print(response)
    
async def product_attributes_update(offer_id: list[str], complex_id: int, id: int, dictionary_value_id: int, value: str, api_client):
    """Обновление характеристик товара"""  
    request_data = ArrayData(items=[Item(attributes=[Attribute(complex_id=complex_id, id=id, values=[Value(dictionary_value_id=dictionary_value_id, value=value)])], offer_id=offer_id)])
    response = await api_client.request('POST', 'https://api-seller.ozon.ru/v1/product/attributes/update', request_data.model_dump())
    print(response)

async def product_attributes(offer_id, product_id, visibility, last_id, limit, sort_by, sort_dir, api_client):
    """Список товаров продавца"""
    request_data = product_attributes_request(filter=product_attributes_filter(offer_id=offer_id, product_id=product_id, visibility=visibility), last_id=last_id, limit=limit, sort_by=sort_by, sort_dir=sort_dir)
    response = await api_client.request('POST', 'https://api-seller.ozon.ru/v3/products/info/attributes', request_data.to_dict())
    print(response)

async def product_stocks(offer_id, product_id, visibility, last_id, limit, api_client):
    """Информация о количестве товара"""
    request_data = product_stocks_request(filter=product_stocks_filter(offer_id=offer_id, product_id=product_id, visibility=visibility), last_id=last_id, limit=limit)
    response = await api_client.request('POST', 'https://api-seller.ozon.ru/v3/product/info/stocks', request_data.to_dict())
    print(response)

async def product_stocks_update(offer_id, product_id, stock, api_client):
    """Обновление количества товара"""
    request_data = stocks(offer_id=offer_id, product_id=product_id, stock=stock)
    response = await api_client.request('POST', 'https://api-seller.ozon.ru/v1/product/import/stocks', request_data.model_dump())
    print(response)

async def warehouse_list(api_client):
    """Функции для просмотра списка складов"""
    request_data = warehouse_list_request()
    response = await api_client.request('POST','https://api-seller.ozon.ru/v1/warehouse/list', request_data.to_dict())
    print(len(response['result']))


async def warehouse_delivery_methods(provider_id, status, warehouse_id, limit, offset, api_client):
    """Методы доставки склада"""
    request_data = warehouse_delivery_methods_request(filter = warehouse_delivery_methods_filter(provider_id=provider_id, status=status, warehouse_id=warehouse_id), limit=limit, offset=offset)
    response = await api_client.request('POST', 'https://api-seller.ozon.ru/v1/delivery-method/list', request_data.model_dump())
    print(response)

async def company_certification_brands_list(page, page_size, api_client):
    """Список сертифицируемых брендов"""
    request_data = company_certification_brands_list_request(page=page, page_size=page_size)
    response = await api_client.request('POST', 'https://api-seller.ozon.ru/v1/brand/company-certification/list', request_data.model_dump())
    print(response)

async def company_certification_types(api_client):
    """Справочник типов документов"""
    request_data = company_certification_types_request()
    response = await api_client.request('GET', 'https://api-seller.ozon.ru/v1/product/certificate/types', request_data.model_dump())
    print(response)

async def company_certification_list(offer_id, status, type_, page, page_size, api_client):
    """Список сертификатов"""
    request_data = company_certification_list_request(offer_id=offer_id, status=status, type_=type_, page=page, page_size=page_size)
    response = await api_client.request('POST', 'https://api-seller.ozon.ru/v1/product/certificate/list', request_data.model_dump())
    print(response)

async def company_certification_info(certificate_number, api_client):
    """Информация о сертификате"""
    request_data = company_certification_info_request(certificate_number=certificate_number)
    response = await api_client.request('POST', 'https://api-seller.ozon.ru/v1/product/certificate/info', request_data.model_dump())
    print(response)


async def product_certification_bind(certificate_id, product_id, api_client):
    """Привязать сертификат к товару"""
    request_data = product_certification_bind_request(certificate_id=certificate_id, product_id=product_id)
    response = await api_client.request('POST', 'https://api-seller.ozon.ru/v1/product/certificate/bind', request_data.model_dump())
    print(response)

async def product_certification_unbind(certificate_id, product_id, api_client):
    """Отвязать товар от сертификата"""
    request_data = product_certification_unbind_request(certificate_id=certificate_id, product_id=product_id)
    response = await api_client.request('POST', 'https://api-seller.ozon.ru/v1/product/certificate/unbind', request_data.model_dump())
    print(response)

async def product_certificate_list(certificate_id:int, product_status_code:str, page:int, page_size:int, api_client):
    """Список товаров, привязанных к сертификату"""
    request_data = product_certification_list_request(certificate_id=certificate_id, product_status_code=product_status_code, page=page, page_size=page_size)
    response = await api_client.request('POST', 'https://api-seller.ozon.ru/v1/product/certificate/products/list', request_data.model_dump())
    print(response)


async def company_certificate_delete(certificate_id, api_client):
    """Удалить сертификат"""
    request_data = company_certificate_delete_request(certificate_id=certificate_id)
    response = await api_client.request('POST', 'https://api-seller.ozon.ru/v1/product/certificate/delete', request_data.model_dump())
    print(response)


async def fbo_company_returns(posting_number, status, last_id, limit, api_client):
    """Получить информацию о возвратах FBO"""
    request_data = fbo_company_returns_request(filter=fbo_company_returns_filter(posting_number=posting_number, status=status), last_id=last_id, limit=limit)
    response = await api_client.request('POST','https://api-seller.ozon.ru/v3/returns/company/fbo', request_data.model_dump())
    print(response)



async def fbs_company_returns(time_from, time_to, order_id, posting_number, product_name, product_offer_id, status, limit, last_id, api_client):
    """Получить информацию о возвратах FBS"""
    request_data = fbs_company_returns_request(filter=fbs_company_returns_filter(
        last_free_waiting_day=fbs_company_returns_last_free_waiting_day(
        time_to=time_to, 
        time_from=time_from), 
        order_id=order_id, 
        posting_number=posting_number, 
        product_name=product_name, 
        product_offer_id=product_offer_id, 
        status=status), 
        limit=limit, 
        last_id=last_id)
    
    response = await api_client.request('POST','https://api-seller.ozon.ru/v3/returns/company/fbs', request_data.model_dump())
    print(response)


async def fbs_act_get_postings(id, api_client):
    """Список отправлений в акте"""
    request_data = fbs_act_get_postings_request(id=id)
    response = await api_client.request('POST', 'https://api-seller.ozon.ru/v2/posting/fbs/act/get-postings', request_data.model_dump())
    print(response)


async def supply_order_list(page, page_size, states, api_client):
    """Список заявок на поставку на склад Ozon"""
    request_data = supply_order_list_request(page=page, page_size=page_size, states=states)
    response = await api_client.request('POST', 'https://api-seller.ozon.ru/v1/supply-order/list', request_data.model_dump())
    print(response)

async def supply_order_get(supply_order_id, api_client):
    """Информация о заявке на поставку"""
    request_data = supply_order_get_request(supply_order_id=supply_order_id)
    response = await api_client.request('POST', 'https://api-seller.ozon.ru/v1/supply-order/get', request_data.model_dump())
    print(response)


async def supply_order_items(page, page_size, supply_order_id, api_client):
    """Список товаров в заявке на поставку"""
    request_data = supply_order_items_request(page=page, page_size=page_size, supply_order_id=supply_order_id)
    response = await api_client.request('POST', 'https://api-seller.ozon.ru/v1/supply-order/items', request_data.model_dump())
    print(response)


async def seller_rating_summary(group_name, direction, meaning, current_value, name, past_value, rating, rating_direction, status, value_type, penalty_score_exceeded, premium, api_client):
    """Получение информации о текущих рейтингах продавца"""
    request_data = seller_rating_summary_request(
    groups=seller_rating_summary_group(
        group_name=group_name, 
        items=[seller_rating_summary_items(
            change=change_class(
                direction=direction, 
                meaning=meaning), 
            current_value=current_value, 
            name=name, 
            past_value=past_value, 
            rating=rating, 
            rating_direction=rating_direction, 
            status=status, 
            value_type=value_type)]), 
    penalty_score_exceeded=penalty_score_exceeded, 
    premium=premium)
    
    response = await api_client.request('POST', 'https://api-seller.ozon.ru/v1/rating/summary', request_data.model_dump())
    print(response)


async def rating_history(date_from, date_to, ratings, with_premium_scores, api_client):
    """Получить информацию о рейтингах продавца за период"""
    request_data = rating_history_request(date_from=date_from, date_to=date_to, ratings=ratings, with_premium_scores=with_premium_scores)
    response = await api_client.request('POST', 'https://api-seller.ozon.ru/v1/rating/history', request_data.model_dump())
    print(response)


async def report_product_create(language, offer_id, search, sku, visibility, api_client):
    """Метод для получения отчёта с данными о товарах. Например, Ozon ID, количества товаров, цен, статуса."""
    request_data = report_product_create_request(language=language, offer_id=offer_id, search=search, sku=sku, visibility=visibility)
    response = await api_client.request('POST','https://api-seller.ozon.ru/v1/report/products/create', request_data.model_dump())
    print(response)



async def report_returns_create(delivery_schema, order_id, status, language, api_client):
    """Метод для получения отчёта о возвратах товара"""
    request_data = report_returns_create_request(delivery_schema=delivery_schema, order_id=order_id, status=status, language=language)
    response = await api_client.request('POST','https://api-seller.ozon.ru/v1/report/returns/create', request_data.model_dump())
    print(response)


# ФУНКЦИЯ НЕ ЗАБУДЬ ДОДЕЛАТЬ 
async def report_postings_create(cancel_reason_id, delivery_schema, offer_id, processed_at_from, processed_at_to, sku, status_alias, statuses, title, language, api_client):
    """Отчёт об отправлениях с информацией по заказам"""
    request_data = report_postings_create_request(filter=report_postings_creater_filter(cancel_reason_id=cancel_reason_id,delivery_schema=delivery_schema, offer_id=offer_id, processed_at_from=processed_at_from,processed_at_to=processed_at_to,sku=sku,status_alias=status_alias,statuses=statuses,title=title),language = language)
    
    response = await api_client.request('POST','https://api-seller.ozon.ru/v1/report/postings/create', request_data.model_dump())
    print(response)



async def finance_statement_list(from_, to, page, with_details, page_size, api_client):
    """Метод для получения финансового отчёта"""
    request_data = finance_statement_list_request(date=finance_statement_list_date(from_=from_, to=to), page=page, with_details=with_details, page_size=page_size)
    
    response = await api_client.request('POST','https://api-seller.ozon.ru/v1/finance/cash-flow-statement/list', request_data.model_dump())
    print(response)

# async def invoice_create_or_update(HS_code:str, date:str, number:str, posting_number:str, price:float, price_currency:str, url:str, api_client):
#     """Создание или изменение ссылки на таможенный счёт-фактуру для возврата НДС продавцам из Турции"""
#     request_data = invoice_create_or_update_request(HS_code, date, number, posting_number, price, price_currency, url)
    
#     response = await api_client.request('POST','https://api-seller.ozon.ru/v1/invoice/create-or-update', request_data.model_dump())
#     print(response)


async def invoice_create_or_update(HS_code, date, number, posting_number, price, price_currency, url, api_client):
    """Создание или изменение ссылки на таможенный счёт-фактуру для возврата НДС продавцам из Турции""" 
    request_data = invoice_create_or_update_request(HS_code=HS_code, date=date, number=number, posting_number=posting_number, price=price, price_currency=price_currency, url=url)
    response = await api_client.request('POST', 'https://api-seller.ozon.ru/v1/invoice/create-or-update', request_data.model_dump())
    print(response)

async def invoice_get(posting_number, api_client):
    """Получить ссылку на счёт-фактуру"""
    request_data = invoice_get_request(posting_number=posting_number)
    response = await api_client.request('POST', 'https://api-seller.ozon.ru/v1/invoice/get', request_data.model_dump())
    print(response)

async def invoice_delete(posting_number, api_client):
    """Удалить ссылку на счёт-фактуру"""
    request_data = invoice_delete_request(posting_number=posting_number)
    response = await api_client.request('POST', 'https://api-seller.ozon.ru/v1/invoice/delete', request_data.model_dump())
    print(response)

async def main():
    api_client = APIClient('https://api-seller.ozon.ru', {'Client-Id': "YOUR CLIENT-ID", 'Api-Key': "YOUR API-KEY"})
    #Call the function here

asyncio.run(main())

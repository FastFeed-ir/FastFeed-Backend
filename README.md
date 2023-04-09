This file contains:

1.All apps and their APIs in this project<br>
2.All HTTP methods used in this project and their work<br>
3.Description of each API in each app in detail<br>
______________________________________________________________________________________________________________

# All apps:

## store app

Store API : For handling the stores<br>

## menu app

Collection API: For handling the collections of all stores and the collections of a specified store<br>
Product API: For handling the products of all stores and collections,and the products of a specified store or
collection<br>

## comment app<br>

Comment API: For handling the comments of all orders and the comments of a specified order<br>
Rating API: For handling the ratings of all products and the rating of a specified product<br>

## subs app

Subscription API: For handling the subscriptions of all stores and the subscription of a specified store<br>

## owner app

BusinessOwner API: For handling the business owners(store owners)<br>

## order app <br>

Order API: For handling the orders of all stores and the orders of a specified store<br>
OrderItem API: For handling the order items of all orders and the order items of a specified order<br>
______________________________________________________________________________________________________________

# All HTTP methods:

1.**POST method** : For creating a new object<br>
2.**PUT method** : For updating all fields of an existing object<br>
3.**PATCH method** : For updating a subset of an existing object's fields<br>
4.**GET method** : For retrieving an existing object<br>
5.**DELETE method** : For deleting an existing object<br>
______________________________________________________________________________________________________________

# Description of each API in each app in detail:

**Note: images are not supported yet.**

## store app:<br>

**APIs**:<br>
Store API:<br>

### the arguments needed: <br>

title: string(char field 32): required
business_owner: int: required:
    1=> cafe
    2=> restaurant
business_type: int: required
state: int: required:
    chosen from [constants.py](./utilities/constants.py )
city: string(char field 32): optional
address: string(char field 1024): optional
telephone_number: string(char field 32): required
tables_count: int: required
instagram_page_link: string(char field 64): optional
telegram_channel_link: string(char field 64): optional

**if 201 in Response body server send you store which created(with id and other only read fields)**

## Store API:

### POST method:<br>

specified URL:
```<baseURL>/stores/```

Data example:<br>

```
    {
        "title": "کبابی عمو حسن",
        "business_type": 2,
        "business_owner": 1,
        "telephone_number": "031311122233",
        "tables_count": 5,
        "state":4,
        "logo": "null",
        "city": "کاشان",
        "address": "نبش خیابان مدرس",
        "instagram_page_link": "@test",
        "telegram_channel_link": "@test"
    }
```

Status codes:```201``` ```400```

### PUT method

specified URL:
```<baseURL>/stores/```
Data example:
```
    {
        "title": "کبابی عمو حسن",
        "business_type": 2,
        "business_owner": 1,
        "telephone_number": "031311122233",
        "tables_count": 5,
        "state":4,
        "logo": "null",
        "city": "کاشان",
        "address": "نبش خیابان مدرس",
        "instagram_page_link": "@test",
        "telegram_channel_link": "@test"
    }
```
Status codes:
202
400
404

### PATCH method

specified URL:
```<baseURL>/stores/```
Data example:
```
    {
        "title": "کبابی عمو حسن",
        "business_type": 2,
        "business_owner": 1,
        "telephone_number": "031311122233",
        "tables_count": 5,
        "state":4,
        "logo": "null",
        "city": "کاشان",
        "address": "نبش خیابان مدرس",
        "instagram_page_link": "@test",
        "telegram_channel_link": "@test"
    }
```
Status codes:
202
400
404

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
GET method:
specified URL:
```<baseURL>/stores/```
```<baseURL>/stores/<ID>/```
Status codes:
200
404
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

DELETE method
specified URL:
```<baseURL>/stores/<ID>/```
Status codes:
204
404
______________________________________________________________________________________________________________
## menu app:<br>

**APIs**:<br>
Collection API:<br>
Product API:<br>
========================================================================
## Collection API

### the arguments needed: <br>
store: int: required
title: string(char field 32): required
is_featured: bool: optional



POST method:
specified URL:
```<baseURL>/collections/```
Data example:
```
    {
        "title": "cakes",
        "store": "Nuveen Core Equity Alpha Fund",
        "is_featured": false
    }
```
Status codes:
201
400

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
PUT method:
specified URL:
```<baseURL>/collections/<ID>/```

Data example:
```
    {
        "title": "cakes",
        "store": "Nuveen Core Equity Alpha Fund",
        "is_featured": false
    }
```
Status codes:
202
400
404
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

PATCH method:
specified URL:
```<baseURL>/collections/<ID>/```

Data example:
```
    {
        "is_featured": false
    }
```
Status codes:
202
400
404

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
GET method:
specified URL:
```<baseURL>/collections/```
```<baseURL>/collections/<ID>/```
Status codes:
200
404
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

DELETE method:
specified URL:
```<baseURL>/collections/<ID>/```
Status codes:
204
404
========================================================================
## Product API

### the arguments needed: <br>

title: string(char field 32): required
unit_price: decimal: required
collection: int: required
is_available: bool: required
is_featured: bool: optional
description: string(char field 1024): optional
inventory: positive small int: optional
discount_percentage: int: optional

POST method:
specified URL:
```<baseURL>/products/```
Data example:
```
    {
        "title": "chocolate cake",
        "description": "Quisque id justo sit amet sapien dignissim vestibulum. Vestibulum ante ipsum primis in faucibus orci
        luctus et ultrices posuere cubilia Curae; Nulla dapibus dolor vel est. Donec odio justo, sollicitudin ut, suscipit a,
        feugiat et, eros.",
        "unit_price": 41,
        "inventory": 53,
        "is_available": true,
        "is_featured": false,
        "discount_percentage": 27,
        "collection": "cakes"
    }
```
Status codes:
201
400

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
PUT method
specified URL:
```<baseURL>/products/<ID>/```
Data example:
```
    {
        "title": "chocolate cake",
        "description": "Quisque id justo sit amet sapien dignissim vestibulum. Vestibulum ante ipsum primis in faucibus orci
        luctus et ultrices posuere cubilia Curae; Nulla dapibus dolor vel est. Donec odio justo, sollicitudin ut, suscipit a,
        feugiat et, eros.",
        "unit_price": 41,
        "inventory": 53,
        "is_available": true,
        "is_featured": false,
        "discount_percentage": 27,
        "collection": "cakes"
    }
```
Status codes:
202
400
404
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

PATCH method
specified URL:
```<baseURL>/products/<ID>/```
Data example:
```
    {
        "is_available": true,
        "is_featured": false,
        "discount_percentage": 27
    }
```
Status codes:
202
400
404

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
GET method:
specified URL:
http://localhost:8000/products/
http://localhost:8000/products/<ID>/
Status codes:
200
404
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

DELETE method
specified URL:
```<baseURL>/products/<ID>/```
Status codes:
204
404
______________________________________________________________________________________________________________
## comment app:<br>

**APIs**:<br>
Comment API:<br>
Rating API:<br>
========================================================================
## Comment API

### the arguments needed: <br>

name: string(char field 32): required
content: string(char field 1024): required

POST method:
specified URL:
```<baseURL>/comments/```
Data example:
```
    {
        "name": "Ardis Hamman",
        "content": "Maecenas leo odio, condimentum id, luctus nec, molestie sed, justo. Pellentesque viverra pede ac diam. Cras
        pellentesque volutpat dui.\n\nMaecenas tristique, est et tempus semper, est quam pharetra magna, ac consequat metus
        sapien ut nunc. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Mauris viverra
        diam vitae quam. Suspendisse potenti."
    }
```
Status codes:
201
400

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
GET method:
specified URL:
```<baseURL>/comments/```
```<baseURL>/comments/<ID>/```
Status codes:
200
404
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

DELETE method:
specified URL:
```<baseURL>/comments/<ID>/```
Status codes:
204
404
========================================================================
Rating API

POST method:
specified URL:
http://localhost:8000/ratings/
Data example:
{
"id": 1,
"product": "chocolate cake",
"score": 5,
"created_at": 2021-08-14 14:25:00
}
Status codes:
201
400

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
GET method:
specified URL:
http://localhost:8000/ratings/
http://localhost:8000/ratings/<ID>/
Status codes:
200
404
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

DELETE method:
specified URL:
http://localhost:8000/ratings/<ID>/
Status codes:
204
404
______________________________________________________________________________________________________________
4.subs app:
APIs:
Subscription API
========================================================================
Subscription API

POST method:
specified URL:
http://localhost:8000/subscriptions/
Data example:
{
"id": 1,
"store": 1,
"period": 90,
"amount": "2000.0",
"url":"http://localhost:8000/stores/5/",
"start_date": "2021-08-14 14:25:00"
"created_at": 2021-08-14 14:25:00,
"updated_at": 2021-08-14 14:25:00
}
Status codes:
201
400

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
PUT method:
specified URL:
http://localhost:8000/subscriptions/<ID>/
Data example:
    {
        "id": 1,
        "store": 1,
        "period": 90,
        "amount": "2000.0",
        "url":"http://localhost:8000/stores/5/",
        "start_date": "2021-08-14 14:25:00"
        "created_at": 2021-08-14 14:25:00,
        "updated_at": 2021-08-14 14:25:00
    }
Status codes:
201
400
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

PATCH method:
specified URL:
http://localhost:8000/subscriptions/<ID>/
Data example:
{
"amount": "2000.0",
"url":"http://localhost:8000/stores/5/",
"start_date": "2021-08-14 14:25:00"
"updated_at": 2021-08-14 14:25:00
}
Status codes:
201
400

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
GET method:
specified URL:
http://localhost:8000/subs/
http://localhost:8000/subs/<ID>/
Status codes:
200
404
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

DELETE method:
specified URL:
http://localhost:8000/subs/
http://localhost:8000/subs/<ID>/
Status codes:
204
404
______________________________________________________________________________________________________________
5.owner app:
APIs:
BusinessOwner API
========================================================================
BusinessOwner API

POST method:
specified URL:
http://localhost:8000/owners/
Data example:
{
"id": 1,
"first_name": "علی",
"last_name": "رهی",
"phone_number": "09398506609",
"created_at": 2021-08-14 14:25:00,
"updated_at": 2021-08-14 14:25:00
}
Status codes:
201
400

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
PUT method:
specified URL:
http://localhost:8000/owners/<ID>/
Data example:
    {
        "id": 1,
        "first_name": "علی",
        "last_name": "رهی",
        "phone_number": "09398506609",
        "created_at": 2021-08-14 14:25:00,
        "updated_at": 2021-08-14 14:25:00
}
Status codes:
202
400
404
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

PATCH method:
specified URL:
http://localhost:8000/owners/<ID>/
Data example:
{
"first_name": "علی",
"last_name": "رهی",
"updated_at": 2021-08-14 14:25:00
}
Status codes:
202
400
404

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
GET method:
specified URL:
http://localhost:8000/owners/
http://localhost:8000/owners/<ID>/
Status codes:
200
404
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

### DELETE

specified URL:
http://localhost:8000/owners/
http://localhost:8000/owners/<ID>/
Status codes:
204
404
______________________________________________________________________________________________________________
6.order app:
APIs:
Order API
OrderItem API
========================================================================
Order API

POST method:
specified URL:
http://localhost:8000/orders/
Data example:
{
"id": 1,
"store": 1,
"table_number": 6,
"description": "فغدقبسذیرس",
"auth_code": 76543,
"created_at": 2021-08-14 14:25:00,
"created_at_shamsi": "یک فروردین 1402",
"updated_at": 2021-08-14 14:25:00
}
Status codes:
201
400

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
PUT method:
specified URL:
http://localhost:8000/orders/<ID>/
Data example:
    {
        "id": 1,
        "store": 1,
        "table_number": 6,
        "description": "فغدقبسذیرس",
        "auth_code": 76543,
        "created_at": 2021-08-14 14:25:00,
        "created_at_shamsi": "یک فروردین 1402",
        "updated_at": 2021-08-14 14:25:00
    }
Status codes:
202
400
404
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

PATCH method:
specified URL:
http://localhost:8000/orders/<ID>/
Data example:
{
"table_number": 6,
"updated_at": 2021-08-14 14:25:00
}
Status codes:
202
400
404

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
GET method:
specified URL:
http://localhost:8000/orders/
http://localhost:8000/orders/<ID>/
Status codes:
200
404
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

### DELETE

specified URL:
http://localhost:8000/orders/
http://localhost:8000/orders/<ID>/
Status codes:
204
404
========================================================================
OrderItem API

POST method:
specified URL:
http://localhost:8000/order-items/
Data example:
{
"id": 1,
"order": 1,
"product": 6,
"quantity": 2,
"created_at": 2021-08-14 14:25:00
}
Status codes:
201
400

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
GET method:
specified URL:
http://localhost:8000/order-items/
http://localhost:8000/order-items/<ID>/
Status codes:
200
404
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

### DELETE

specified URL:
http://localhost:8000/order-items/
http://localhost:8000/order-items/<ID>/
Status codes:
204
404
______________________________________________________________________________________________________________
##SMS verification activation

1.Sign in to sms.ir
2.Install smsir in project(no need to add it to INSTALLED_APPS)
3.Set SMSIR_API_KEY, SMSIR_PHONE_NUMBER, SMSIR_API_URL values in the settings.py module, based on your sms.ir account

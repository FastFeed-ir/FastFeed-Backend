**This file contains:**

- All apps and their APIs in this project
- All HTTP methods used in this project and their functionality
- Description of every API in each app in detail
- SMS verification activation using Django

***

# All apps:

## store app

Store API: For handling the stores<br>

## menu app

Collection API: For handling the collections of all stores and the collections of a specified store<br>
Product API: For handling the products of all stores and collections,and the products of a specified store or
collection

## comment app

Comment API: For handling the comments of all orders and the comments of a specified order<br>
Rating API: For handling the ratings of all products and the rating of a specified product

## subs app

Subscription API: For handling the subscriptions of all stores and the subscription of a specified store<br>

## owner app

BusinessOwner API: For handling the business owners(store owners)<br>

## order app

Order API: For handling the orders of all stores and the orders of a specified store<br>
OrderItem API: For handling the order items of all orders and the order items of a specified order

***

# All HTTP methods:

- POST method: For creating a new object
- PUT method: For updating all fields of an existing object
- PATCH method: For updating a subset of an existing object's fields
- GET method: For retrieving an existing object
- DELETE method: For deleting an existing object

***

# Description of every API in each app in detail:

**Note: Images are not supported yet.**<br>
**Note: If the response body contains the status code of ```201```, 
it means that the server has sent you the respective object that was created, 
including id and other read-only fields.**

## store app:

**API(s)**:
- Store API

---

### Store API:

#### The arguments needed:
- title: string (char field 32): required
- business_type: int: required
    - 1 => cafe
    - 2 => restaurant
- state: int: required:
    - chosen from [constants.py](./utilities/constants.py)
- city: string (char field 32): optional
- address: string (char field 1024): optional
- telephone_number: string (char field 32): required
- owner_phone_number: string (char field 20): required
- tables_count: int: required
- instagram_page_link: string (char field 64): optional

#### HTTP methods:

###### POST method:

specified URL(s):
```<baseURL>/stores/```

Data example:
```
    {
        "title": "کبابی عمو حسن",
        "business_type": 2,
        "business_owner": 1,
        "telephone_number": "031311122233",
        "owner_phone_number": "09398506609",
        "tables_count": 5,
        "state": 4,
        "city": "کاشان",
        "address": "نبش خیابان مدرس",
        "instagram_page_link": "@test"
}
```

Status codes:
```201```
```400```

###### PUT method:

specified URL(s):
```<baseURL>/stores/```

Data example:
```
    {
        "title": "کبابی عمو حسن",
        "business_type": 2,
        "business_owner": 1,
        "telephone_number": "031311122233",
        "owner_phone_number": "09398506609",
        "tables_count": 5,
        "state":4,
        "city": "کاشان",
        "address": "نبش خیابان مدرس",
        "instagram_page_link": "@test"
    }
```

Status codes:
```202```
```400```
```404```

###### PATCH method:

specified URL(s):
```<baseURL>/stores/```

Data example:
```
    {
        "title": "کبابی عمو حسن",
        "business_type": 2,
        "business_owner": 1,
        "telephone_number": "031311122233",
        "address": "نبش خیابان مدرس",
        "instagram_page_link": "@test"
    }
```

Status codes:
```202```
```400```
```404```

###### GET method:

specified URL(s):
```<baseURL>/stores/```
```<baseURL>/stores/<ID>/```

Status codes:
```200```
```404```

###### DELETE method:

specified URL(s):
```<baseURL>/stores/<ID>/```

Status codes:
```204```
```404```

***

## menu app:

**API(s)**:
- Collection API
- Product API

---

### Collection API:

#### The arguments needed:
- title: string(char field 32): required
- is_featured: bool: optional

#### HTTP methods:

###### POST method:

specified URL(s):
```<baseURL>/collections/```

Data example:
```
    {
        "title": "cakes",
        "is_featured": false
    }
```
Status codes:```201``` ```400```

###### PUT method:

specified URL(s):
```<baseURL>/collections/<ID>/```

Data example:
```
    {
        "title": "cakes",
        "is_featured": false
    }
```

Status codes:```202``` ```400``` ```404```

###### PATCH method:

specified URL(s):
```<baseURL>/collections/<ID>/```

Data example:
```
    {
        "is_featured": false
    }
```

Status codes:
```202```
```400```
```404```

###### GET method:

specified URL(s):
```<baseURL>/collections/```
```<baseURL>/collections/<ID>/```

Status codes:
```200```
```404```

###### DELETE method:

specified URL(s):
```<baseURL>/collections/<ID>/```

Status codes:
```204```
```404```

---

### Product API:

#### The arguments needed:
- title: string(char field 32): required
- unit_price: decimal(max_digits=15, decimal_places=3): required
- is_available: bool: required
- is_featured: bool: optional
- description: string(char field 1024): optional
- inventory: positive small int: optional
- discount_percentage: decimal(max_digits=5, decimal_places=2): optional

#### HTTP methods:

###### POST method:

specified URL(s):
```<baseURL>/products/```

Data example:
```
    {
        "title": "chocolate cake",
        "description": "Quisque id justo sit amet sapien dignissim vestibulum.",
        "unit_price": 41,
        "inventory": 53,
        "is_available": true,
        "is_featured": false,
        "discount_percentage": 27
    }
```

Status codes:
```201```
```400```

###### PUT method:

specified URL:
```<baseURL>/products/<ID>/```

Data example:
```
    {
        "title": "chocolate cake",
        "description": "Quisque id justo sit amet sapien dig",
        "unit_price": 41,
        "inventory": 53,
        "is_available": true,
        "is_featured": false,
        "discount_percentage": 27,
    }
```

Status codes:
```202```
```400```
```404```

###### PATCH method:

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
```202```
```400```
```404```

###### GET method:

specified URL:
```<baseURL>/products/```
```<baseURL>/products/<ID>/```

Status codes:
```200```
```404```

###### DELETE method:

specified URL:
```<baseURL>/products/<ID>/```

Status codes:
```204```
```404```

***

## comment app:

**API(s)**:
- Comment API
- Rating API

---

### Comment API:

#### The arguments needed:
- name: string(char field 32): required
- content: string(char field 1024): required

#### HTTP methods:

###### POST method:

specified URL:
```<baseURL>/comments/```

Data example:
```
    {
        "name": "Ardis Hamman",
        "content": "Maecenas leo odio."
    }
```

Status codes:
```201```
```400```

###### GET method:

specified URL:
```<baseURL>/comments/```
```<baseURL>/comments/<ID>/```

Status codes:
```200```
```404```

###### DELETE method:

specified URL:
```<baseURL>/comments/<ID>/```

Status codes:
```204```
```404```

---

### Rating API:

#### The arguments needed:
- score: int (1-5): required

#### HTTP methods:

###### POST method:

specified URL:
```<baseURL>/ratings/```

Data example:
```
    {
        "score": 5
    }
```

Status codes:
```201```
```400```

###### GET method:

specified URL:
```<baseURL>/ratings/```
```<baseURL>/ratings/<ID>/```

Status codes:
```200```
```404```

###### DELETE method:

specified URL:
```<baseURL>/ratings/<ID>/```

Status codes:
```204```
```404```

***

## subs app:

**API(s)**:
- Subscription API

---

### Subscription API:

#### The arguments needed:
- period: positive int: required
- amount: decimal(max_digits=20, decimal_places=3): optional

#### HTTP methods:

###### POST method:

specified URL:
```<baseURL>/subscription/```

Data example:
```
    {
        "period": 90,
        "amount": "2000.0"
    }
```

Status codes:
```201```
```400```

###### PUT method:

specified URL:
```<baseURL>/subscription/<ID>/```

Data example:
```
    {
        "period": 80,
        "amount": "3000.0"
    }
```

Status codes:
```201```
```400```

###### PATCH method:

specified URL:
```<baseURL>/subscription/<ID>/```

Data example:
```
    {
        "amount": "2000.0"
    }
```

Status codes:
```201```
```400```

###### GET method:

specified URL:
```<baseURL>/subscription/```
```<baseURL>/subscription/<ID>/```

Status codes:
```200```
```404```

###### DELETE method:

specified URL:
```<baseURL>/subscription/```
```<baseURL>/subscription/<ID>/```

Status codes:
```204```
```404```

***

## owner app:

**API(s)**:
- BusinessOwner API

---

### BusinessOwner API:

#### The arguments needed:
- first_name: string (char field 50): optional
- last_name: string (char field 50): optional
- phone_number: string (char field 20): required

#### HTTP methods:

###### POST method:

specified URL:
```<baseURL>/owners/```

Data example:
```
    {
        "first_name": "علی",
        "last_name": "رهی",
        "phone_number": "09398506609"
    }
```

Status codes:
```201```
```400```

###### PUT method:

specified URL:
```<baseURL>/owners/<ID>/```

Data example:
```
    {
        "first_name": "علی",
        "last_name": "رهی",
        "phone_number": "09398506609"
    }
```

Status codes:
```201```
```400```

###### PATCH method:

specified URL:
```<baseURL>/owners/<ID>/```

Data example:
```
    {
        "phone_number": "09398506609"
    }
```

Status codes:
```201```
```400```

###### GET method:

specified URL:
```<baseURL>/owners/```
```<baseURL>/owners/<ID>/```

Status codes:
```200```
```404```

###### DELETE method:

specified URL:
```<baseURL>/owners/<ID>/```

Status codes:
```204```
```404```

***

## order app:

**API(s)**:
- Order API
- OrderItem API

---

### Order API:

#### The arguments needed:
- table_number: positive int: required
- description: string (char field 1024): optional

#### HTTP methods

###### POST method:

specified URL:
```<baseURL>/orders/```

Data example:
```
    {
        "table_number": 6,
        "description": "فغدقبسذیرس"
    }
```

Status codes:
```201```
```400```

###### PUT method:

specified URL:
```<baseURL>/orders/<ID>/```

Data example:
```
    {
        "table_number": 7,
        "description": "فغدثغفدقلذیبسذیرس"
    }
```

Status codes:
```201```
```400```

###### PATCH method:

specified URL:
```<baseURL>/owners/<ID>/```

Data example:
```
    {
        "table_number": 5
    }
```

Status codes:
```201```
```400```

###### GET method:

specified URL:
```<baseURL>/orders/```
```<baseURL>/orders/<ID>/```

Status codes:
```200```
```404```

###### DELETE method:

specified URL:
```<baseURL>/orders/<ID>/```

Status codes:
```204```
```404```

---

### OrderItem API:

#### The arguments needed:
- quantity: positive small int: required

#### HTTP methods:

###### POST method:

specified URL:
```<baseURL>/order-items/```

Data example:
```
    {
        "quantity": 2
    }
```

Status codes:
```201```
```400```

###### GET method:

specified URL:
```<baseURL>/order-items/```
```<baseURL>/order-items/<ID>/```

Status codes:
```200```
```404```

###### DELETE method:

specified URL:
```<baseURL>/order-items/<ID>/```

Status codes:
```204```
```404```

***

# SMS verification activation using Django:

## Steps:
- Sign in to sms.ir
- Install smsir in the project
- Set SMSIR_API_KEY, SMSIR_PHONE_NUMBER, and SMSIR_API_URL values in the settings.py module, using your sms.ir account info


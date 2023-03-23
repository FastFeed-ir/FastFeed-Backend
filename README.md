
## Subscribtion API

### POST
URL:
```
http://localhost:8000/subs/
```
Data example:
```
{
"store":1,
"period":90,
"amount":"2000.0"
}
```
Status codes:
```
201
400
```
### GET
URL:
```
http://localhost:8000/subs/
http://localhost:8000/subs/<ID>/
```
Status codes:
```
200
404
```
### PUT
URL:
```
http://localhost:8000/subs/<ID>/
```
Data example:
```
{
  "last_extension": 45,
  "amount": 4000.0
}
```
Status codes:
```
202
400
404
```
### DELETE
URL:
```
http://localhost:8000/subs/
http://localhost:8000/subs/<ID>/
```
Status codes:
```
204
404
```

## Cafe/Resturant Owner API

### POST
URL:
```
http://localhost:8000/cro/
```
Data example:
```
{
  "business_type": "Restaurant",
  "first_name": "علی",
  "last_name": "رهی",
  "phone_number": "09398506609"
}
```
Status codes:
```
201
400
```
### GET
URL:
```
http://localhost:8000/cro/
http://localhost:8000/cro/<ID>/
```
Status codes:
```
200
404
```
### PUT
URL:
```
http://localhost:8000/cro/<ID>/
```
Data example:
```
{
  "business_type": "Cafe",
    "first_name": "علی",
  "last_name": "رهی",
  "phone_number": "09398506609"
}
```
Status codes:
```
202
400
404
```
### DELETE
URL:
```
http://localhost:8000/subs/
http://localhost:8000/subs/<ID>/
```
Status codes:
```
204
404
```


## Store API

### POST
URL:
```
http://localhost:8000/stores/
```
Data example:
```
    {
        "id": 1,
        "title": "Energy Recovery, Inc.",
        "logo": "profile_pictures/my_profile_picture.jpg",
        "telephone_number": "384-776-0164",
        "tables_count": 1,
        "instagram_page_link": "https://businesswire.com/eget/congue/eget/semper/rutrum/nulla/nunc.xml?eget=in&rutrum=magna&at=bibendum&lorem=imperdiet&integer=nullam&tincidunt=orci&ante=pede&vel=venenatis&ipsum=non",
        "telegram_channel_link": "http://kickstarter.com/orci/luctus/et/ultrices.aspx?velit=lacus&vivamus=purus&vel=aliquet&nulla=at&eget=feugiat&eros=non&elementum=pretium&pellentesque=quis&quisque=lectus&porta=suspendisse&volutpat=potenti&erat=in&quisque=eleifend&erat=quam&eros=a&viverra=odio&eget=in&congue=hac&eget=habitasse&semper=platea&rutrum=dictumst&nulla=maecenas&nunc=ut&purus=massa&phasellus=quis&in=augue&felis=luctus&donec=tincidunt&semper=nulla&sapien=mollis&a=molestie",
        "city": "Žďár",
        "address": "788 Oak Road",
        "subscription_factor": 67.16,
        "created_at": 2021-08-14 14:25:00
        "updated_at": 2021-08-14 14:25:00
    }
```
Status codes:
```
201
400
```
### GET
URL:
```
http://localhost:8000/stores/
http://localhost:8000/stores/<ID>/
```
Status codes:
```
200
404
```
### PUT
URL:
```
http://localhost:8000/stores/<ID>/
```
Data example:
```
    {
        "id": 1,
        "title": "Energy Recovery, Inc.",
        "logo": null,
        "telephone_number": "384-776-0164",
        "tables_count": 1,
        "instagram_page_link": "https://businesswire.com/eget/congue/eget/semper/rutrum/nulla/nunc.xml?eget=in&rutrum=magna&at=bibendum&lorem=imperdiet&integer=nullam&tincidunt=orci&ante=pede&vel=venenatis&ipsum=non",
        "telegram_channel_link": "http://kickstarter.com/orci/luctus/et/ultrices.aspx?velit=lacus&vivamus=purus&vel=aliquet&nulla=at&eget=feugiat&eros=non&elementum=pretium&pellentesque=quis&quisque=lectus&porta=suspendisse&volutpat=potenti&erat=in&quisque=eleifend&erat=quam&eros=a&viverra=odio&eget=in&congue=hac&eget=habitasse&semper=platea&rutrum=dictumst&nulla=maecenas&nunc=ut&purus=massa&phasellus=quis&in=augue&felis=luctus&donec=tincidunt&semper=nulla&sapien=mollis&a=molestie",
        "city": "Žďár",
        "address": "788 Oak Road",
        "subscription_factor": 67.16,
        "created_at": 2021-08-14 14:25:00
        "updated_at": 2021-08-14 14:25:00
    }
```
Status codes:
```
202
400
404
```
### DELETE
URL:
```
http://localhost:8000/stores/<ID>/
```
Status codes:
```
204
404
```

## Collection API

### POST
URL:
```
http://localhost:8000/collections/
```
Data example:
```
{
  "id": 1,
  "title": "cakes",
  "store": "Nuveen Core Equity Alpha Fund",
  "is_featured": false,
  "created_at": 2021-08-14 14:25:00
  "updated_at": 2021-08-14 14:25:00
}
```
Status codes:
```
201
400
```
### GET
URL:
```
http://localhost:8000/collections/
http://localhost:8000/collections/<ID>/
```
Status codes:
```
200
404
```
### PUT
URL:
```
http://localhost:8000/collections/<ID>/
```
Data example:
```
{
  "id": 1,
  "title": "cakes",
  "store": "Nuveen Core Equity Alpha Fund",
  "is_featured": false,
  "created_at": 2021-08-14 14:25:00
  "updated_at": 2021-08-14 14:25:00
}
```
Status codes:
```
202
400
404
```
### DELETE
URL:
```
http://localhost:8000/collections/<ID>/
```
Status codes:
```
204
404
```

## Product API

### POST
URL:
```
http://localhost:8000/products/
```
Data example:
```
{
  "id": 1,
  "title": "chocolate cake",
  "description": "Quisque id justo sit amet sapien dignissim vestibulum. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Nulla dapibus dolor vel est. Donec odio justo, sollicitudin ut, suscipit a, feugiat et, eros.",
  "unit_price": 41,
  "inventory": 53,
  "is_available": true,
  "is_featured": false,
  "discount_percentage": 27,
  "store": "Brookfield Infrastructure Partners LP",
  "collection": "cakes"
  "created_at": 2021-08-14 14:25:00
  "updated_at": 2021-08-14 14:25:00
}
```
Status codes:
```
201
400
```
### GET
URL:
```
http://localhost:8000/products/
http://localhost:8000/products/<ID>/
```
Status codes:
```
200
404
```
### PUT
URL:
```
http://localhost:8000/products/<ID>/
```
Data example:
```
{
  "id": 1,
  "title": "chocolate cake",
  "description": "Quisque id justo sit amet sapien dignissim vestibulum. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Nulla dapibus dolor vel est. Donec odio justo, sollicitudin ut, suscipit a, feugiat et, eros.",
  "unit_price": 41,
  "inventory": 53,
  "is_available": true,
  "is_featured": false,
  "discount_percentage": 27,
  "store": "Brookfield Infrastructure Partners LP",
  "collection": "cakes"
  "created_at": 2021-08-14 14:25:00
  "updated_at": 2021-08-14 14:25:00
}
```
Status codes:
```
202
400
404
```
### DELETE
URL:
```
http://localhost:8000/products/<ID>/
```
Status codes:
```
204
404
```

## Comment API

### POST
URL:
```
http://localhost:8000/comments/
```
Data example:
```
{
  "id": 1,
  "name": "Ardis Hamman",
  "content": "Maecenas leo odio, condimentum id, luctus nec, molestie sed, justo. Pellentesque viverra pede ac diam. Cras pellentesque volutpat dui.\n\nMaecenas tristique, est et tempus semper, est quam pharetra magna, ac consequat metus sapien ut nunc. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Mauris viverra diam vitae quam. Suspendisse potenti.",
  "product": "chocolate cake"
  "created_at": 2021-08-14 14:25:00
}
```
Status codes:
```
201
400
```
### GET
URL:
```
http://localhost:8000/comments/
http://localhost:8000/comments/<ID>/
```
Status codes:
```
200
404
```
### DELETE
URL:
```
http://localhost:8000/comments/<ID>/
```
Status codes:
```
204
404
```

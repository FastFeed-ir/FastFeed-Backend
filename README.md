
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


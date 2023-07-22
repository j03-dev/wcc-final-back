# API doc

## Endpoints

- `POST api/v1/user/login`

Request : 
```
{
    "username": "Gracy",
    "password": "xyz",
}

```
Response : 
```
{
    "token" : jflkajslkdfjlkajsdlkfjdsf,
}
```

- `POST api/v1/user/register`

Request
```
{
    "username": "Gracy",
    "password": "xyz",
}
```

Response
```
{
    "success": true,
}
```

- `GET /generate`
    - Generate a clothing combination
    - Need auth

Request

| Name | Type                                   |
| ---- | -------------------------------------- |
| hot  | boolean                                |
| type | ('sport', 'plage', 'casual', 'formel') |

```
{
    "hot": false
    "type":  "sport"
}
```

Response
```
```

- `POST /api/v1/clothes`
    - Add a new one
    - Need auth

Request 
(formdata)

| Name     | Type                                   |
| -------- | -------------------------------------- |
| image    | file                                   |
| type     | ('sport', 'plage', 'casual', 'formel') |
| category | ('haut', 'bas', 'accessory', 'shoe')   |
| hot      | boolean                                |
| colors   | string                                 |

```
{
    "label": "T-shirt",
    "image": file,
    "type": "sport",
    "category": "haut",
    "hot": true
    "hexcode": "#ffffff",
}
```

Response 
```
{
    "success": true,
    "new_cloth_id": 123,
}
```
- `GET /api/v1/clothes`
    - Get all clothes of an user
    - Need token

Response
```
{
    "total":  4,
    "clothes": [
        {
            "id": 123,
            "label": "t-shirt",
            "image": "fsljl.png",
            "type": "sport",
            "category": "haut",
            "hxcode": "#fffff",
            "hot": true
        },
        {
            "id": 123,
            "label": "t-shirt",
            "image": "fsljl.png",
            "type": "sport",
            "category": "haut",
            "hxcode": "#fffff",
            "hot": true
        },
        {
            "id": 123,
            "label": "t-shirt",
            "image": "fsljl.png",
            "type": "sport",
            "category": "haut",
            "hxcode": "#fffff",
            "hot": true
        },
        {
            "id": 123,
            "label": "t-shirt",
            "image": "fsljl.png",
            "type": "sport",
            "category": "haut",
            "hxcode": "#fffff",
            "hot": true
        },
    ]
}
```
# mbola tsy vita
- `DELETE /clothes/{clothe_id}`
    - Need auth
Response
```
{
    "success": true,
}
```
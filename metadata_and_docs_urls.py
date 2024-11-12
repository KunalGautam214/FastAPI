from fastapi import FastAPI

description = """
Code with KG API helps you do awesome stuff.

## Items

You can **read items**.

## Users

You will be able to:

* **Create users** (_not implemented_).
* **Read users** (_not implemented_).
"""

app = FastAPI(
    title="Code with KG",
    description=description,
    summary="Best place to learn FastAPI.",
    version="0.0.1",
    terms_of_service="http://example.com/terms/",
    contact={
        "name": "Code with KG is awesome",
        "url": "http://x-force.example.com/contact/",
        "email": "dp@x-force.example.com",
    },
    license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    },
)

description = """
Code with KG API helps you do awesome stuff.

## Items

You can **read items**.

## Users

You will be able to:

* **Create users** (_not implemented_).
* **Read users** (_not implemented_).
"""

app = FastAPI(
    title="Code with KG",
    description=description,
    summary="Best place to learn FastAPI.",
    version="0.0.1",
    terms_of_service="http://example.com/terms/",
    contact={
        "name": "Code with KG is Amazing",
        "url": "http://x-force.example.com/contact/",
        "email": "dp@x-force.example.com",
    },
    license_info={
        "name": "Apache 2.0",
        "identifier": "MIT",
    },
)


@app.get('/items')
async def read_items():
    return {'name': 'Code with KG'}

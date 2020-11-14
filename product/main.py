import uvicorn
from ariadne.asgi import GraphQL
from ariadne.contrib.federation import make_federated_schema

from product.schema import query, type_defs

schema = make_federated_schema(type_defs, query)
app = GraphQL(schema, debug=True)

if __name__ == "__main__":
    uvicorn.run(app, port=5003)

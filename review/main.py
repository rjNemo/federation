import uvicorn
from ariadne.asgi import GraphQL
from ariadne.contrib.federation import make_federated_schema

from review.schema import query, type_defs, product, review, user

schema = make_federated_schema(type_defs, query, review, user, product)
app = GraphQL(schema, debug=True)

if __name__ == "__main__":
    uvicorn.run(app, port=5002)

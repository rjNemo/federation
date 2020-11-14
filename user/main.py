import uvicorn
from ariadne.asgi import GraphQL
from ariadne.contrib.federation import make_federated_schema

from user.schema import type_defs, query, mutation, user

schema = make_federated_schema(type_defs, query, mutation, user)
app = GraphQL(schema, debug=True)

if __name__ == "__main__":
    uvicorn.run(app, port=5001)

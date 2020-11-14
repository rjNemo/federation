from ariadne import load_schema_from_path
from user.schema.query import query
from user.schema.mutation import mutation
from user.schema.types.user import user

type_defs = load_schema_from_path("./")

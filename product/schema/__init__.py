from ariadne import load_schema_from_path
from .query import query

type_defs = load_schema_from_path("./")

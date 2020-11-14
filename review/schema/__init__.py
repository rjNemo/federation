from ariadne import load_schema_from_path

from .query import query
from .types.review import review
from .types.product import product
from .types.user import user

type_defs = load_schema_from_path("./")

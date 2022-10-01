from ninja import Schema
from ninja.orm import create_schema
from typing import List
from .models import APIResponse, Todo


class APIResponseListString(Schema):
    success: bool = None
    response: List[str] = None


TodoSchema = create_schema(Todo, name="TodoSchema")


class TodoListSchema(Schema):
    total: int = None
    items: List[TodoSchema] = None


APIResponseTodoListSchema = create_schema(APIResponse, name="APIResponseRegisterSchema", exclude=["id"], custom_fields=[("response", TodoListSchema, None)])
APIResponseTodoSchema = create_schema(APIResponse, name="APIResponseRegisterSchema", exclude=["id"], custom_fields=[("response", TodoSchema, None)])
APIResponseBoolSchema = create_schema(APIResponse, name="APIResponseRegisterSchema", exclude=["id"], custom_fields=[("response", bool, None)])

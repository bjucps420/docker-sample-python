from django.core.paginator import Paginator, EmptyPage
from todo.models import Todo
from .api import TodoSchema, APIResponseTodoListSchema, APIResponseBoolSchema, APIResponseTodoSchema
from ninja import Router


router = Router()


def translate(status):
    if status == "PENDING":
        return "Pending"
    if status == "IN_PROGRESS":
        return "In Progress"
    if status == "COMPLETE":
        return "Complete"


@router.get("list/{status}", response=APIResponseTodoListSchema)
def todo_list(request, status: str, search: str = "", groupBy: str = "", groupByDesc: str = "", sortBy: str = "title", sortDesc: str = "false", page: int = 1, mustSort: str = "", multiSort: str = "", itemsPerPage: int = 10):
    todos = Todo.objects.filter(status=translate(status))
    if search != "":
        todos = todos.filter(title__contains=search)

    sortByList = sortBy.split(",")
    sortDescList = sortDesc.split(",")
    for i in range(0, len(sortByList)):
        if sortDescList[i] == "true":
            todos = todos.order_by("-" + sortByList[i])
        else:
            todos = todos.order_by(sortByList[i])

    paginator = Paginator(todos, itemsPerPage)
    try:
        page = paginator.page(page)
        return {"success": True, "response": {"total": todos.count(), "items": list(page.object_list)}}
    except EmptyPage:
        return {"success": True, "response": {"total": todos.count(), "items": []}}


@router.post("create", response=APIResponseTodoSchema)
def create(request, data: TodoSchema):
    if request.user.has_perm("Aid"):
        return {"success": False, "errorMessage": "You are not permitted to access this action"}
    if data.id is None:
        return {"success": True, "response": Todo.objects.create(**data.dict())}
    return {"success": False, "errorMessage": "cannot update todo via create"}


@router.post("update", response=APIResponseTodoSchema)
def update(request, data: TodoSchema):
    try:
        Todo.objects.filter(id=data.id).update(**data.dict())
        return {"success": True, "response": Todo.objects.get(id=data.id)}
    except Todo.DoesNotExist:
        return {"success": False, "errorMessage": "Todo not found"}


@router.post("delete", response=APIResponseBoolSchema)
def delete(request, data: TodoSchema):
    try:
        Todo.objects.filter(id=data.id).delete()
    except Todo.DoesNotExist:
        pass
    return {"success": True, "response": True}


@router.get("{identifier}", response=APIResponseTodoSchema)
def by_id(request, identifier: int):
    try:
        todo = Todo.objects.get(id=identifier)
        return {"success": True, "response": todo}
    except Todo.DoesNotExist:
        return {"success": False, "errorMessage": "Todo not found"}
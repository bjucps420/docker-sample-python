from django.core.paginator import Paginator
from django.http import JsonResponse

from todo.models import Todo


def todo_list(request):
    search = request.GET.get('search', '')
    groupBy = request.GET.get('groupBy', '')
    groupByDesc = request.GET.get('groupByDesc', '')
    sortBy = request.GET.get('sortBy', 'title')
    sortDesc = bool(request.GET.get('sortDesc', 'false'))
    page = int(request.GET.get('page', 1))
    mustSort = request.GET.get('mustSort', '')
    multiSort = request.GET.get('multiSort', '')
    itemsPerPage = int(request.GET.get('itemsPerPage', '10'))

    todos = Todo.objects.all()
    if search != "":
        todos = todos.filter(title=search)
    if sortBy != "":
        if sortDesc:
            todos = todos.order_by("-" + sortBy)
        else:
            todos = todos.order_by(sortBy)
    paginator = Paginator(todos.values("title"), itemsPerPage)
    objs = paginator.get_page(page)
    return JsonResponse({
        "total": Todo.objects.count(),
        "items": list(objs)
    })

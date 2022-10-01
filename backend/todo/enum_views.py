from django.views.decorators.cache import never_cache
from ninja import Router
from .api import APIResponseListString


router = Router()


@router.get("status/all", response=APIResponseListString)
def list_status(request):
    return {
        "success": True,
        "response": ['Pending', 'In Progress', 'Complete']
    }


@router.get("type/all", response=APIResponseListString)
def list_type(request):
    return {
        "success": True,
        "response": ['Unclassified', 'Classified', 'Secret', 'Top Secret']
    }

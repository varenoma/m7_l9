from rest_framework.decorators import api_view
from django.db.models import Q
from django.core.paginator import Paginator
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework import status

from .models import ElectronLugatModel
from .serializers import ElectronLugatDetailSerializer, ElectronLugatListSerializer

# Create your views here.

search_param = openapi.Parameter(
    'search', openapi.IN_QUERY, description="So'zlarni qidirish (ru, uz_kiril, uz_lotin, en, tr bo'yicha)", type=openapi.TYPE_STRING
)
sort_by_param = openapi.Parameter(
    'sort_by', openapi.IN_QUERY, description="Sort qilish: ru, uz_kiril, uz_lotin, en, tr", type=openapi.TYPE_STRING
)
sort_order_param = openapi.Parameter(
    'sort_order', openapi.IN_QUERY, description="Tartib: asc (o‘sish), desc (kamayish)", type=openapi.TYPE_STRING
)
page_param = openapi.Parameter(
    'page', openapi.IN_QUERY, description="Sahifa raqami", type=openapi.TYPE_INTEGER
)


@swagger_auto_schema(
    method='get',
    manual_parameters=[search_param, sort_by_param,
                       sort_order_param, page_param],
    responses={200: ElectronLugatListSerializer(many=True)}
)
@api_view(['GET'])
def electron_lugat_view(request):
    lugat = ElectronLugatModel.objects.all()

    qidirish_url = request.GET.get('search', '')
    if qidirish_url:
        lugat = lugat.filter(
            Q(ru__icontains=qidirish_url) |
            Q(uz_kiril__icontains=qidirish_url) |
            Q(uz_lotin__icontains=qidirish_url) |
            Q(en__icontains=qidirish_url) |
            Q(tr__icontains=qidirish_url)
        )

    sort_by = request.GET.get('sort_by', 'uz_lotin')
    sort_order = request.GET.get('sort_order', 'asc')
    if sort_by in ['ru', 'uz_kiril', 'uz_lotin', 'en', 'tr']:
        if sort_order == 'desc':
            lugat = lugat.order_by(f"-{sort_by}")
        else:
            lugat = lugat.order_by(sort_by)

    page = int(request.GET.get('page', 1))
    page_son = 5
    paginator = Paginator(lugat, page_son)
    page_obj = paginator.get_page(page)

    serializer = ElectronLugatListSerializer(page_obj, many=True)
    return Response({
        'results': serializer.data,
        'count': paginator.count,
        'num_pages': paginator.num_pages,
        'current_page': page
    })


@api_view(['GET'])
def electron_lugat_detail(request, pk):
    try:
        lugat = ElectronLugatModel.objects.get(pk=pk)
        ser = ElectronLugatDetailSerializer(lugat)
        return Response(ser.data)
    except lugat.DoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)
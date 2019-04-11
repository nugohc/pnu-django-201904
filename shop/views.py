from django.shortcuts import render
from .models import Item


def item_list(request):
    # DB로부터 모든 Item List를 가져올 예정
    qs  = Item.objects.all()  # QuerySet 타입
    # 템플릿 파일 위치 : shop/templates/shop/item_list.html
    return render(request, 'shop/item_list.html', {
        'item_list': qs,
    })

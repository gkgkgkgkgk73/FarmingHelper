from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Farming
from .utils.exceptions import CustomBadRequestException, InputException
import json
from django.http import JsonResponse
from django.utils import timezone
from django.db.models import Sum

def farming_record(request):
    if request.method == 'GET':
        return render(request, 'farmerapp/farming_input.html')
    elif request.method == 'POST':
        data = json.loads(request.body)
        if 'farming_title' in data:
            new_farming_object = Farming.objects.create(name=data['farming_title'])
            context = {'status':200, 'key': new_farming_object.id}
            return JsonResponse(context)
        else:
            raise InputException('farming_title')   
    raise CustomBadRequestException('')

def farming_record_end(request):
    if request.method == 'POST':
        # FormData로 전송된 데이터를 처리하기 위해 request.POST 사용
        data = request.POST.get('key')
        print(request.POST.get('map_count'))
        if data:
            update_objects = Farming.objects.filter(id=request.POST.get('key')).update(
                name=request.POST.get('farming_title'),
                rotation=request.POST.get('rotation'),
                yellow=request.POST.get('yellow'),
                red=request.POST.get('red'),
                blue=request.POST.get('blue'),
                divine=request.POST.get('divine'),
                map_type=request.POST.get('map_type'),
                map_count=request.POST.get('map_count'),
                cost=request.POST.get('cost'),
                end_time=timezone.now()
            )
            context = {'status':204}
            return JsonResponse(context)
        else:
            raise InputException('farming_key')
    raise CustomBadRequestException('')

def get_farming_score(request):
    if request.method == 'GET':
        farming_name_list = list(Farming.objects.values('name').distinct())
        context={'data':farming_name_list}
        print(context)
        return render(request, 'farmerapp/dash_board.html', context)
    
    elif request.method == 'POST':
        data = json.loads(request.body)
        if 'title' in data:
            farming_list = Farming.objects.filter(name = data['title']).values().order_by('id')
            pre_netperhour = farming_list.aggregate(
                net_total = Sum('net_profit') /  Sum('duration') / 3600
            )['net_total']
            netperhour = pre_netperhour if pre_netperhour is not None else 0
            context = {'status': 200, 'data':{'filtered_data':list(farming_list), 'netperhour':netperhour }}
            print(context)
            return JsonResponse(context)
    
    raise CustomBadRequestException('')
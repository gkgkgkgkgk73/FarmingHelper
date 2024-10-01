from django.urls import path
from .views import farming_record, get_farming_score, farming_record_end

urlpatterns = [
    path('farming-record/', farming_record, name='farming-record'),
    path('farmerapp/', get_farming_score, name='farmerapp'),
    path('farming-record-end/', farming_record_end, name='farming-record-end')
]

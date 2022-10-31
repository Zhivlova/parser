from django.urls import path

from vavt_wheat_exports.views import WheatTablesView, UserWheatDataView

urlpatterns = [
    path('wheat/', WheatTablesView.as_view(), name='example_wheat'),
    path('calculate_wheat_exports/', UserWheatDataView.as_view(), name='get_data_wheat_exports')
]

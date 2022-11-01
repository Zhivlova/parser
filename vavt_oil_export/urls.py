from django.urls import path

from vavt_oil_export.views import OilTablesView, UserOilDataView

urlpatterns = [
    path('oil/', OilTablesView.as_view(), name='oil_example'),
    path('calculate_oil_export/', UserOilDataView.as_view(), name='oil_get_data')

]

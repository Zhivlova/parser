from django.urls import path

from steel_market.views import SteelTablesView, UserSteelDataView

urlpatterns = [
    path('steel/', SteelTablesView.as_view(), name='steel_example'),
    path('calculate_steel_market/', UserSteelDataView.as_view(), name='steel_get_data')

]

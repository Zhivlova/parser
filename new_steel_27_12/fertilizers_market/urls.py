from django.urls import path

from fertilizers_market.views import FertilizersTablesView, UserFertilizersDataView

urlpatterns = [
    path('fertilizers/', FertilizersTablesView.as_view(), name='fertilizers_example'),
    path('calculate_fertilizers_market/', UserFertilizersDataView.as_view(), name='fertilizers_get_data')
]

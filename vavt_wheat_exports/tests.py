from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

class TestSetUp(APITestCase):
    def setUp(self):
        self.example_url = reverse('example')
        self.get_data_url = reverse('get_data')
        self.user_data = {
            "user_data": {
                "PW_A_const_before": 228.0,
                "PW_A_const_after": 228.798691500235,
                "PW_A_shift_before": 0.0,
                "PW_A_shift_after": 0.0,
                "ER_before": 72.32,
                "ER_after": 72.32,
                "CT_before": 59.0,
                "TD_before": 0.0,
                "TD_after": 0.0,
                "Pb_before": 15000.0,
                "Pb_after": 15000.0,
                "Pb2_before": 375.0,
                "Pb2_after": 375.0,
                "Pb3_before": 400.0,
                "Pb3_after": 400.0,
                "t1_before": 0.0,
                "t1_after": 0.7,
                "t2_before": 0.8,
                "t2_after": 0.8,
                "t3_before": 0.9,
                "t3_after": 0.9,
                "demp_before": 0.1,
                "demp_after": 0.1,
                "QSI_A_before": 76.882,
                "i_cost_before": 1.0,
                "i_cost_after": 1.0,
                "shift_QSI_A_before": 0.0,
                "shift_QSI_A_after": 0.0,
                "QDI_С1_before": 14.03,
                "QDI_A_C1_before": 15.129,
                "SpI_C1_before": 1883521.0,
                "QDI_С2_before": 13.297,
                "QDI_A_C2_before": 17.736,
                "SpI_C2_before": 3505628.0,
                "QS_exRUS_A_before": 678.67,
                "QD_A_before": 191.191,
                "QD_exRUS_A_before": 524.002,
                "shift_QSW_A_before": 0.0,
                "shift_QSW_A_after": 0.0,
                "i_cost_world_before": 1.0,
                "i_cost_world_after": 1.0}
        }

        return super().setUp()

class TestWheatExports(TestSetUp):
    def setUp(self):
        super().setUp()


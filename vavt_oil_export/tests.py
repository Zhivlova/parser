from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class TestOilSetUp(APITestCase):
    def setUp(self):
        self.example_url = reverse('example')
        self.get_data_url = reverse('get_data')
        self.user_data = {"user_data": {
            'PW_B1_before': 1500.0,
            'PW_B1_after': 1500.0,
            'PW_B2_before': 300.0,
            'PW_B2_after': 300.0,
            'ER_before': 75.0,
            'ER_after': 75.0,
            'TD_before': 0.0,
            'TD_after': 0.0,
            'Pb_B1_before': 82500.0,
            'Pb_B1_after': 82500.0,
            'tb_B1_before': 0.0,
            'tb_B1_after': 0.7,
            'Pb_B2_before': 13875.0,
            'Pb_B2_after': 13875.0,
            'tb_B2_before': 0.7,
            'tb_B2_after': 0.7,
            'PI_B1': 90000.0,
            'PI_B2': 15000.0,
            'PI_A': 40000.0,
            'QSI_A': 15.0,
            'QSW_RUS_A_before': 0.0,
            'QSW_RUS_A_after': 0.0,
            'i_cost_before': 1.0,
            'i_cost_after': 1.0,
            'shift_QSI_A_before': 0.0,
            'shift_QSI_A_after': 0.0,
            'PI_С': 130000.0,
            'QDI_С': 3.0,
            'QDI_B2': 2.0
        }
        }

        return super().setUp()


class TestOilExport(TestOilSetUp):
    def setUp(self):
        super().setUp()

    def test_get_example_tables_view(self):
        response = self.client.get(self.example_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['prices_on_world_market_of_group_b_products']), 6)
        self.assertEqual(len(response.data['calculation_of_amount_of_export_customs_duty']), 8)

    def test_data_to_front(self):
        response = self.client.post(
            self.get_data_url,
            self.user_data,
            format='json'
        )
        self.assertEqual(response.status_code, 200)
        self.assertTrue(
            {'after': 272453.93831885397,
             'before': 453149.99999999994,
             'increment': -180696.06168114598,
             'increment_pr': -0.3987555151299702,
             'measure': 'долл США*руб/долл США*млн тонн',
             'title': 'Эффект платежного баланса'
             },
            {'after': 56189.208990516214,
             'before': 25146.1875,
             'increment': 31043.021490516214,
             'increment_pr': 1.2345021085409553,
             'measure': 'руб/т*млн тонн',
             'title': 'Эффект таможенных сборов'
             } in response.json().get('prices_on_world_market_of_group_b_products')
        )

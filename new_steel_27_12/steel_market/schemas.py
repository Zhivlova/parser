from drf_yasg import openapi

tables_to_frontend = {
    "200": openapi.Response(
        description="Сервер возвращает список переменных",
        examples={
            "application/json": {
                "table1": [{}],
                "finding_solution": 'true/false',
                "table2": [{}],
                "table3": [{}],
                "table4": [{}]
            }
        }
    ),
}

tables_from_frontend = {
    "200": openapi.Response(
        description="Сервер возвращает список расчитанных значений",
        examples={
            "application/json": {
                "table1": [{}],
                "finding_solution": 'true/false',
                "table2": [{}],
                "table3": [{}],
                "table4": [{}]
            }
        }
    ),
    "400": openapi.Response(
        description="Bad request",
        examples={
            "application/json": {
                "message": "string",
            }
        }
    ),
}

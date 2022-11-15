from drf_yasg import openapi

tables_to_frontend = {
    "200": openapi.Response(
        description="Сервер возвращает список переменных",
        examples={
            "application/json": {
                "table1": [{}],
                "table2": [{}],
                "table3": [{}],
                "table4": [{}],
                "table5": [{}],
                "table6": [{}],
                "table7": [{}],
                "table8": [{}],
                "fintable1": [{}],
                "fintable2": [{}],
                "fintable3": [{}],
                "fintable4": [{}],
                "fintable5": [{}],
                "fintable6": [{}],
                "fintable7": [{}],
                "fintable8": [{}],
                "fintable9": [{}],
                "finding_solution": [{}]
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
                "table2": [{}],
                "table3": [{}],
                "table4": [{}],
                "table5": [{}],
                "table6": [{}],
                "table7": [{}],
                "table8": [{}],
                "fintable1": [{}],
                "fintable2": [{}],
                "fintable3": [{}],
                "fintable4": [{}],
                "fintable5": [{}],
                "fintable6": [{}],
                "fintable7": [{}],
                "fintable8": [{}],
                "fintable9": [{}],
                "finding_solution": [{}]
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

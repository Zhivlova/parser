from drf_yasg import openapi

tables_to_frontend = {
    "200": openapi.Response(
        description="Сервер возвращает список переменных",
        examples={
            "application/json": {
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


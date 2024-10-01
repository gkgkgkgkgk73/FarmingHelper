from rest_framework.exceptions import APIException
from rest_framework import status

class CustomBadRequestException(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = '잘못된 요청입니다.'

class InputException(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = '잘못된 입력값입니다.'
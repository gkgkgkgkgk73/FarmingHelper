from rest_framework.views import exception_handler
from rest_framework.response import Response
from .exceptions import CustomBadRequestException, InputException

def custon_exception_handler(exc, context):
    # 예외 처리기 호출
    response = exception_handler(exc, context)
    
    # 정보 추출
    request = context.get('request')
    
    if response is not None:
        if isinstance(exc, CustomBadRequestException):
            response = {
                'status_code': exc.status_code,
                'message': exc.detail,
            }
        elif isinstance(exc, InputException):
            response = {
                'status_code': exc.default_code,
                'message': exc.detail,
            }
                
    return Response(response, status=response['status'])
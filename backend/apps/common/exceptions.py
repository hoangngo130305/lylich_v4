from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework import status


def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if response is not None:
        error_data = {
            'success': False,
            'error': {
                'status_code': response.status_code,
                'message': _extract_message(response.data),
                'detail': response.data,
            }
        }
        response.data = error_data

    return response


def _extract_message(data):
    if isinstance(data, dict):
        if 'detail' in data:
            return str(data['detail'])
        return '; '.join(
            f"{k}: {v[0] if isinstance(v, list) else v}"
            for k, v in data.items()
        )
    if isinstance(data, list):
        return str(data[0]) if data else 'Lỗi không xác định'
    return str(data)


class BusinessLogicError(Exception):
    def __init__(self, message, code='business_error', status_code=400):
        self.message = message
        self.code = code
        self.status_code = status_code
        super().__init__(message)

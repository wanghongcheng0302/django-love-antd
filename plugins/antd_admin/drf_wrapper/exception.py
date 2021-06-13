from rest_framework.views import exception_handler
from common.response_warp import JsonResponse
from django.core.exceptions import ValidationError
from rest_framework import status
from rest_framework.response import Response
from rest_framework.exceptions import Throttled, AuthenticationFailed
import logging
import traceback
from globals.log import logger
from common.response_warp import RC
from utils.data_wrap import drferror_to_element


def common_exception_handler(exc, context):
    response = exception_handler(exc, context)
    raise exc
    logger.error(traceback.format_exc())
    if isinstance(exc, Throttled):
        return JsonResponse(status=exc.status_code, err='请求频繁', rc=RC.INVALID)

    if isinstance(response, Response):
        err = drferror_to_element(response.data)
        return JsonResponse(status=response.status_code, err=err, rc=RC.INVALID)

    if isinstance(exc, ValidationError):
        # 异常标准化输出
        err = drferror_to_element(exc.message)
        return JsonResponse(status=status.HTTP_400_BAD_REQUEST, err=err, rc=RC.INVALID)

    if isinstance(exc, AuthenticationFailed):
        err = drferror_to_element(str(exc))
        return JsonResponse(status=status.HTTP_400_BAD_REQUEST, err=err, rc=RC.INVALID)

    if isinstance(exc, Exception):
        return JsonResponse(status=status.HTTP_500_INTERNAL_SERVER_ERROR, err=str(exc), rc=RC.ERROR)

    return response

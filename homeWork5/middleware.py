from django.urls import resolve
from django.utils.deprecation import MiddlewareMixin
import datetime
import logging
logging.basicConfig(level=logging.INFO, filename='logs.log')


class LogMiddleware(MiddlewareMixin):

    def process_request(self, request):
        resolved_path_info = resolve(request.path_info)
        logging.info(
            'Request %s View name %s route %s',
            request, resolved_path_info.view_name, resolved_path_info.route)

    def process_response(self, request, response):
        logging.info('For request %s response %s', request, response)
        return response


class RawDataMiddleware(MiddlewareMixin):

    def process_request(self, request):
        current_hash = hash(datetime.datetime.now())
        request.META['current_hash'] = current_hash


class IdentifyResponseMiddleware(MiddlewareMixin):

    def process_response(self, request, response):
        response['current_hash'] = request.META['current_hash']
        return response

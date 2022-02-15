"""
    Quantum Network Explorer

    Server for the QNE project  # noqa: E501

    The version of the OpenAPI document: 0.0.8
    Contact: apiteam@swagger.io
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from openapi_client.api_client import ApiClient, Endpoint as _Endpoint
from openapi_client.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from openapi_client.model.result import Result


class ResultsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        def __create_result(
            self,
            body,
            **kwargs
        ):
            """Add a Result to the RoundSet for the authenticated Backend  # noqa: E501

            Typically only used by quantum network backends. When a Backend has executed a single RoundSet for an Experiment it sends the Result to api-router to register this Result to the RoundSet that is currently running for the Experiment.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.create_result(body, async_req=True)
            >>> result = thread.get()

            Args:
                body (Result): Result that needs to be added.

            Keyword Args:
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                Result
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['body'] = \
                body
            return self.call_with_http_info(**kwargs)

        self.create_result = _Endpoint(
            settings={
                'response_type': (Result,),
                'auth': [
                    'api_key'
                ],
                'endpoint_path': '/results/',
                'operation_id': 'create_result',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'body',
                ],
                'required': [
                    'body',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'body':
                        (Result,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'body': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client,
            callable=__create_result
        )

        def __results_experiment(
            self,
            exp_id,
            **kwargs
        ):
            """List Results for Experiment uniquely identified by <id>  # noqa: E501

            For the authenticated Backend, returns all the Results for all the RoundSets for the specific Experiment. The Results are linked to one or more RoundSets that have been executed for the Experiment. When a Backend starts executing a new RoundSet for an Experiment it needs all the previous Results of the Experiment to calculate new cumulative Results. For the authenticated user, returns only the Results for RoundSets for Experiment with <id> that have status COMPLETE or FAILED. The Results are sorted on round-set-id (low to high) and for each RoundSet on the Results round number.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.results_experiment(exp_id, async_req=True)
            >>> result = thread.get()

            Args:
                exp_id (int): ID of Experiment

            Keyword Args:
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                [Result]
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['exp_id'] = \
                exp_id
            return self.call_with_http_info(**kwargs)

        self.results_experiment = _Endpoint(
            settings={
                'response_type': ([Result],),
                'auth': [
                    'api_key'
                ],
                'endpoint_path': '/experiments/{exp-id}/results/',
                'operation_id': 'results_experiment',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'exp_id',
                ],
                'required': [
                    'exp_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'exp_id':
                        (int,),
                },
                'attribute_map': {
                    'exp_id': 'exp-id',
                },
                'location_map': {
                    'exp_id': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__results_experiment
        )

        def __results_round_set(
            self,
            round_set_id,
            **kwargs
        ):
            """For the authenticated user, list Results for the RoundSet uniquely identified by <id>  # noqa: E501

            Get all Results that are linked to the specific RoundSet. Only RoundSets that have been picked up by an executing Backend, have Results. The Results are sorted on round number (low to high).  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.results_round_set(round_set_id, async_req=True)
            >>> result = thread.get()

            Args:
                round_set_id (int): ID of RoundSet

            Keyword Args:
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                [Result]
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['round_set_id'] = \
                round_set_id
            return self.call_with_http_info(**kwargs)

        self.results_round_set = _Endpoint(
            settings={
                'response_type': ([Result],),
                'auth': [
                    'api_key'
                ],
                'endpoint_path': '/round-sets/{round-set-id}/results/',
                'operation_id': 'results_round_set',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'round_set_id',
                ],
                'required': [
                    'round_set_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'round_set_id':
                        (int,),
                },
                'attribute_map': {
                    'round_set_id': 'round-set-id',
                },
                'location_map': {
                    'round_set_id': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__results_round_set
        )

        def __retrieve_result(
            self,
            result_id,
            **kwargs
        ):
            """For the authenticated user, get Result uniquely identified by <id>  # noqa: E501

            Get the specific Result. The Result is linked to a RoundSet of an Experiment owned by the user.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.retrieve_result(result_id, async_req=True)
            >>> result = thread.get()

            Args:
                result_id (int): ID of Result

            Keyword Args:
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                Result
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['result_id'] = \
                result_id
            return self.call_with_http_info(**kwargs)

        self.retrieve_result = _Endpoint(
            settings={
                'response_type': (Result,),
                'auth': [
                    'api_key'
                ],
                'endpoint_path': '/results/{result-id}/',
                'operation_id': 'retrieve_result',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'result_id',
                ],
                'required': [
                    'result_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'result_id':
                        (int,),
                },
                'attribute_map': {
                    'result_id': 'result-id',
                },
                'location_map': {
                    'result_id': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__retrieve_result
        )

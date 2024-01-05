# coding: utf-8
import pprint
import re  # noqa: F401

import six
from enum import Enum
from schema.aws.s3.objectcreated.Bucket import Bucket  # noqa: F401,E501
from schema.aws.s3.objectcreated.Object import Object  # noqa: F401,E501

class ObjectCreated(object):


    _types = {
        'bucket': 'Bucket',
        'object': 'Object',
        'reason': 'str',
        'request_id': 'str',
        'requester': 'str',
        'source_ip_address': 'str',
        'version': 'str'
    }

    _attribute_map = {
        'bucket': 'bucket',
        'object': 'object',
        'reason': 'reason',
        'request_id': 'request-id',
        'requester': 'requester',
        'source_ip_address': 'source-ip-address',
        'version': 'version'
    }

    def __init__(self, bucket=None, object=None, reason=None, request_id=None, requester=None, source_ip_address=None, version=None):  # noqa: E501
        self._bucket = None
        self._object = None
        self._reason = None
        self._request_id = None
        self._requester = None
        self._source_ip_address = None
        self._version = None
        self.discriminator = None
        self.bucket = bucket
        self.object = object
        self.reason = reason
        self.request_id = request_id
        self.requester = requester
        self.source_ip_address = source_ip_address
        self.version = version


    @property
    def bucket(self):

        return self._bucket

    @bucket.setter
    def bucket(self, bucket):


        self._bucket = bucket


    @property
    def object(self):

        return self._object

    @object.setter
    def object(self, object):


        self._object = object


    @property
    def reason(self):

        return self._reason

    @reason.setter
    def reason(self, reason):


        self._reason = reason


    @property
    def request_id(self):

        return self._request_id

    @request_id.setter
    def request_id(self, request_id):


        self._request_id = request_id


    @property
    def requester(self):

        return self._requester

    @requester.setter
    def requester(self, requester):


        self._requester = requester


    @property
    def source_ip_address(self):

        return self._source_ip_address

    @source_ip_address.setter
    def source_ip_address(self, source_ip_address):


        self._source_ip_address = source_ip_address


    @property
    def version(self):

        return self._version

    @version.setter
    def version(self, version):


        self._version = version

    def to_dict(self):
        result = {}

        for attr, _ in six.iteritems(self._types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(ObjectCreated, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, ObjectCreated):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other


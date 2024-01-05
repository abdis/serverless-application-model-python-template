# coding: utf-8
import pprint
import re  # noqa: F401

import six
from enum import Enum

class Object(object):


    _types = {
        'etag': 'str',
        'key': 'str',
        'sequencer': 'str',
        'size': 'float',
        'version_id': 'str'
    }

    _attribute_map = {
        'etag': 'etag',
        'key': 'key',
        'sequencer': 'sequencer',
        'size': 'size',
        'version_id': 'version-id'
    }

    def __init__(self, etag=None, key=None, sequencer=None, size=None, version_id=None):  # noqa: E501
        self._etag = None
        self._key = None
        self._sequencer = None
        self._size = None
        self._version_id = None
        self.discriminator = None
        self.etag = etag
        self.key = key
        self.sequencer = sequencer
        self.size = size
        self.version_id = version_id


    @property
    def etag(self):

        return self._etag

    @etag.setter
    def etag(self, etag):


        self._etag = etag


    @property
    def key(self):

        return self._key

    @key.setter
    def key(self, key):


        self._key = key


    @property
    def sequencer(self):

        return self._sequencer

    @sequencer.setter
    def sequencer(self, sequencer):


        self._sequencer = sequencer


    @property
    def size(self):

        return self._size

    @size.setter
    def size(self, size):


        self._size = size


    @property
    def version_id(self):

        return self._version_id

    @version_id.setter
    def version_id(self, version_id):


        self._version_id = version_id

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
        if issubclass(Object, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, Object):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other


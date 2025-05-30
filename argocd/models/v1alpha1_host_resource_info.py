# coding: utf-8

"""
    Consolidate Services

    Description of all APIs  # noqa: E501

    OpenAPI spec version: version not set
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from argocd.configuration import Configuration


class V1alpha1HostResourceInfo(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'capacity': 'int',
        'requested_by_app': 'int',
        'requested_by_neighbors': 'int',
        'resource_name': 'str'
    }

    attribute_map = {
        'capacity': 'capacity',
        'requested_by_app': 'requestedByApp',
        'requested_by_neighbors': 'requestedByNeighbors',
        'resource_name': 'resourceName'
    }

    def __init__(self, capacity=None, requested_by_app=None, requested_by_neighbors=None, resource_name=None, _configuration=None):  # noqa: E501
        """V1alpha1HostResourceInfo - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._capacity = None
        self._requested_by_app = None
        self._requested_by_neighbors = None
        self._resource_name = None
        self.discriminator = None

        if capacity is not None:
            self.capacity = capacity
        if requested_by_app is not None:
            self.requested_by_app = requested_by_app
        if requested_by_neighbors is not None:
            self.requested_by_neighbors = requested_by_neighbors
        if resource_name is not None:
            self.resource_name = resource_name

    @property
    def capacity(self):
        """Gets the capacity of this V1alpha1HostResourceInfo.  # noqa: E501


        :return: The capacity of this V1alpha1HostResourceInfo.  # noqa: E501
        :rtype: int
        """
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        """Sets the capacity of this V1alpha1HostResourceInfo.


        :param capacity: The capacity of this V1alpha1HostResourceInfo.  # noqa: E501
        :type: int
        """

        self._capacity = capacity

    @property
    def requested_by_app(self):
        """Gets the requested_by_app of this V1alpha1HostResourceInfo.  # noqa: E501


        :return: The requested_by_app of this V1alpha1HostResourceInfo.  # noqa: E501
        :rtype: int
        """
        return self._requested_by_app

    @requested_by_app.setter
    def requested_by_app(self, requested_by_app):
        """Sets the requested_by_app of this V1alpha1HostResourceInfo.


        :param requested_by_app: The requested_by_app of this V1alpha1HostResourceInfo.  # noqa: E501
        :type: int
        """

        self._requested_by_app = requested_by_app

    @property
    def requested_by_neighbors(self):
        """Gets the requested_by_neighbors of this V1alpha1HostResourceInfo.  # noqa: E501


        :return: The requested_by_neighbors of this V1alpha1HostResourceInfo.  # noqa: E501
        :rtype: int
        """
        return self._requested_by_neighbors

    @requested_by_neighbors.setter
    def requested_by_neighbors(self, requested_by_neighbors):
        """Sets the requested_by_neighbors of this V1alpha1HostResourceInfo.


        :param requested_by_neighbors: The requested_by_neighbors of this V1alpha1HostResourceInfo.  # noqa: E501
        :type: int
        """

        self._requested_by_neighbors = requested_by_neighbors

    @property
    def resource_name(self):
        """Gets the resource_name of this V1alpha1HostResourceInfo.  # noqa: E501


        :return: The resource_name of this V1alpha1HostResourceInfo.  # noqa: E501
        :rtype: str
        """
        return self._resource_name

    @resource_name.setter
    def resource_name(self, resource_name):
        """Sets the resource_name of this V1alpha1HostResourceInfo.


        :param resource_name: The resource_name of this V1alpha1HostResourceInfo.  # noqa: E501
        :type: str
        """

        self._resource_name = resource_name

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(V1alpha1HostResourceInfo, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, V1alpha1HostResourceInfo):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1alpha1HostResourceInfo):
            return True

        return self.to_dict() != other.to_dict()

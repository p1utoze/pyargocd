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


class ClusterSettingsPluginsResponse(object):
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
        'plugins': 'list[ClusterPlugin]'
    }

    attribute_map = {
        'plugins': 'plugins'
    }

    def __init__(self, plugins=None, _configuration=None):  # noqa: E501
        """ClusterSettingsPluginsResponse - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._plugins = None
        self.discriminator = None

        if plugins is not None:
            self.plugins = plugins

    @property
    def plugins(self):
        """Gets the plugins of this ClusterSettingsPluginsResponse.  # noqa: E501


        :return: The plugins of this ClusterSettingsPluginsResponse.  # noqa: E501
        :rtype: list[ClusterPlugin]
        """
        return self._plugins

    @plugins.setter
    def plugins(self, plugins):
        """Sets the plugins of this ClusterSettingsPluginsResponse.


        :param plugins: The plugins of this ClusterSettingsPluginsResponse.  # noqa: E501
        :type: list[ClusterPlugin]
        """

        self._plugins = plugins

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
        if issubclass(ClusterSettingsPluginsResponse, dict):
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
        if not isinstance(other, ClusterSettingsPluginsResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ClusterSettingsPluginsResponse):
            return True

        return self.to_dict() != other.to_dict()

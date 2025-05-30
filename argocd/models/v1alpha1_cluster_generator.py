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


class V1alpha1ClusterGenerator(object):
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
        'flat_list': 'bool',
        'selector': 'V1LabelSelector',
        'template': 'V1alpha1ApplicationSetTemplate',
        'values': 'dict(str, str)'
    }

    attribute_map = {
        'flat_list': 'flatList',
        'selector': 'selector',
        'template': 'template',
        'values': 'values'
    }

    def __init__(self, flat_list=None, selector=None, template=None, values=None, _configuration=None):  # noqa: E501
        """V1alpha1ClusterGenerator - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._flat_list = None
        self._selector = None
        self._template = None
        self._values = None
        self.discriminator = None

        if flat_list is not None:
            self.flat_list = flat_list
        if selector is not None:
            self.selector = selector
        if template is not None:
            self.template = template
        if values is not None:
            self.values = values

    @property
    def flat_list(self):
        """Gets the flat_list of this V1alpha1ClusterGenerator.  # noqa: E501


        :return: The flat_list of this V1alpha1ClusterGenerator.  # noqa: E501
        :rtype: bool
        """
        return self._flat_list

    @flat_list.setter
    def flat_list(self, flat_list):
        """Sets the flat_list of this V1alpha1ClusterGenerator.


        :param flat_list: The flat_list of this V1alpha1ClusterGenerator.  # noqa: E501
        :type: bool
        """

        self._flat_list = flat_list

    @property
    def selector(self):
        """Gets the selector of this V1alpha1ClusterGenerator.  # noqa: E501


        :return: The selector of this V1alpha1ClusterGenerator.  # noqa: E501
        :rtype: V1LabelSelector
        """
        return self._selector

    @selector.setter
    def selector(self, selector):
        """Sets the selector of this V1alpha1ClusterGenerator.


        :param selector: The selector of this V1alpha1ClusterGenerator.  # noqa: E501
        :type: V1LabelSelector
        """

        self._selector = selector

    @property
    def template(self):
        """Gets the template of this V1alpha1ClusterGenerator.  # noqa: E501


        :return: The template of this V1alpha1ClusterGenerator.  # noqa: E501
        :rtype: V1alpha1ApplicationSetTemplate
        """
        return self._template

    @template.setter
    def template(self, template):
        """Sets the template of this V1alpha1ClusterGenerator.


        :param template: The template of this V1alpha1ClusterGenerator.  # noqa: E501
        :type: V1alpha1ApplicationSetTemplate
        """

        self._template = template

    @property
    def values(self):
        """Gets the values of this V1alpha1ClusterGenerator.  # noqa: E501


        :return: The values of this V1alpha1ClusterGenerator.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._values

    @values.setter
    def values(self, values):
        """Sets the values of this V1alpha1ClusterGenerator.


        :param values: The values of this V1alpha1ClusterGenerator.  # noqa: E501
        :type: dict(str, str)
        """

        self._values = values

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
        if issubclass(V1alpha1ClusterGenerator, dict):
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
        if not isinstance(other, V1alpha1ClusterGenerator):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1alpha1ClusterGenerator):
            return True

        return self.to_dict() != other.to_dict()

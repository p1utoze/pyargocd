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


class V1alpha1DuckTypeGenerator(object):
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
        'config_map_ref': 'str',
        'label_selector': 'V1LabelSelector',
        'name': 'str',
        'requeue_after_seconds': 'int',
        'template': 'V1alpha1ApplicationSetTemplate',
        'values': 'dict(str, str)'
    }

    attribute_map = {
        'config_map_ref': 'configMapRef',
        'label_selector': 'labelSelector',
        'name': 'name',
        'requeue_after_seconds': 'requeueAfterSeconds',
        'template': 'template',
        'values': 'values'
    }

    def __init__(self, config_map_ref=None, label_selector=None, name=None, requeue_after_seconds=None, template=None, values=None, _configuration=None):  # noqa: E501
        """V1alpha1DuckTypeGenerator - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._config_map_ref = None
        self._label_selector = None
        self._name = None
        self._requeue_after_seconds = None
        self._template = None
        self._values = None
        self.discriminator = None

        if config_map_ref is not None:
            self.config_map_ref = config_map_ref
        if label_selector is not None:
            self.label_selector = label_selector
        if name is not None:
            self.name = name
        if requeue_after_seconds is not None:
            self.requeue_after_seconds = requeue_after_seconds
        if template is not None:
            self.template = template
        if values is not None:
            self.values = values

    @property
    def config_map_ref(self):
        """Gets the config_map_ref of this V1alpha1DuckTypeGenerator.  # noqa: E501


        :return: The config_map_ref of this V1alpha1DuckTypeGenerator.  # noqa: E501
        :rtype: str
        """
        return self._config_map_ref

    @config_map_ref.setter
    def config_map_ref(self, config_map_ref):
        """Sets the config_map_ref of this V1alpha1DuckTypeGenerator.


        :param config_map_ref: The config_map_ref of this V1alpha1DuckTypeGenerator.  # noqa: E501
        :type: str
        """

        self._config_map_ref = config_map_ref

    @property
    def label_selector(self):
        """Gets the label_selector of this V1alpha1DuckTypeGenerator.  # noqa: E501


        :return: The label_selector of this V1alpha1DuckTypeGenerator.  # noqa: E501
        :rtype: V1LabelSelector
        """
        return self._label_selector

    @label_selector.setter
    def label_selector(self, label_selector):
        """Sets the label_selector of this V1alpha1DuckTypeGenerator.


        :param label_selector: The label_selector of this V1alpha1DuckTypeGenerator.  # noqa: E501
        :type: V1LabelSelector
        """

        self._label_selector = label_selector

    @property
    def name(self):
        """Gets the name of this V1alpha1DuckTypeGenerator.  # noqa: E501


        :return: The name of this V1alpha1DuckTypeGenerator.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this V1alpha1DuckTypeGenerator.


        :param name: The name of this V1alpha1DuckTypeGenerator.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def requeue_after_seconds(self):
        """Gets the requeue_after_seconds of this V1alpha1DuckTypeGenerator.  # noqa: E501


        :return: The requeue_after_seconds of this V1alpha1DuckTypeGenerator.  # noqa: E501
        :rtype: int
        """
        return self._requeue_after_seconds

    @requeue_after_seconds.setter
    def requeue_after_seconds(self, requeue_after_seconds):
        """Sets the requeue_after_seconds of this V1alpha1DuckTypeGenerator.


        :param requeue_after_seconds: The requeue_after_seconds of this V1alpha1DuckTypeGenerator.  # noqa: E501
        :type: int
        """

        self._requeue_after_seconds = requeue_after_seconds

    @property
    def template(self):
        """Gets the template of this V1alpha1DuckTypeGenerator.  # noqa: E501


        :return: The template of this V1alpha1DuckTypeGenerator.  # noqa: E501
        :rtype: V1alpha1ApplicationSetTemplate
        """
        return self._template

    @template.setter
    def template(self, template):
        """Sets the template of this V1alpha1DuckTypeGenerator.


        :param template: The template of this V1alpha1DuckTypeGenerator.  # noqa: E501
        :type: V1alpha1ApplicationSetTemplate
        """

        self._template = template

    @property
    def values(self):
        """Gets the values of this V1alpha1DuckTypeGenerator.  # noqa: E501


        :return: The values of this V1alpha1DuckTypeGenerator.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._values

    @values.setter
    def values(self, values):
        """Sets the values of this V1alpha1DuckTypeGenerator.


        :param values: The values of this V1alpha1DuckTypeGenerator.  # noqa: E501
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
        if issubclass(V1alpha1DuckTypeGenerator, dict):
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
        if not isinstance(other, V1alpha1DuckTypeGenerator):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1alpha1DuckTypeGenerator):
            return True

        return self.to_dict() != other.to_dict()

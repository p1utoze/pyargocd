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


class V1alpha1TLSClientConfig(object):
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
        'ca_data': 'str',
        'cert_data': 'str',
        'insecure': 'bool',
        'key_data': 'str',
        'server_name': 'str'
    }

    attribute_map = {
        'ca_data': 'caData',
        'cert_data': 'certData',
        'insecure': 'insecure',
        'key_data': 'keyData',
        'server_name': 'serverName'
    }

    def __init__(self, ca_data=None, cert_data=None, insecure=None, key_data=None, server_name=None, _configuration=None):  # noqa: E501
        """V1alpha1TLSClientConfig - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._ca_data = None
        self._cert_data = None
        self._insecure = None
        self._key_data = None
        self._server_name = None
        self.discriminator = None

        if ca_data is not None:
            self.ca_data = ca_data
        if cert_data is not None:
            self.cert_data = cert_data
        if insecure is not None:
            self.insecure = insecure
        if key_data is not None:
            self.key_data = key_data
        if server_name is not None:
            self.server_name = server_name

    @property
    def ca_data(self):
        """Gets the ca_data of this V1alpha1TLSClientConfig.  # noqa: E501


        :return: The ca_data of this V1alpha1TLSClientConfig.  # noqa: E501
        :rtype: str
        """
        return self._ca_data

    @ca_data.setter
    def ca_data(self, ca_data):
        """Sets the ca_data of this V1alpha1TLSClientConfig.


        :param ca_data: The ca_data of this V1alpha1TLSClientConfig.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                ca_data is not None and not re.search(r'^(?:[A-Za-z0-9+\/]{4})*(?:[A-Za-z0-9+\/]{2}==|[A-Za-z0-9+\/]{3}=)?$', ca_data)):  # noqa: E501
            raise ValueError(r"Invalid value for `ca_data`, must be a follow pattern or equal to `/^(?:[A-Za-z0-9+\/]{4})*(?:[A-Za-z0-9+\/]{2}==|[A-Za-z0-9+\/]{3}=)?$/`")  # noqa: E501

        self._ca_data = ca_data

    @property
    def cert_data(self):
        """Gets the cert_data of this V1alpha1TLSClientConfig.  # noqa: E501


        :return: The cert_data of this V1alpha1TLSClientConfig.  # noqa: E501
        :rtype: str
        """
        return self._cert_data

    @cert_data.setter
    def cert_data(self, cert_data):
        """Sets the cert_data of this V1alpha1TLSClientConfig.


        :param cert_data: The cert_data of this V1alpha1TLSClientConfig.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                cert_data is not None and not re.search(r'^(?:[A-Za-z0-9+\/]{4})*(?:[A-Za-z0-9+\/]{2}==|[A-Za-z0-9+\/]{3}=)?$', cert_data)):  # noqa: E501
            raise ValueError(r"Invalid value for `cert_data`, must be a follow pattern or equal to `/^(?:[A-Za-z0-9+\/]{4})*(?:[A-Za-z0-9+\/]{2}==|[A-Za-z0-9+\/]{3}=)?$/`")  # noqa: E501

        self._cert_data = cert_data

    @property
    def insecure(self):
        """Gets the insecure of this V1alpha1TLSClientConfig.  # noqa: E501

        Insecure specifies that the server should be accessed without verifying the TLS certificate. For testing only.  # noqa: E501

        :return: The insecure of this V1alpha1TLSClientConfig.  # noqa: E501
        :rtype: bool
        """
        return self._insecure

    @insecure.setter
    def insecure(self, insecure):
        """Sets the insecure of this V1alpha1TLSClientConfig.

        Insecure specifies that the server should be accessed without verifying the TLS certificate. For testing only.  # noqa: E501

        :param insecure: The insecure of this V1alpha1TLSClientConfig.  # noqa: E501
        :type: bool
        """

        self._insecure = insecure

    @property
    def key_data(self):
        """Gets the key_data of this V1alpha1TLSClientConfig.  # noqa: E501


        :return: The key_data of this V1alpha1TLSClientConfig.  # noqa: E501
        :rtype: str
        """
        return self._key_data

    @key_data.setter
    def key_data(self, key_data):
        """Sets the key_data of this V1alpha1TLSClientConfig.


        :param key_data: The key_data of this V1alpha1TLSClientConfig.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                key_data is not None and not re.search(r'^(?:[A-Za-z0-9+\/]{4})*(?:[A-Za-z0-9+\/]{2}==|[A-Za-z0-9+\/]{3}=)?$', key_data)):  # noqa: E501
            raise ValueError(r"Invalid value for `key_data`, must be a follow pattern or equal to `/^(?:[A-Za-z0-9+\/]{4})*(?:[A-Za-z0-9+\/]{2}==|[A-Za-z0-9+\/]{3}=)?$/`")  # noqa: E501

        self._key_data = key_data

    @property
    def server_name(self):
        """Gets the server_name of this V1alpha1TLSClientConfig.  # noqa: E501

        ServerName is passed to the server for SNI and is used in the client to check server certificates against. If ServerName is empty, the hostname used to contact the server is used.  # noqa: E501

        :return: The server_name of this V1alpha1TLSClientConfig.  # noqa: E501
        :rtype: str
        """
        return self._server_name

    @server_name.setter
    def server_name(self, server_name):
        """Sets the server_name of this V1alpha1TLSClientConfig.

        ServerName is passed to the server for SNI and is used in the client to check server certificates against. If ServerName is empty, the hostname used to contact the server is used.  # noqa: E501

        :param server_name: The server_name of this V1alpha1TLSClientConfig.  # noqa: E501
        :type: str
        """

        self._server_name = server_name

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
        if issubclass(V1alpha1TLSClientConfig, dict):
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
        if not isinstance(other, V1alpha1TLSClientConfig):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1alpha1TLSClientConfig):
            return True

        return self.to_dict() != other.to_dict()

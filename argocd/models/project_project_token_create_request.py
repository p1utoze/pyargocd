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


class ProjectProjectTokenCreateRequest(object):
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
        'description': 'str',
        'expires_in': 'int',
        'id': 'str',
        'project': 'str',
        'role': 'str'
    }

    attribute_map = {
        'description': 'description',
        'expires_in': 'expiresIn',
        'id': 'id',
        'project': 'project',
        'role': 'role'
    }

    def __init__(self, description=None, expires_in=None, id=None, project=None, role=None, _configuration=None):  # noqa: E501
        """ProjectProjectTokenCreateRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._description = None
        self._expires_in = None
        self._id = None
        self._project = None
        self._role = None
        self.discriminator = None

        if description is not None:
            self.description = description
        if expires_in is not None:
            self.expires_in = expires_in
        if id is not None:
            self.id = id
        if project is not None:
            self.project = project
        if role is not None:
            self.role = role

    @property
    def description(self):
        """Gets the description of this ProjectProjectTokenCreateRequest.  # noqa: E501


        :return: The description of this ProjectProjectTokenCreateRequest.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ProjectProjectTokenCreateRequest.


        :param description: The description of this ProjectProjectTokenCreateRequest.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def expires_in(self):
        """Gets the expires_in of this ProjectProjectTokenCreateRequest.  # noqa: E501


        :return: The expires_in of this ProjectProjectTokenCreateRequest.  # noqa: E501
        :rtype: int
        """
        return self._expires_in

    @expires_in.setter
    def expires_in(self, expires_in):
        """Sets the expires_in of this ProjectProjectTokenCreateRequest.


        :param expires_in: The expires_in of this ProjectProjectTokenCreateRequest.  # noqa: E501
        :type: int
        """

        self._expires_in = expires_in

    @property
    def id(self):
        """Gets the id of this ProjectProjectTokenCreateRequest.  # noqa: E501


        :return: The id of this ProjectProjectTokenCreateRequest.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ProjectProjectTokenCreateRequest.


        :param id: The id of this ProjectProjectTokenCreateRequest.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def project(self):
        """Gets the project of this ProjectProjectTokenCreateRequest.  # noqa: E501


        :return: The project of this ProjectProjectTokenCreateRequest.  # noqa: E501
        :rtype: str
        """
        return self._project

    @project.setter
    def project(self, project):
        """Sets the project of this ProjectProjectTokenCreateRequest.


        :param project: The project of this ProjectProjectTokenCreateRequest.  # noqa: E501
        :type: str
        """

        self._project = project

    @property
    def role(self):
        """Gets the role of this ProjectProjectTokenCreateRequest.  # noqa: E501


        :return: The role of this ProjectProjectTokenCreateRequest.  # noqa: E501
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        """Sets the role of this ProjectProjectTokenCreateRequest.


        :param role: The role of this ProjectProjectTokenCreateRequest.  # noqa: E501
        :type: str
        """

        self._role = role

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
        if issubclass(ProjectProjectTokenCreateRequest, dict):
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
        if not isinstance(other, ProjectProjectTokenCreateRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ProjectProjectTokenCreateRequest):
            return True

        return self.to_dict() != other.to_dict()

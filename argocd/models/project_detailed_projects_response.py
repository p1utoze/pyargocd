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


class ProjectDetailedProjectsResponse(object):
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
        'clusters': 'list[V1alpha1Cluster]',
        'global_projects': 'list[V1alpha1AppProject]',
        'project': 'V1alpha1AppProject',
        'repositories': 'list[V1alpha1Repository]'
    }

    attribute_map = {
        'clusters': 'clusters',
        'global_projects': 'globalProjects',
        'project': 'project',
        'repositories': 'repositories'
    }

    def __init__(self, clusters=None, global_projects=None, project=None, repositories=None, _configuration=None):  # noqa: E501
        """ProjectDetailedProjectsResponse - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._clusters = None
        self._global_projects = None
        self._project = None
        self._repositories = None
        self.discriminator = None

        if clusters is not None:
            self.clusters = clusters
        if global_projects is not None:
            self.global_projects = global_projects
        if project is not None:
            self.project = project
        if repositories is not None:
            self.repositories = repositories

    @property
    def clusters(self):
        """Gets the clusters of this ProjectDetailedProjectsResponse.  # noqa: E501


        :return: The clusters of this ProjectDetailedProjectsResponse.  # noqa: E501
        :rtype: list[V1alpha1Cluster]
        """
        return self._clusters

    @clusters.setter
    def clusters(self, clusters):
        """Sets the clusters of this ProjectDetailedProjectsResponse.


        :param clusters: The clusters of this ProjectDetailedProjectsResponse.  # noqa: E501
        :type: list[V1alpha1Cluster]
        """

        self._clusters = clusters

    @property
    def global_projects(self):
        """Gets the global_projects of this ProjectDetailedProjectsResponse.  # noqa: E501


        :return: The global_projects of this ProjectDetailedProjectsResponse.  # noqa: E501
        :rtype: list[V1alpha1AppProject]
        """
        return self._global_projects

    @global_projects.setter
    def global_projects(self, global_projects):
        """Sets the global_projects of this ProjectDetailedProjectsResponse.


        :param global_projects: The global_projects of this ProjectDetailedProjectsResponse.  # noqa: E501
        :type: list[V1alpha1AppProject]
        """

        self._global_projects = global_projects

    @property
    def project(self):
        """Gets the project of this ProjectDetailedProjectsResponse.  # noqa: E501


        :return: The project of this ProjectDetailedProjectsResponse.  # noqa: E501
        :rtype: V1alpha1AppProject
        """
        return self._project

    @project.setter
    def project(self, project):
        """Sets the project of this ProjectDetailedProjectsResponse.


        :param project: The project of this ProjectDetailedProjectsResponse.  # noqa: E501
        :type: V1alpha1AppProject
        """

        self._project = project

    @property
    def repositories(self):
        """Gets the repositories of this ProjectDetailedProjectsResponse.  # noqa: E501


        :return: The repositories of this ProjectDetailedProjectsResponse.  # noqa: E501
        :rtype: list[V1alpha1Repository]
        """
        return self._repositories

    @repositories.setter
    def repositories(self, repositories):
        """Sets the repositories of this ProjectDetailedProjectsResponse.


        :param repositories: The repositories of this ProjectDetailedProjectsResponse.  # noqa: E501
        :type: list[V1alpha1Repository]
        """

        self._repositories = repositories

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
        if issubclass(ProjectDetailedProjectsResponse, dict):
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
        if not isinstance(other, ProjectDetailedProjectsResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ProjectDetailedProjectsResponse):
            return True

        return self.to_dict() != other.to_dict()

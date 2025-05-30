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


class V1alpha1PullRequestGenerator(object):
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
        'azuredevops': 'V1alpha1PullRequestGeneratorAzureDevOps',
        'bitbucket': 'V1alpha1PullRequestGeneratorBitbucket',
        'bitbucket_server': 'V1alpha1PullRequestGeneratorBitbucketServer',
        'filters': 'list[V1alpha1PullRequestGeneratorFilter]',
        'gitea': 'V1alpha1PullRequestGeneratorGitea',
        'github': 'V1alpha1PullRequestGeneratorGithub',
        'gitlab': 'V1alpha1PullRequestGeneratorGitLab',
        'requeue_after_seconds': 'int',
        'template': 'V1alpha1ApplicationSetTemplate'
    }

    attribute_map = {
        'azuredevops': 'azuredevops',
        'bitbucket': 'bitbucket',
        'bitbucket_server': 'bitbucketServer',
        'filters': 'filters',
        'gitea': 'gitea',
        'github': 'github',
        'gitlab': 'gitlab',
        'requeue_after_seconds': 'requeueAfterSeconds',
        'template': 'template'
    }

    def __init__(self, azuredevops=None, bitbucket=None, bitbucket_server=None, filters=None, gitea=None, github=None, gitlab=None, requeue_after_seconds=None, template=None, _configuration=None):  # noqa: E501
        """V1alpha1PullRequestGenerator - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._azuredevops = None
        self._bitbucket = None
        self._bitbucket_server = None
        self._filters = None
        self._gitea = None
        self._github = None
        self._gitlab = None
        self._requeue_after_seconds = None
        self._template = None
        self.discriminator = None

        if azuredevops is not None:
            self.azuredevops = azuredevops
        if bitbucket is not None:
            self.bitbucket = bitbucket
        if bitbucket_server is not None:
            self.bitbucket_server = bitbucket_server
        if filters is not None:
            self.filters = filters
        if gitea is not None:
            self.gitea = gitea
        if github is not None:
            self.github = github
        if gitlab is not None:
            self.gitlab = gitlab
        if requeue_after_seconds is not None:
            self.requeue_after_seconds = requeue_after_seconds
        if template is not None:
            self.template = template

    @property
    def azuredevops(self):
        """Gets the azuredevops of this V1alpha1PullRequestGenerator.  # noqa: E501


        :return: The azuredevops of this V1alpha1PullRequestGenerator.  # noqa: E501
        :rtype: V1alpha1PullRequestGeneratorAzureDevOps
        """
        return self._azuredevops

    @azuredevops.setter
    def azuredevops(self, azuredevops):
        """Sets the azuredevops of this V1alpha1PullRequestGenerator.


        :param azuredevops: The azuredevops of this V1alpha1PullRequestGenerator.  # noqa: E501
        :type: V1alpha1PullRequestGeneratorAzureDevOps
        """

        self._azuredevops = azuredevops

    @property
    def bitbucket(self):
        """Gets the bitbucket of this V1alpha1PullRequestGenerator.  # noqa: E501


        :return: The bitbucket of this V1alpha1PullRequestGenerator.  # noqa: E501
        :rtype: V1alpha1PullRequestGeneratorBitbucket
        """
        return self._bitbucket

    @bitbucket.setter
    def bitbucket(self, bitbucket):
        """Sets the bitbucket of this V1alpha1PullRequestGenerator.


        :param bitbucket: The bitbucket of this V1alpha1PullRequestGenerator.  # noqa: E501
        :type: V1alpha1PullRequestGeneratorBitbucket
        """

        self._bitbucket = bitbucket

    @property
    def bitbucket_server(self):
        """Gets the bitbucket_server of this V1alpha1PullRequestGenerator.  # noqa: E501


        :return: The bitbucket_server of this V1alpha1PullRequestGenerator.  # noqa: E501
        :rtype: V1alpha1PullRequestGeneratorBitbucketServer
        """
        return self._bitbucket_server

    @bitbucket_server.setter
    def bitbucket_server(self, bitbucket_server):
        """Sets the bitbucket_server of this V1alpha1PullRequestGenerator.


        :param bitbucket_server: The bitbucket_server of this V1alpha1PullRequestGenerator.  # noqa: E501
        :type: V1alpha1PullRequestGeneratorBitbucketServer
        """

        self._bitbucket_server = bitbucket_server

    @property
    def filters(self):
        """Gets the filters of this V1alpha1PullRequestGenerator.  # noqa: E501

        Filters for which pull requests should be considered.  # noqa: E501

        :return: The filters of this V1alpha1PullRequestGenerator.  # noqa: E501
        :rtype: list[V1alpha1PullRequestGeneratorFilter]
        """
        return self._filters

    @filters.setter
    def filters(self, filters):
        """Sets the filters of this V1alpha1PullRequestGenerator.

        Filters for which pull requests should be considered.  # noqa: E501

        :param filters: The filters of this V1alpha1PullRequestGenerator.  # noqa: E501
        :type: list[V1alpha1PullRequestGeneratorFilter]
        """

        self._filters = filters

    @property
    def gitea(self):
        """Gets the gitea of this V1alpha1PullRequestGenerator.  # noqa: E501


        :return: The gitea of this V1alpha1PullRequestGenerator.  # noqa: E501
        :rtype: V1alpha1PullRequestGeneratorGitea
        """
        return self._gitea

    @gitea.setter
    def gitea(self, gitea):
        """Sets the gitea of this V1alpha1PullRequestGenerator.


        :param gitea: The gitea of this V1alpha1PullRequestGenerator.  # noqa: E501
        :type: V1alpha1PullRequestGeneratorGitea
        """

        self._gitea = gitea

    @property
    def github(self):
        """Gets the github of this V1alpha1PullRequestGenerator.  # noqa: E501


        :return: The github of this V1alpha1PullRequestGenerator.  # noqa: E501
        :rtype: V1alpha1PullRequestGeneratorGithub
        """
        return self._github

    @github.setter
    def github(self, github):
        """Sets the github of this V1alpha1PullRequestGenerator.


        :param github: The github of this V1alpha1PullRequestGenerator.  # noqa: E501
        :type: V1alpha1PullRequestGeneratorGithub
        """

        self._github = github

    @property
    def gitlab(self):
        """Gets the gitlab of this V1alpha1PullRequestGenerator.  # noqa: E501


        :return: The gitlab of this V1alpha1PullRequestGenerator.  # noqa: E501
        :rtype: V1alpha1PullRequestGeneratorGitLab
        """
        return self._gitlab

    @gitlab.setter
    def gitlab(self, gitlab):
        """Sets the gitlab of this V1alpha1PullRequestGenerator.


        :param gitlab: The gitlab of this V1alpha1PullRequestGenerator.  # noqa: E501
        :type: V1alpha1PullRequestGeneratorGitLab
        """

        self._gitlab = gitlab

    @property
    def requeue_after_seconds(self):
        """Gets the requeue_after_seconds of this V1alpha1PullRequestGenerator.  # noqa: E501

        Standard parameters.  # noqa: E501

        :return: The requeue_after_seconds of this V1alpha1PullRequestGenerator.  # noqa: E501
        :rtype: int
        """
        return self._requeue_after_seconds

    @requeue_after_seconds.setter
    def requeue_after_seconds(self, requeue_after_seconds):
        """Sets the requeue_after_seconds of this V1alpha1PullRequestGenerator.

        Standard parameters.  # noqa: E501

        :param requeue_after_seconds: The requeue_after_seconds of this V1alpha1PullRequestGenerator.  # noqa: E501
        :type: int
        """

        self._requeue_after_seconds = requeue_after_seconds

    @property
    def template(self):
        """Gets the template of this V1alpha1PullRequestGenerator.  # noqa: E501


        :return: The template of this V1alpha1PullRequestGenerator.  # noqa: E501
        :rtype: V1alpha1ApplicationSetTemplate
        """
        return self._template

    @template.setter
    def template(self, template):
        """Sets the template of this V1alpha1PullRequestGenerator.


        :param template: The template of this V1alpha1PullRequestGenerator.  # noqa: E501
        :type: V1alpha1ApplicationSetTemplate
        """

        self._template = template

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
        if issubclass(V1alpha1PullRequestGenerator, dict):
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
        if not isinstance(other, V1alpha1PullRequestGenerator):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1alpha1PullRequestGenerator):
            return True

        return self.to_dict() != other.to_dict()

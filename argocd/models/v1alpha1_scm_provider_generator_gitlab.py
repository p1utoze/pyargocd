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


class V1alpha1SCMProviderGeneratorGitlab(object):
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
        'all_branches': 'bool',
        'api': 'str',
        'ca_ref': 'V1alpha1ConfigMapKeyRef',
        'group': 'str',
        'include_shared_projects': 'bool',
        'include_subgroups': 'bool',
        'insecure': 'bool',
        'token_ref': 'V1alpha1SecretRef',
        'topic': 'str'
    }

    attribute_map = {
        'all_branches': 'allBranches',
        'api': 'api',
        'ca_ref': 'caRef',
        'group': 'group',
        'include_shared_projects': 'includeSharedProjects',
        'include_subgroups': 'includeSubgroups',
        'insecure': 'insecure',
        'token_ref': 'tokenRef',
        'topic': 'topic'
    }

    def __init__(self, all_branches=None, api=None, ca_ref=None, group=None, include_shared_projects=None, include_subgroups=None, insecure=None, token_ref=None, topic=None, _configuration=None):  # noqa: E501
        """V1alpha1SCMProviderGeneratorGitlab - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._all_branches = None
        self._api = None
        self._ca_ref = None
        self._group = None
        self._include_shared_projects = None
        self._include_subgroups = None
        self._insecure = None
        self._token_ref = None
        self._topic = None
        self.discriminator = None

        if all_branches is not None:
            self.all_branches = all_branches
        if api is not None:
            self.api = api
        if ca_ref is not None:
            self.ca_ref = ca_ref
        if group is not None:
            self.group = group
        if include_shared_projects is not None:
            self.include_shared_projects = include_shared_projects
        if include_subgroups is not None:
            self.include_subgroups = include_subgroups
        if insecure is not None:
            self.insecure = insecure
        if token_ref is not None:
            self.token_ref = token_ref
        if topic is not None:
            self.topic = topic

    @property
    def all_branches(self):
        """Gets the all_branches of this V1alpha1SCMProviderGeneratorGitlab.  # noqa: E501

        Scan all branches instead of just the default branch.  # noqa: E501

        :return: The all_branches of this V1alpha1SCMProviderGeneratorGitlab.  # noqa: E501
        :rtype: bool
        """
        return self._all_branches

    @all_branches.setter
    def all_branches(self, all_branches):
        """Sets the all_branches of this V1alpha1SCMProviderGeneratorGitlab.

        Scan all branches instead of just the default branch.  # noqa: E501

        :param all_branches: The all_branches of this V1alpha1SCMProviderGeneratorGitlab.  # noqa: E501
        :type: bool
        """

        self._all_branches = all_branches

    @property
    def api(self):
        """Gets the api of this V1alpha1SCMProviderGeneratorGitlab.  # noqa: E501

        The Gitlab API URL to talk to.  # noqa: E501

        :return: The api of this V1alpha1SCMProviderGeneratorGitlab.  # noqa: E501
        :rtype: str
        """
        return self._api

    @api.setter
    def api(self, api):
        """Sets the api of this V1alpha1SCMProviderGeneratorGitlab.

        The Gitlab API URL to talk to.  # noqa: E501

        :param api: The api of this V1alpha1SCMProviderGeneratorGitlab.  # noqa: E501
        :type: str
        """

        self._api = api

    @property
    def ca_ref(self):
        """Gets the ca_ref of this V1alpha1SCMProviderGeneratorGitlab.  # noqa: E501


        :return: The ca_ref of this V1alpha1SCMProviderGeneratorGitlab.  # noqa: E501
        :rtype: V1alpha1ConfigMapKeyRef
        """
        return self._ca_ref

    @ca_ref.setter
    def ca_ref(self, ca_ref):
        """Sets the ca_ref of this V1alpha1SCMProviderGeneratorGitlab.


        :param ca_ref: The ca_ref of this V1alpha1SCMProviderGeneratorGitlab.  # noqa: E501
        :type: V1alpha1ConfigMapKeyRef
        """

        self._ca_ref = ca_ref

    @property
    def group(self):
        """Gets the group of this V1alpha1SCMProviderGeneratorGitlab.  # noqa: E501

        Gitlab group to scan. Required.  You can use either the project id (recommended) or the full namespaced path.  # noqa: E501

        :return: The group of this V1alpha1SCMProviderGeneratorGitlab.  # noqa: E501
        :rtype: str
        """
        return self._group

    @group.setter
    def group(self, group):
        """Sets the group of this V1alpha1SCMProviderGeneratorGitlab.

        Gitlab group to scan. Required.  You can use either the project id (recommended) or the full namespaced path.  # noqa: E501

        :param group: The group of this V1alpha1SCMProviderGeneratorGitlab.  # noqa: E501
        :type: str
        """

        self._group = group

    @property
    def include_shared_projects(self):
        """Gets the include_shared_projects of this V1alpha1SCMProviderGeneratorGitlab.  # noqa: E501


        :return: The include_shared_projects of this V1alpha1SCMProviderGeneratorGitlab.  # noqa: E501
        :rtype: bool
        """
        return self._include_shared_projects

    @include_shared_projects.setter
    def include_shared_projects(self, include_shared_projects):
        """Sets the include_shared_projects of this V1alpha1SCMProviderGeneratorGitlab.


        :param include_shared_projects: The include_shared_projects of this V1alpha1SCMProviderGeneratorGitlab.  # noqa: E501
        :type: bool
        """

        self._include_shared_projects = include_shared_projects

    @property
    def include_subgroups(self):
        """Gets the include_subgroups of this V1alpha1SCMProviderGeneratorGitlab.  # noqa: E501


        :return: The include_subgroups of this V1alpha1SCMProviderGeneratorGitlab.  # noqa: E501
        :rtype: bool
        """
        return self._include_subgroups

    @include_subgroups.setter
    def include_subgroups(self, include_subgroups):
        """Sets the include_subgroups of this V1alpha1SCMProviderGeneratorGitlab.


        :param include_subgroups: The include_subgroups of this V1alpha1SCMProviderGeneratorGitlab.  # noqa: E501
        :type: bool
        """

        self._include_subgroups = include_subgroups

    @property
    def insecure(self):
        """Gets the insecure of this V1alpha1SCMProviderGeneratorGitlab.  # noqa: E501


        :return: The insecure of this V1alpha1SCMProviderGeneratorGitlab.  # noqa: E501
        :rtype: bool
        """
        return self._insecure

    @insecure.setter
    def insecure(self, insecure):
        """Sets the insecure of this V1alpha1SCMProviderGeneratorGitlab.


        :param insecure: The insecure of this V1alpha1SCMProviderGeneratorGitlab.  # noqa: E501
        :type: bool
        """

        self._insecure = insecure

    @property
    def token_ref(self):
        """Gets the token_ref of this V1alpha1SCMProviderGeneratorGitlab.  # noqa: E501


        :return: The token_ref of this V1alpha1SCMProviderGeneratorGitlab.  # noqa: E501
        :rtype: V1alpha1SecretRef
        """
        return self._token_ref

    @token_ref.setter
    def token_ref(self, token_ref):
        """Sets the token_ref of this V1alpha1SCMProviderGeneratorGitlab.


        :param token_ref: The token_ref of this V1alpha1SCMProviderGeneratorGitlab.  # noqa: E501
        :type: V1alpha1SecretRef
        """

        self._token_ref = token_ref

    @property
    def topic(self):
        """Gets the topic of this V1alpha1SCMProviderGeneratorGitlab.  # noqa: E501

        Filter repos list based on Gitlab Topic.  # noqa: E501

        :return: The topic of this V1alpha1SCMProviderGeneratorGitlab.  # noqa: E501
        :rtype: str
        """
        return self._topic

    @topic.setter
    def topic(self, topic):
        """Sets the topic of this V1alpha1SCMProviderGeneratorGitlab.

        Filter repos list based on Gitlab Topic.  # noqa: E501

        :param topic: The topic of this V1alpha1SCMProviderGeneratorGitlab.  # noqa: E501
        :type: str
        """

        self._topic = topic

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
        if issubclass(V1alpha1SCMProviderGeneratorGitlab, dict):
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
        if not isinstance(other, V1alpha1SCMProviderGeneratorGitlab):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1alpha1SCMProviderGeneratorGitlab):
            return True

        return self.to_dict() != other.to_dict()

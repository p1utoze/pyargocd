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


class V1alpha1ApplicationSetApplicationStatus(object):
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
        'application': 'str',
        'last_transition_time': 'V1Time',
        'message': 'str',
        'status': 'str',
        'step': 'str',
        'targetrevisions': 'list[str]'
    }

    attribute_map = {
        'application': 'application',
        'last_transition_time': 'lastTransitionTime',
        'message': 'message',
        'status': 'status',
        'step': 'step',
        'targetrevisions': 'targetrevisions'
    }

    def __init__(self, application=None, last_transition_time=None, message=None, status=None, step=None, targetrevisions=None, _configuration=None):  # noqa: E501
        """V1alpha1ApplicationSetApplicationStatus - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._application = None
        self._last_transition_time = None
        self._message = None
        self._status = None
        self._step = None
        self._targetrevisions = None
        self.discriminator = None

        if application is not None:
            self.application = application
        if last_transition_time is not None:
            self.last_transition_time = last_transition_time
        if message is not None:
            self.message = message
        if status is not None:
            self.status = status
        if step is not None:
            self.step = step
        if targetrevisions is not None:
            self.targetrevisions = targetrevisions

    @property
    def application(self):
        """Gets the application of this V1alpha1ApplicationSetApplicationStatus.  # noqa: E501


        :return: The application of this V1alpha1ApplicationSetApplicationStatus.  # noqa: E501
        :rtype: str
        """
        return self._application

    @application.setter
    def application(self, application):
        """Sets the application of this V1alpha1ApplicationSetApplicationStatus.


        :param application: The application of this V1alpha1ApplicationSetApplicationStatus.  # noqa: E501
        :type: str
        """

        self._application = application

    @property
    def last_transition_time(self):
        """Gets the last_transition_time of this V1alpha1ApplicationSetApplicationStatus.  # noqa: E501


        :return: The last_transition_time of this V1alpha1ApplicationSetApplicationStatus.  # noqa: E501
        :rtype: V1Time
        """
        return self._last_transition_time

    @last_transition_time.setter
    def last_transition_time(self, last_transition_time):
        """Sets the last_transition_time of this V1alpha1ApplicationSetApplicationStatus.


        :param last_transition_time: The last_transition_time of this V1alpha1ApplicationSetApplicationStatus.  # noqa: E501
        :type: V1Time
        """

        self._last_transition_time = last_transition_time

    @property
    def message(self):
        """Gets the message of this V1alpha1ApplicationSetApplicationStatus.  # noqa: E501


        :return: The message of this V1alpha1ApplicationSetApplicationStatus.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this V1alpha1ApplicationSetApplicationStatus.


        :param message: The message of this V1alpha1ApplicationSetApplicationStatus.  # noqa: E501
        :type: str
        """

        self._message = message

    @property
    def status(self):
        """Gets the status of this V1alpha1ApplicationSetApplicationStatus.  # noqa: E501


        :return: The status of this V1alpha1ApplicationSetApplicationStatus.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this V1alpha1ApplicationSetApplicationStatus.


        :param status: The status of this V1alpha1ApplicationSetApplicationStatus.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def step(self):
        """Gets the step of this V1alpha1ApplicationSetApplicationStatus.  # noqa: E501


        :return: The step of this V1alpha1ApplicationSetApplicationStatus.  # noqa: E501
        :rtype: str
        """
        return self._step

    @step.setter
    def step(self, step):
        """Sets the step of this V1alpha1ApplicationSetApplicationStatus.


        :param step: The step of this V1alpha1ApplicationSetApplicationStatus.  # noqa: E501
        :type: str
        """

        self._step = step

    @property
    def targetrevisions(self):
        """Gets the targetrevisions of this V1alpha1ApplicationSetApplicationStatus.  # noqa: E501

        TargetRevision tracks the desired revisions the Application should be synced to.  # noqa: E501

        :return: The targetrevisions of this V1alpha1ApplicationSetApplicationStatus.  # noqa: E501
        :rtype: list[str]
        """
        return self._targetrevisions

    @targetrevisions.setter
    def targetrevisions(self, targetrevisions):
        """Sets the targetrevisions of this V1alpha1ApplicationSetApplicationStatus.

        TargetRevision tracks the desired revisions the Application should be synced to.  # noqa: E501

        :param targetrevisions: The targetrevisions of this V1alpha1ApplicationSetApplicationStatus.  # noqa: E501
        :type: list[str]
        """

        self._targetrevisions = targetrevisions

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
        if issubclass(V1alpha1ApplicationSetApplicationStatus, dict):
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
        if not isinstance(other, V1alpha1ApplicationSetApplicationStatus):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1alpha1ApplicationSetApplicationStatus):
            return True

        return self.to_dict() != other.to_dict()

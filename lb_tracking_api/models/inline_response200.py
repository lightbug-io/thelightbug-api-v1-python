# coding: utf-8

"""
    TrackingAPI

    API for retrieving tracking data and changing settings on LightBug & RemoteThings tracking devices  # noqa: E501

    OpenAPI spec version: 1.1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class InlineResponse200(object):
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
        'client_id': 'str',
        'username': 'str',
        'password': 'str'
    }

    attribute_map = {
        'client_id': 'clientId',
        'username': 'username',
        'password': 'password'
    }

    def __init__(self, client_id=None, username=None, password=None):  # noqa: E501
        """InlineResponse200 - a model defined in Swagger"""  # noqa: E501

        self._client_id = None
        self._username = None
        self._password = None
        self.discriminator = None

        if client_id is not None:
            self.client_id = client_id
        if username is not None:
            self.username = username
        if password is not None:
            self.password = password

    @property
    def client_id(self):
        """Gets the client_id of this InlineResponse200.  # noqa: E501


        :return: The client_id of this InlineResponse200.  # noqa: E501
        :rtype: str
        """
        return self._client_id

    @client_id.setter
    def client_id(self, client_id):
        """Sets the client_id of this InlineResponse200.


        :param client_id: The client_id of this InlineResponse200.  # noqa: E501
        :type: str
        """

        self._client_id = client_id

    @property
    def username(self):
        """Gets the username of this InlineResponse200.  # noqa: E501


        :return: The username of this InlineResponse200.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this InlineResponse200.


        :param username: The username of this InlineResponse200.  # noqa: E501
        :type: str
        """

        self._username = username

    @property
    def password(self):
        """Gets the password of this InlineResponse200.  # noqa: E501


        :return: The password of this InlineResponse200.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this InlineResponse200.


        :param password: The password of this InlineResponse200.  # noqa: E501
        :type: str
        """

        self._password = password

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
        if issubclass(InlineResponse200, dict):
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
        if not isinstance(other, InlineResponse200):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

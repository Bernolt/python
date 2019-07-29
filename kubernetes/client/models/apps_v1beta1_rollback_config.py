# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1.14.5
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class AppsV1beta1RollbackConfig(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
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
        'revision': 'int'
    }

    attribute_map = {
        'revision': 'revision'
    }

    def __init__(self, revision=None):
        """
        AppsV1beta1RollbackConfig - a model defined in Swagger
        """

        self._revision = None
        self.discriminator = None

        if revision is not None:
          self.revision = revision

    @property
    def revision(self):
        """
        Gets the revision of this AppsV1beta1RollbackConfig.
        The revision to rollback to. If set to 0, rollback to the last revision.

        :return: The revision of this AppsV1beta1RollbackConfig.
        :rtype: int
        """
        return self._revision

    @revision.setter
    def revision(self, revision):
        """
        Sets the revision of this AppsV1beta1RollbackConfig.
        The revision to rollback to. If set to 0, rollback to the last revision.

        :param revision: The revision of this AppsV1beta1RollbackConfig.
        :type: int
        """

        self._revision = revision

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, AppsV1beta1RollbackConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

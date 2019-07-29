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


class V1TopologySelectorTerm(object):
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
        'match_label_expressions': 'list[V1TopologySelectorLabelRequirement]'
    }

    attribute_map = {
        'match_label_expressions': 'matchLabelExpressions'
    }

    def __init__(self, match_label_expressions=None):
        """
        V1TopologySelectorTerm - a model defined in Swagger
        """

        self._match_label_expressions = None
        self.discriminator = None

        if match_label_expressions is not None:
          self.match_label_expressions = match_label_expressions

    @property
    def match_label_expressions(self):
        """
        Gets the match_label_expressions of this V1TopologySelectorTerm.
        A list of topology selector requirements by labels.

        :return: The match_label_expressions of this V1TopologySelectorTerm.
        :rtype: list[V1TopologySelectorLabelRequirement]
        """
        return self._match_label_expressions

    @match_label_expressions.setter
    def match_label_expressions(self, match_label_expressions):
        """
        Sets the match_label_expressions of this V1TopologySelectorTerm.
        A list of topology selector requirements by labels.

        :param match_label_expressions: The match_label_expressions of this V1TopologySelectorTerm.
        :type: list[V1TopologySelectorLabelRequirement]
        """

        self._match_label_expressions = match_label_expressions

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
        if not isinstance(other, V1TopologySelectorTerm):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

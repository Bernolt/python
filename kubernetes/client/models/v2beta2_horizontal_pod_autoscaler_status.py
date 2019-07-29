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


class V2beta2HorizontalPodAutoscalerStatus(object):
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
        'conditions': 'list[V2beta2HorizontalPodAutoscalerCondition]',
        'current_metrics': 'list[V2beta2MetricStatus]',
        'current_replicas': 'int',
        'desired_replicas': 'int',
        'last_scale_time': 'datetime',
        'observed_generation': 'int'
    }

    attribute_map = {
        'conditions': 'conditions',
        'current_metrics': 'currentMetrics',
        'current_replicas': 'currentReplicas',
        'desired_replicas': 'desiredReplicas',
        'last_scale_time': 'lastScaleTime',
        'observed_generation': 'observedGeneration'
    }

    def __init__(self, conditions=None, current_metrics=None, current_replicas=None, desired_replicas=None, last_scale_time=None, observed_generation=None):
        """
        V2beta2HorizontalPodAutoscalerStatus - a model defined in Swagger
        """

        self._conditions = None
        self._current_metrics = None
        self._current_replicas = None
        self._desired_replicas = None
        self._last_scale_time = None
        self._observed_generation = None
        self.discriminator = None

        self.conditions = conditions
        if current_metrics is not None:
          self.current_metrics = current_metrics
        self.current_replicas = current_replicas
        self.desired_replicas = desired_replicas
        if last_scale_time is not None:
          self.last_scale_time = last_scale_time
        if observed_generation is not None:
          self.observed_generation = observed_generation

    @property
    def conditions(self):
        """
        Gets the conditions of this V2beta2HorizontalPodAutoscalerStatus.
        conditions is the set of conditions required for this autoscaler to scale its target, and indicates whether or not those conditions are met.

        :return: The conditions of this V2beta2HorizontalPodAutoscalerStatus.
        :rtype: list[V2beta2HorizontalPodAutoscalerCondition]
        """
        return self._conditions

    @conditions.setter
    def conditions(self, conditions):
        """
        Sets the conditions of this V2beta2HorizontalPodAutoscalerStatus.
        conditions is the set of conditions required for this autoscaler to scale its target, and indicates whether or not those conditions are met.

        :param conditions: The conditions of this V2beta2HorizontalPodAutoscalerStatus.
        :type: list[V2beta2HorizontalPodAutoscalerCondition]
        """
        if conditions is None:
            raise ValueError("Invalid value for `conditions`, must not be `None`")

        self._conditions = conditions

    @property
    def current_metrics(self):
        """
        Gets the current_metrics of this V2beta2HorizontalPodAutoscalerStatus.
        currentMetrics is the last read state of the metrics used by this autoscaler.

        :return: The current_metrics of this V2beta2HorizontalPodAutoscalerStatus.
        :rtype: list[V2beta2MetricStatus]
        """
        return self._current_metrics

    @current_metrics.setter
    def current_metrics(self, current_metrics):
        """
        Sets the current_metrics of this V2beta2HorizontalPodAutoscalerStatus.
        currentMetrics is the last read state of the metrics used by this autoscaler.

        :param current_metrics: The current_metrics of this V2beta2HorizontalPodAutoscalerStatus.
        :type: list[V2beta2MetricStatus]
        """

        self._current_metrics = current_metrics

    @property
    def current_replicas(self):
        """
        Gets the current_replicas of this V2beta2HorizontalPodAutoscalerStatus.
        currentReplicas is current number of replicas of pods managed by this autoscaler, as last seen by the autoscaler.

        :return: The current_replicas of this V2beta2HorizontalPodAutoscalerStatus.
        :rtype: int
        """
        return self._current_replicas

    @current_replicas.setter
    def current_replicas(self, current_replicas):
        """
        Sets the current_replicas of this V2beta2HorizontalPodAutoscalerStatus.
        currentReplicas is current number of replicas of pods managed by this autoscaler, as last seen by the autoscaler.

        :param current_replicas: The current_replicas of this V2beta2HorizontalPodAutoscalerStatus.
        :type: int
        """
        if current_replicas is None:
            raise ValueError("Invalid value for `current_replicas`, must not be `None`")

        self._current_replicas = current_replicas

    @property
    def desired_replicas(self):
        """
        Gets the desired_replicas of this V2beta2HorizontalPodAutoscalerStatus.
        desiredReplicas is the desired number of replicas of pods managed by this autoscaler, as last calculated by the autoscaler.

        :return: The desired_replicas of this V2beta2HorizontalPodAutoscalerStatus.
        :rtype: int
        """
        return self._desired_replicas

    @desired_replicas.setter
    def desired_replicas(self, desired_replicas):
        """
        Sets the desired_replicas of this V2beta2HorizontalPodAutoscalerStatus.
        desiredReplicas is the desired number of replicas of pods managed by this autoscaler, as last calculated by the autoscaler.

        :param desired_replicas: The desired_replicas of this V2beta2HorizontalPodAutoscalerStatus.
        :type: int
        """
        if desired_replicas is None:
            raise ValueError("Invalid value for `desired_replicas`, must not be `None`")

        self._desired_replicas = desired_replicas

    @property
    def last_scale_time(self):
        """
        Gets the last_scale_time of this V2beta2HorizontalPodAutoscalerStatus.
        lastScaleTime is the last time the HorizontalPodAutoscaler scaled the number of pods, used by the autoscaler to control how often the number of pods is changed.

        :return: The last_scale_time of this V2beta2HorizontalPodAutoscalerStatus.
        :rtype: datetime
        """
        return self._last_scale_time

    @last_scale_time.setter
    def last_scale_time(self, last_scale_time):
        """
        Sets the last_scale_time of this V2beta2HorizontalPodAutoscalerStatus.
        lastScaleTime is the last time the HorizontalPodAutoscaler scaled the number of pods, used by the autoscaler to control how often the number of pods is changed.

        :param last_scale_time: The last_scale_time of this V2beta2HorizontalPodAutoscalerStatus.
        :type: datetime
        """

        self._last_scale_time = last_scale_time

    @property
    def observed_generation(self):
        """
        Gets the observed_generation of this V2beta2HorizontalPodAutoscalerStatus.
        observedGeneration is the most recent generation observed by this autoscaler.

        :return: The observed_generation of this V2beta2HorizontalPodAutoscalerStatus.
        :rtype: int
        """
        return self._observed_generation

    @observed_generation.setter
    def observed_generation(self, observed_generation):
        """
        Sets the observed_generation of this V2beta2HorizontalPodAutoscalerStatus.
        observedGeneration is the most recent generation observed by this autoscaler.

        :param observed_generation: The observed_generation of this V2beta2HorizontalPodAutoscalerStatus.
        :type: int
        """

        self._observed_generation = observed_generation

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
        if not isinstance(other, V2beta2HorizontalPodAutoscalerStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

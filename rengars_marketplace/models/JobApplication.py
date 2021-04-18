# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from rengars_marketplace.models.Model import Model
from rengars_marketplace.models.JobApplicationState import JobApplicationState  # noqa: F401,E501
from rengars_marketplace.models.User import User  # noqa: F401,E501
from rengars_marketplace import util


class JobApplication(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, id: int = None, applicant: User = None, note: str = None, job_offer_id: int = None,
                 state: JobApplicationState = None, date_created: datetime = None,
                 date_closed: datetime = None):  # noqa: E501
        """JobApplication - a model defined in Swagger

        :param id: The id of this JobApplication.  # noqa: E501
        :type id: int
        :param applicant: The applicant of this JobApplication.  # noqa: E501
        :type applicant: User
        :param note: The note of this JobApplication.  # noqa: E501
        :type note: str
        :param job_offer_id: The job_offer_id of this JobApplication.  # noqa: E501
        :type job_offer_id: int
        :param state: The state of this JobApplication.  # noqa: E501
        :type state: JobApplicationState
        :param date_created: The date_created of this JobApplication.  # noqa: E501
        :type date_created: datetime
        :param date_closed: The date_closed of this JobApplication.  # noqa: E501
        :type date_closed: datetime
        """
        self.swagger_types = {
            'id': int,
            'applicant': User,
            'note': str,
            'job_offer_id': int,
            'state': JobApplicationState,
            'date_created': datetime,
            'date_closed': datetime
        }

        self.attribute_map = {
            'id': 'id',
            'applicant': 'applicant',
            'note': 'note',
            'job_offer_id': 'jobOfferId',
            'state': 'state',
            'date_created': 'dateCreated',
            'date_closed': 'dateClosed'
        }
        self._id = id
        self._applicant = applicant
        self._note = note
        self._job_offer_id = job_offer_id
        self._state = state
        self._date_created = date_created
        self._date_closed = date_closed

    @classmethod
    def from_dict(cls, dikt) -> 'JobApplication':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The JobApplication of this JobApplication.  # noqa: E501
        :rtype: JobApplication
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> int:
        """Gets the id of this JobApplication.


        :return: The id of this JobApplication.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id: int):
        """Sets the id of this JobApplication.


        :param id: The id of this JobApplication.
        :type id: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def applicant(self) -> User:
        """Gets the applicant of this JobApplication.


        :return: The applicant of this JobApplication.
        :rtype: User
        """
        return self._applicant

    @applicant.setter
    def applicant(self, applicant: User):
        """Sets the applicant of this JobApplication.


        :param applicant: The applicant of this JobApplication.
        :type applicant: User
        """
        if applicant is None:
            raise ValueError("Invalid value for `applicant`, must not be `None`")  # noqa: E501

        self._applicant = applicant

    @property
    def note(self) -> str:
        """Gets the note of this JobApplication.


        :return: The note of this JobApplication.
        :rtype: str
        """
        return self._note

    @note.setter
    def note(self, note: str):
        """Sets the note of this JobApplication.


        :param note: The note of this JobApplication.
        :type note: str
        """
        if note is None:
            raise ValueError("Invalid value for `note`, must not be `None`")  # noqa: E501

        self._note = note

    @property
    def job_offer_id(self) -> int:
        """Gets the job_offer_id of this JobApplication.


        :return: The job_offer_id of this JobApplication.
        :rtype: int
        """
        return self._job_offer_id

    @job_offer_id.setter
    def job_offer_id(self, job_offer_id: int):
        """Sets the job_offer_id of this JobApplication.


        :param job_offer_id: The job_offer_id of this JobApplication.
        :type job_offer_id: int
        """
        if job_offer_id is None:
            raise ValueError("Invalid value for `job_offer_id`, must not be `None`")  # noqa: E501

        self._job_offer_id = job_offer_id

    @property
    def state(self) -> JobApplicationState:
        """Gets the state of this JobApplication.


        :return: The state of this JobApplication.
        :rtype: JobApplicationState
        """
        return self._state

    @state.setter
    def state(self, state: JobApplicationState):
        """Sets the state of this JobApplication.


        :param state: The state of this JobApplication.
        :type state: JobApplicationState
        """

        self._state = state

    @property
    def date_created(self) -> datetime:
        """Gets the date_created of this JobApplication.


        :return: The date_created of this JobApplication.
        :rtype: datetime
        """
        return self._date_created

    @date_created.setter
    def date_created(self, date_created: datetime):
        """Sets the date_created of this JobApplication.


        :param date_created: The date_created of this JobApplication.
        :type date_created: datetime
        """

        self._date_created = date_created

    @property
    def date_closed(self) -> datetime:
        """Gets the date_closed of this JobApplication.


        :return: The date_closed of this JobApplication.
        :rtype: datetime
        """
        return self._date_closed

    @date_closed.setter
    def date_closed(self, date_closed: datetime):
        """Sets the date_closed of this JobApplication.


        :param date_closed: The date_closed of this JobApplication.
        :type date_closed: datetime
        """

        self._date_closed = date_closed

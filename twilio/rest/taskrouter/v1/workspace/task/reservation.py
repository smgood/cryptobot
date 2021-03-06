# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from twilio.base import deserialize
from twilio.base import serialize
from twilio.base import values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.page import Page


class ReservationList(ListResource):
    """  """

    def __init__(self, version, workspace_sid, task_sid):
        """
        Initialize the ReservationList

        :param Version version: Version that contains the resource
        :param workspace_sid: The ID of the Workspace that this task is contained within.
        :param task_sid: The ID of the reserved Task

        :returns: twilio.rest.taskrouter.v1.workspace.task.reservation.ReservationList
        :rtype: twilio.rest.taskrouter.v1.workspace.task.reservation.ReservationList
        """
        super(ReservationList, self).__init__(version)

        # Path Solution
        self._solution = {'workspace_sid': workspace_sid, 'task_sid': task_sid, }
        self._uri = '/Workspaces/{workspace_sid}/Tasks/{task_sid}/Reservations'.format(**self._solution)

    def stream(self, reservation_status=values.unset, limit=None, page_size=None):
        """
        Streams ReservationInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param ReservationInstance.Status reservation_status: Returns the list of reservations for a task with a specified ReservationStatus
        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.taskrouter.v1.workspace.task.reservation.ReservationInstance]
        """
        limits = self._version.read_limits(limit, page_size)

        page = self.page(reservation_status=reservation_status, page_size=limits['page_size'], )

        return self._version.stream(page, limits['limit'], limits['page_limit'])

    def list(self, reservation_status=values.unset, limit=None, page_size=None):
        """
        Lists ReservationInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param ReservationInstance.Status reservation_status: Returns the list of reservations for a task with a specified ReservationStatus
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.taskrouter.v1.workspace.task.reservation.ReservationInstance]
        """
        return list(self.stream(reservation_status=reservation_status, limit=limit, page_size=page_size, ))

    def page(self, reservation_status=values.unset, page_token=values.unset,
             page_number=values.unset, page_size=values.unset):
        """
        Retrieve a single page of ReservationInstance records from the API.
        Request is executed immediately

        :param ReservationInstance.Status reservation_status: Returns the list of reservations for a task with a specified ReservationStatus
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of ReservationInstance
        :rtype: twilio.rest.taskrouter.v1.workspace.task.reservation.ReservationPage
        """
        params = values.of({
            'ReservationStatus': reservation_status,
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = self._version.page(
            'GET',
            self._uri,
            params=params,
        )

        return ReservationPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of ReservationInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of ReservationInstance
        :rtype: twilio.rest.taskrouter.v1.workspace.task.reservation.ReservationPage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url,
        )

        return ReservationPage(self._version, response, self._solution)

    def get(self, sid):
        """
        Constructs a ReservationContext

        :param sid: The sid

        :returns: twilio.rest.taskrouter.v1.workspace.task.reservation.ReservationContext
        :rtype: twilio.rest.taskrouter.v1.workspace.task.reservation.ReservationContext
        """
        return ReservationContext(
            self._version,
            workspace_sid=self._solution['workspace_sid'],
            task_sid=self._solution['task_sid'],
            sid=sid,
        )

    def __call__(self, sid):
        """
        Constructs a ReservationContext

        :param sid: The sid

        :returns: twilio.rest.taskrouter.v1.workspace.task.reservation.ReservationContext
        :rtype: twilio.rest.taskrouter.v1.workspace.task.reservation.ReservationContext
        """
        return ReservationContext(
            self._version,
            workspace_sid=self._solution['workspace_sid'],
            task_sid=self._solution['task_sid'],
            sid=sid,
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Taskrouter.V1.ReservationList>'


class ReservationPage(Page):
    """  """

    def __init__(self, version, response, solution):
        """
        Initialize the ReservationPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API
        :param workspace_sid: The ID of the Workspace that this task is contained within.
        :param task_sid: The ID of the reserved Task

        :returns: twilio.rest.taskrouter.v1.workspace.task.reservation.ReservationPage
        :rtype: twilio.rest.taskrouter.v1.workspace.task.reservation.ReservationPage
        """
        super(ReservationPage, self).__init__(version, response)

        # Path Solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of ReservationInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.taskrouter.v1.workspace.task.reservation.ReservationInstance
        :rtype: twilio.rest.taskrouter.v1.workspace.task.reservation.ReservationInstance
        """
        return ReservationInstance(
            self._version,
            payload,
            workspace_sid=self._solution['workspace_sid'],
            task_sid=self._solution['task_sid'],
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Taskrouter.V1.ReservationPage>'


class ReservationContext(InstanceContext):
    """  """

    def __init__(self, version, workspace_sid, task_sid, sid):
        """
        Initialize the ReservationContext

        :param Version version: Version that contains the resource
        :param workspace_sid: The workspace_sid
        :param task_sid: The task_sid
        :param sid: The sid

        :returns: twilio.rest.taskrouter.v1.workspace.task.reservation.ReservationContext
        :rtype: twilio.rest.taskrouter.v1.workspace.task.reservation.ReservationContext
        """
        super(ReservationContext, self).__init__(version)

        # Path Solution
        self._solution = {'workspace_sid': workspace_sid, 'task_sid': task_sid, 'sid': sid, }
        self._uri = '/Workspaces/{workspace_sid}/Tasks/{task_sid}/Reservations/{sid}'.format(**self._solution)

    def fetch(self):
        """
        Fetch a ReservationInstance

        :returns: Fetched ReservationInstance
        :rtype: twilio.rest.taskrouter.v1.workspace.task.reservation.ReservationInstance
        """
        params = values.of({})

        payload = self._version.fetch(
            'GET',
            self._uri,
            params=params,
        )

        return ReservationInstance(
            self._version,
            payload,
            workspace_sid=self._solution['workspace_sid'],
            task_sid=self._solution['task_sid'],
            sid=self._solution['sid'],
        )

    def update(self, reservation_status=values.unset,
               worker_activity_sid=values.unset, instruction=values.unset,
               dequeue_post_work_activity_sid=values.unset,
               dequeue_from=values.unset, dequeue_record=values.unset,
               dequeue_timeout=values.unset, dequeue_to=values.unset,
               dequeue_status_callback_url=values.unset, call_from=values.unset,
               call_record=values.unset, call_timeout=values.unset,
               call_to=values.unset, call_url=values.unset,
               call_status_callback_url=values.unset, call_accept=values.unset,
               redirect_call_sid=values.unset, redirect_accept=values.unset,
               redirect_url=values.unset, to=values.unset, from_=values.unset,
               status_callback=values.unset, status_callback_method=values.unset,
               status_callback_event=values.unset, timeout=values.unset,
               record=values.unset, muted=values.unset, beep=values.unset,
               start_conference_on_enter=values.unset,
               end_conference_on_exit=values.unset, wait_url=values.unset,
               wait_method=values.unset, early_media=values.unset,
               max_participants=values.unset,
               conference_status_callback=values.unset,
               conference_status_callback_method=values.unset,
               conference_status_callback_event=values.unset,
               conference_record=values.unset, conference_trim=values.unset,
               recording_channels=values.unset,
               recording_status_callback=values.unset,
               recording_status_callback_method=values.unset,
               conference_recording_status_callback=values.unset,
               conference_recording_status_callback_method=values.unset,
               region=values.unset, sip_auth_username=values.unset,
               sip_auth_password=values.unset,
               dequeue_status_callback_event=values.unset,
               post_work_activity_sid=values.unset):
        """
        Update the ReservationInstance

        :param ReservationInstance.Status reservation_status: Yes
        :param unicode worker_activity_sid: No
        :param unicode instruction: Yes
        :param unicode dequeue_post_work_activity_sid: No
        :param unicode dequeue_from: Yes
        :param unicode dequeue_record: No
        :param unicode dequeue_timeout: No
        :param unicode dequeue_to: No
        :param unicode dequeue_status_callback_url: No
        :param unicode call_from: Yes
        :param unicode call_record: No
        :param unicode call_timeout: No
        :param unicode call_to: No
        :param unicode call_url: Yes
        :param unicode call_status_callback_url: No
        :param bool call_accept: No
        :param unicode redirect_call_sid: Yes
        :param bool redirect_accept: No
        :param unicode redirect_url: Yes
        :param unicode to: No
        :param unicode from_: No
        :param unicode status_callback: The status_callback
        :param unicode status_callback_method: The status_callback_method
        :param ReservationInstance.CallStatus status_callback_event: The status_callback_event
        :param unicode timeout: No
        :param bool record: The record
        :param bool muted: The muted
        :param unicode beep: The beep
        :param bool start_conference_on_enter: The start_conference_on_enter
        :param bool end_conference_on_exit: The end_conference_on_exit
        :param unicode wait_url: The wait_url
        :param unicode wait_method: The wait_method
        :param bool early_media: The early_media
        :param unicode max_participants: The max_participants
        :param unicode conference_status_callback: The conference_status_callback
        :param unicode conference_status_callback_method: The conference_status_callback_method
        :param ReservationInstance.ConferenceEvent conference_status_callback_event: The conference_status_callback_event
        :param unicode conference_record: The conference_record
        :param unicode conference_trim: The conference_trim
        :param unicode recording_channels: The recording_channels
        :param unicode recording_status_callback: The recording_status_callback
        :param unicode recording_status_callback_method: The recording_status_callback_method
        :param unicode conference_recording_status_callback: The conference_recording_status_callback
        :param unicode conference_recording_status_callback_method: The conference_recording_status_callback_method
        :param unicode region: The region
        :param unicode sip_auth_username: The sip_auth_username
        :param unicode sip_auth_password: The sip_auth_password
        :param unicode dequeue_status_callback_event: No
        :param unicode post_work_activity_sid: No

        :returns: Updated ReservationInstance
        :rtype: twilio.rest.taskrouter.v1.workspace.task.reservation.ReservationInstance
        """
        data = values.of({
            'ReservationStatus': reservation_status,
            'WorkerActivitySid': worker_activity_sid,
            'Instruction': instruction,
            'DequeuePostWorkActivitySid': dequeue_post_work_activity_sid,
            'DequeueFrom': dequeue_from,
            'DequeueRecord': dequeue_record,
            'DequeueTimeout': dequeue_timeout,
            'DequeueTo': dequeue_to,
            'DequeueStatusCallbackUrl': dequeue_status_callback_url,
            'CallFrom': call_from,
            'CallRecord': call_record,
            'CallTimeout': call_timeout,
            'CallTo': call_to,
            'CallUrl': call_url,
            'CallStatusCallbackUrl': call_status_callback_url,
            'CallAccept': call_accept,
            'RedirectCallSid': redirect_call_sid,
            'RedirectAccept': redirect_accept,
            'RedirectUrl': redirect_url,
            'To': to,
            'From': from_,
            'StatusCallback': status_callback,
            'StatusCallbackMethod': status_callback_method,
            'StatusCallbackEvent': serialize.map(status_callback_event, lambda e: e),
            'Timeout': timeout,
            'Record': record,
            'Muted': muted,
            'Beep': beep,
            'StartConferenceOnEnter': start_conference_on_enter,
            'EndConferenceOnExit': end_conference_on_exit,
            'WaitUrl': wait_url,
            'WaitMethod': wait_method,
            'EarlyMedia': early_media,
            'MaxParticipants': max_participants,
            'ConferenceStatusCallback': conference_status_callback,
            'ConferenceStatusCallbackMethod': conference_status_callback_method,
            'ConferenceStatusCallbackEvent': serialize.map(conference_status_callback_event, lambda e: e),
            'ConferenceRecord': conference_record,
            'ConferenceTrim': conference_trim,
            'RecordingChannels': recording_channels,
            'RecordingStatusCallback': recording_status_callback,
            'RecordingStatusCallbackMethod': recording_status_callback_method,
            'ConferenceRecordingStatusCallback': conference_recording_status_callback,
            'ConferenceRecordingStatusCallbackMethod': conference_recording_status_callback_method,
            'Region': region,
            'SipAuthUsername': sip_auth_username,
            'SipAuthPassword': sip_auth_password,
            'DequeueStatusCallbackEvent': serialize.map(dequeue_status_callback_event, lambda e: e),
            'PostWorkActivitySid': post_work_activity_sid,
        })

        payload = self._version.update(
            'POST',
            self._uri,
            data=data,
        )

        return ReservationInstance(
            self._version,
            payload,
            workspace_sid=self._solution['workspace_sid'],
            task_sid=self._solution['task_sid'],
            sid=self._solution['sid'],
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Taskrouter.V1.ReservationContext {}>'.format(context)


class ReservationInstance(InstanceResource):
    """  """

    class Status(object):
        PENDING = "pending"
        ACCEPTED = "accepted"
        REJECTED = "rejected"
        TIMEOUT = "timeout"
        CANCELED = "canceled"
        RESCINDED = "rescinded"

    class CallStatus(object):
        INITIATED = "initiated"
        RINGING = "ringing"
        ANSWERED = "answered"
        COMPLETED = "completed"

    class ConferenceEvent(object):
        START = "start"
        END = "end"
        JOIN = "join"
        LEAVE = "leave"
        MUTE = "mute"
        HOLD = "hold"
        SPEAKER = "speaker"

    def __init__(self, version, payload, workspace_sid, task_sid, sid=None):
        """
        Initialize the ReservationInstance

        :returns: twilio.rest.taskrouter.v1.workspace.task.reservation.ReservationInstance
        :rtype: twilio.rest.taskrouter.v1.workspace.task.reservation.ReservationInstance
        """
        super(ReservationInstance, self).__init__(version)

        # Marshaled Properties
        self._properties = {
            'account_sid': payload['account_sid'],
            'date_created': deserialize.iso8601_datetime(payload['date_created']),
            'date_updated': deserialize.iso8601_datetime(payload['date_updated']),
            'reservation_status': payload['reservation_status'],
            'sid': payload['sid'],
            'task_sid': payload['task_sid'],
            'worker_name': payload['worker_name'],
            'worker_sid': payload['worker_sid'],
            'workspace_sid': payload['workspace_sid'],
            'url': payload['url'],
            'links': payload['links'],
        }

        # Context
        self._context = None
        self._solution = {
            'workspace_sid': workspace_sid,
            'task_sid': task_sid,
            'sid': sid or self._properties['sid'],
        }

    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions.  All instance actions are proxied to the context

        :returns: ReservationContext for this ReservationInstance
        :rtype: twilio.rest.taskrouter.v1.workspace.task.reservation.ReservationContext
        """
        if self._context is None:
            self._context = ReservationContext(
                self._version,
                workspace_sid=self._solution['workspace_sid'],
                task_sid=self._solution['task_sid'],
                sid=self._solution['sid'],
            )
        return self._context

    @property
    def account_sid(self):
        """
        :returns: The ID of the Account that owns this Task
        :rtype: unicode
        """
        return self._properties['account_sid']

    @property
    def date_created(self):
        """
        :returns: The date_created
        :rtype: datetime
        """
        return self._properties['date_created']

    @property
    def date_updated(self):
        """
        :returns: The date_updated
        :rtype: datetime
        """
        return self._properties['date_updated']

    @property
    def reservation_status(self):
        """
        :returns: The current status of the reservation.
        :rtype: ReservationInstance.Status
        """
        return self._properties['reservation_status']

    @property
    def sid(self):
        """
        :returns: The unique ID of this Reservation.
        :rtype: unicode
        """
        return self._properties['sid']

    @property
    def task_sid(self):
        """
        :returns: The ID of the reserved Task
        :rtype: unicode
        """
        return self._properties['task_sid']

    @property
    def worker_name(self):
        """
        :returns: Human readable description of the Worker that is reserved
        :rtype: unicode
        """
        return self._properties['worker_name']

    @property
    def worker_sid(self):
        """
        :returns: The ID of the reserved Worker
        :rtype: unicode
        """
        return self._properties['worker_sid']

    @property
    def workspace_sid(self):
        """
        :returns: The ID of the Workspace that this task is contained within.
        :rtype: unicode
        """
        return self._properties['workspace_sid']

    @property
    def url(self):
        """
        :returns: The url
        :rtype: unicode
        """
        return self._properties['url']

    @property
    def links(self):
        """
        :returns: The links
        :rtype: unicode
        """
        return self._properties['links']

    def fetch(self):
        """
        Fetch a ReservationInstance

        :returns: Fetched ReservationInstance
        :rtype: twilio.rest.taskrouter.v1.workspace.task.reservation.ReservationInstance
        """
        return self._proxy.fetch()

    def update(self, reservation_status=values.unset,
               worker_activity_sid=values.unset, instruction=values.unset,
               dequeue_post_work_activity_sid=values.unset,
               dequeue_from=values.unset, dequeue_record=values.unset,
               dequeue_timeout=values.unset, dequeue_to=values.unset,
               dequeue_status_callback_url=values.unset, call_from=values.unset,
               call_record=values.unset, call_timeout=values.unset,
               call_to=values.unset, call_url=values.unset,
               call_status_callback_url=values.unset, call_accept=values.unset,
               redirect_call_sid=values.unset, redirect_accept=values.unset,
               redirect_url=values.unset, to=values.unset, from_=values.unset,
               status_callback=values.unset, status_callback_method=values.unset,
               status_callback_event=values.unset, timeout=values.unset,
               record=values.unset, muted=values.unset, beep=values.unset,
               start_conference_on_enter=values.unset,
               end_conference_on_exit=values.unset, wait_url=values.unset,
               wait_method=values.unset, early_media=values.unset,
               max_participants=values.unset,
               conference_status_callback=values.unset,
               conference_status_callback_method=values.unset,
               conference_status_callback_event=values.unset,
               conference_record=values.unset, conference_trim=values.unset,
               recording_channels=values.unset,
               recording_status_callback=values.unset,
               recording_status_callback_method=values.unset,
               conference_recording_status_callback=values.unset,
               conference_recording_status_callback_method=values.unset,
               region=values.unset, sip_auth_username=values.unset,
               sip_auth_password=values.unset,
               dequeue_status_callback_event=values.unset,
               post_work_activity_sid=values.unset):
        """
        Update the ReservationInstance

        :param ReservationInstance.Status reservation_status: Yes
        :param unicode worker_activity_sid: No
        :param unicode instruction: Yes
        :param unicode dequeue_post_work_activity_sid: No
        :param unicode dequeue_from: Yes
        :param unicode dequeue_record: No
        :param unicode dequeue_timeout: No
        :param unicode dequeue_to: No
        :param unicode dequeue_status_callback_url: No
        :param unicode call_from: Yes
        :param unicode call_record: No
        :param unicode call_timeout: No
        :param unicode call_to: No
        :param unicode call_url: Yes
        :param unicode call_status_callback_url: No
        :param bool call_accept: No
        :param unicode redirect_call_sid: Yes
        :param bool redirect_accept: No
        :param unicode redirect_url: Yes
        :param unicode to: No
        :param unicode from_: No
        :param unicode status_callback: The status_callback
        :param unicode status_callback_method: The status_callback_method
        :param ReservationInstance.CallStatus status_callback_event: The status_callback_event
        :param unicode timeout: No
        :param bool record: The record
        :param bool muted: The muted
        :param unicode beep: The beep
        :param bool start_conference_on_enter: The start_conference_on_enter
        :param bool end_conference_on_exit: The end_conference_on_exit
        :param unicode wait_url: The wait_url
        :param unicode wait_method: The wait_method
        :param bool early_media: The early_media
        :param unicode max_participants: The max_participants
        :param unicode conference_status_callback: The conference_status_callback
        :param unicode conference_status_callback_method: The conference_status_callback_method
        :param ReservationInstance.ConferenceEvent conference_status_callback_event: The conference_status_callback_event
        :param unicode conference_record: The conference_record
        :param unicode conference_trim: The conference_trim
        :param unicode recording_channels: The recording_channels
        :param unicode recording_status_callback: The recording_status_callback
        :param unicode recording_status_callback_method: The recording_status_callback_method
        :param unicode conference_recording_status_callback: The conference_recording_status_callback
        :param unicode conference_recording_status_callback_method: The conference_recording_status_callback_method
        :param unicode region: The region
        :param unicode sip_auth_username: The sip_auth_username
        :param unicode sip_auth_password: The sip_auth_password
        :param unicode dequeue_status_callback_event: No
        :param unicode post_work_activity_sid: No

        :returns: Updated ReservationInstance
        :rtype: twilio.rest.taskrouter.v1.workspace.task.reservation.ReservationInstance
        """
        return self._proxy.update(
            reservation_status=reservation_status,
            worker_activity_sid=worker_activity_sid,
            instruction=instruction,
            dequeue_post_work_activity_sid=dequeue_post_work_activity_sid,
            dequeue_from=dequeue_from,
            dequeue_record=dequeue_record,
            dequeue_timeout=dequeue_timeout,
            dequeue_to=dequeue_to,
            dequeue_status_callback_url=dequeue_status_callback_url,
            call_from=call_from,
            call_record=call_record,
            call_timeout=call_timeout,
            call_to=call_to,
            call_url=call_url,
            call_status_callback_url=call_status_callback_url,
            call_accept=call_accept,
            redirect_call_sid=redirect_call_sid,
            redirect_accept=redirect_accept,
            redirect_url=redirect_url,
            to=to,
            from_=from_,
            status_callback=status_callback,
            status_callback_method=status_callback_method,
            status_callback_event=status_callback_event,
            timeout=timeout,
            record=record,
            muted=muted,
            beep=beep,
            start_conference_on_enter=start_conference_on_enter,
            end_conference_on_exit=end_conference_on_exit,
            wait_url=wait_url,
            wait_method=wait_method,
            early_media=early_media,
            max_participants=max_participants,
            conference_status_callback=conference_status_callback,
            conference_status_callback_method=conference_status_callback_method,
            conference_status_callback_event=conference_status_callback_event,
            conference_record=conference_record,
            conference_trim=conference_trim,
            recording_channels=recording_channels,
            recording_status_callback=recording_status_callback,
            recording_status_callback_method=recording_status_callback_method,
            conference_recording_status_callback=conference_recording_status_callback,
            conference_recording_status_callback_method=conference_recording_status_callback_method,
            region=region,
            sip_auth_username=sip_auth_username,
            sip_auth_password=sip_auth_password,
            dequeue_status_callback_event=dequeue_status_callback_event,
            post_work_activity_sid=post_work_activity_sid,
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Taskrouter.V1.ReservationInstance {}>'.format(context)

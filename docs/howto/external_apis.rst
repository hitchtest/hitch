How to test applications which call external APIs
=================================================

.. note::

    The pattern described here is the same that is currently used by :doc:`/plugins/hitchsmtp`.

While it is always preferable to test your application with real APIs wherever
feasible, it is often not feasible to test or develop against real APIs.

For example:

* APIs which cost money to use like SMS gateways or have rate limiting like Twitter.
* APIs where it may be difficult to non-manually determine if it was called correctly.
* APIs which require special hardware or complex software to run.
* APIs where failure scenarios may be difficult or even impossible to reproduce.

If your app needs to talk to an API like this, you can mimic the effect of calling
APIs like this in your test scenarios by starting a :doc:`/glossary/mock_service` and
using hitch to listen to it.

This can help you maintain a high level of :doc:`/glossary/test_realism` and
loose :doc:`/glossary/coupling` in your tests while avoiding the expense
and inconvenience of calling the real API.


Creating your mock service
--------------------------

Your mock service can be written in any language but it must do two things.

Firstly it should print a line when it has fully started and is ready to receive
API calls. E.g.::

    READY

Secondly, it should print individual lines of valid JSON when it receives an API call.
These JSON line should contain all of the data you want to check in your test. If your
mock service is doing something like this it's good to go::

    READY
    {"sent_from": "webmaster@localhost", "header_to": "django@reinhardt.com", "sent_to": ["django@reinhardt.com"], "subject": "[127.0.0.1:18080] Confirm E-mail Address", "header_from_name": null, "multipart": false, "contenttype": "text/plain", "links": ["http://127.0.0.1:18080/accounts/confirm-email/shnqwlss2mwxjfbjszqcyt2bgpydgmrjatjjnuftxzpuykifca2xwrlig2po6o0g/"], "payload": "User django at 127.0.0.1:18080 has given this as an email address.\n\nTo confirm this is correct, go to http://127.0.0.1:18080/accounts/confirm-email/shnqwlss2mwxjfbjszqcyt2bgpydgmrjatjjnuftxzpuykifca2xwrlig2po6o0g/", "header_to_name": null, "header_to_email": null, "header_from_email": null, "header_from": "webmaster@localhost", "date": "Fri, 23 Oct 2015 00:44:47 -0000"}
    {"sent_from": "noreply@localhost", "header_to": "<django@reinhardt.com>", "sent_to": ["django@reinhardt.com"], "subject": "Reminder", "header_from_name": null, "multipart": false, "contenttype": "text/plain", "links": [], "payload": "Remind me about upcoming gig.", "header_to_name": "", "header_to_email": "django@reinhardt.com", "header_from_email": null, "header_from": "noreply@localhost", "date": "Sun, 22 Nov 2015 08:44:49 -0000"}


Running your mock service with Hitch
------------------------------------

Once your mock service is printing valid lines of JSON when it receives API calls, you will
want to run it as part of your tests. To do this, you must add a service definition in the
:doc:`/glossary/execution_engine` like so:

.. code-block:: python

    # Should go at the top of the engine file
    import hitchserve

    # Should go between "self.services = ServiceBundle(...)" and "self.services.startup(...)":
    self.services['MyMockAPI'] = hitchserve.Service(
        command=["command", "arg1", "arg2", "-x", "option1value", "--option2=option2value" ],
        log_line_ready_checker=lambda line: line == "READY",
        no_libfaketime=True,
    )

.. note::

    You should ensure that your mock service runs *unbuffered*.
    If it is a python application this means starting it with the -u switch.

For additional documentation on running mock services
(e.g. to run the command in a specific directory), see :doc:`/api/generic_service_api`.


Manually checking the output of your mock service during a test run
-------------------------------------------------------------------

Once your mock service is up and running during your test and your application has
called it, you can check its logs manually to verify that it received the API
call and logged a message::

    In [1]: self.services['MyMockAPI'].logs
    Out[1]:
    [          MyMockAPI] READY
    [          MyMockAPI] {"subject": "[127.0.0.1:18080] Confirm E-mail Address", "links": ["http://127.0.0.1:18080/accounts/confirm-email/dwu83kr92t96ek7hkfwjsu4nj6et7i4fu6ntjsn6xues1meeflewmpvoh2vihf33/"], "header_to_name": null, "multipart": false, "sent_from": "webmaster@localhost", "header_to": "django@reinhardt.com", "header_to_email": null, "header_from_name": null, "date": "Fri, 23 Oct 2015 01:15:11 -0000", "header_from": "webmaster@localhost", "contenttype": "text/plain", "payload": "User django at 127.0.0.1:18080 has given this as an email address.\n\nTo confirm this is correct, go to http://127.0.0.1:18080/accounts/confirm-email/dwu83kr92t96ek7hkfwjsu4nj6et7i4fu6ntjsn6xues1meeflewmpvoh2vihf33/", "sent_to": ["django@reinhardt.com"], "header_from_email": null}
    [          MyMockAPI] {"subject": "Reminder", "links": [], "header_to_name": "", "multipart": false, "sent_from": "noreply@localhost", "header_to": "<django@reinhardt.com>", "header_to_email": "django@reinhardt.com", "header_from_name": null, "date": "Sun, 22 Nov 2015 09:15:13 -0000", "header_from": "noreply@localhost", "contenttype": "text/plain", "payload": "Remind me about upcoming gig.", "sent_to": ["django@reinhardt.com"], "header_from_email": null}

To get a python list of dicts representation of only the valid JSON lines, you can just
add .json() to the end::

    In [2]: self.services['MyMockAPI'].logs.json()
    Out[2]:
    [{'contenttype': 'text/plain',
      'date': 'Fri, 23 Oct 2015 01:15:11 -0000',
      'header_from': 'webmaster@localhost',
      'header_from_email': None,
      'header_from_name': None,
      'header_to': 'django@reinhardt.com',
      'header_to_email': None,
      'header_to_name': None,
      'links': ['http://127.0.0.1:18080/accounts/confirm-email/dwu83kr92t96ek7hkfwjsu4nj6et7i4fu6ntjsn6xues1meeflewmpvoh2vihf33/'],
      'multipart': False,
      'payload': 'User django at 127.0.0.1:18080 has given this as an email address.\n\nTo confirm this is correct, go to http://127.0.0.1:18080/accounts/confirm-email/dwu83kr92t96ek7hkfwjsu4nj6et7i4fu6ntjsn6xues1meeflewmpvoh2vihf33/',
      'sent_from': 'webmaster@localhost',
      'sent_to': ['django@reinhardt.com'],
      'subject': '[127.0.0.1:18080] Confirm E-mail Address'}]

.. note::

    If .logs shows your JSON but .logs.json() is empty, check that your mock service is printing *valid* lines of JSON.

You can treat this list of dicts like you would any others in python::

    In [2]: self.services['MyMockAPI'].logs.json()[-1]
    Out[2]: [ Returns a dict representation of the last JSON line printed to the console by MyMockAPI ]

    In [3]: self.services['MyMockAPI'].logs.json()[-1]['contenttype']
    Out[3]: 'text/plain'

    In [4]: self.services['MyMockAPI'].logs.json()[-1]['links'][0]
    Out[4]: 'http://127.0.0.1:18080/accounts/confirm-email/dwu83kr92t96ek7hkfwjsu4nj6et7i4fu6ntjsn6xues1meeflewmpvoh2vihf33/'


Automatically checking the output of your mock service during a test run
------------------------------------------------------------------------

Once you've verified that your mock service is running well with your test and printing
the correct output, you will want to write a step in your test which waits for the API
to be called after another step (e.g. a click) which triggers it to be called::

    - Click: send-sms
    - Wait for SMS:
        Containing: Thank you

To do this you must create a step in your engine which listens to the logs:

.. code-block:: python

    def wait_for_sms(self, containing=None):
        """Wait for an SMS arrive containing the text 'containing'."""
        self.services['MyMockAPI'].logs.out.tail.until_json(
            lambda apicall: containing in apicall['smstext'],
            timeout=45,
            lines_back=1,
        )

When this step is reached, it will check the logs to see if the API call
has already been made and, if not, it will wait for up to 45 seconds.

As soon as the API call is made, it will continue on to the next step.

If an API call containing the text "Thank you" in 'smstext' is never made
against the mock service, it will throw an exception, causing the test to fail.

See also:

* :doc:`/api/engine_api`
* :doc:`/api/generic_service_api`
* :doc:`/plugins/hitchsmtp`
* `Python list documentation <https://docs.python.org/3/tutorial/introduction.html#lists>`_
* `Python dict documentation <https://docs.python.org/3/tutorial/datastructures.html#dictionaries>`_
* `Python lambdas <https://docs.python.org/3/tutorial/controlflow.html#lambda-expressions>`_

.. note::

    Was there anything that went wrong or was confusing while following this tutorial? Please tell us! Help with :doc:`/misc/clarifying_documentation`.


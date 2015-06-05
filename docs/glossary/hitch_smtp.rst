HitchSMTP
=========

`HitchSMTP <https://github.com/hitchtest/hitchsmtp>`_ is a very basic
mock SMTP server.

Every SMTP message sent to this server is logged as JSON to stdout, where it
can be parsed by the harness to verify that it was sent correctly.

It can also mock failure scenarios (e.g. rejected email) by sending to
specific email addresses.

It is a separate application that does not have to be used with Saddle
exclusively.

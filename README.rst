Inbox.py: SMTP Server for Humans
================================

This is simplest SMTP server you'll ever see.

And it's extremely fast. One instance easily handles 1000 emails/second.


Usage
-----

Give your app an inbox easily::

    from inbox import Inbox

    inbox = Inbox()

    @inbox.collate
    def handle(to, sender, body)
        ...

    # Bind directly.
    inbox.serve(address='0.0.0.0', port=4467)

    # Argument parser.
    # inbox.dispatch()


Powered By
----------

- Gevent
- Good Intentions
Inbox.py: SMTP Server for Humans
================================

This project strives to be the simplest SMTP application possible.


Usage
-----

Handle incoming emails::

    from inbox import Inbox

    inbox = Inbox()

    @inbox.collate
    def handle(to, from, body)
        ...

    # Bind directly.
    inbox.serve(port=4467)

    # Argument parser.
    # inbox.dispatch()


Powered By
----------

- Ginkgo
- Gevent
- Good Intentions
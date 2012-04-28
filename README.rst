Inbox.py: SMTP Server for Humans
================================

This is simplest SMTP server you'll ever see.

It's quite quick. One instance should handle over one thousand emails per second.


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


Installation
------------

Installing Inbox.py is simple::

    $ pip install inbox
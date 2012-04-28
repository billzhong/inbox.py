# -*- coding: utf-8 -*-

import gevent
from gevent.socket import create_connection
from gevent.coros import Semaphore


from ginkgo import Service



def main():
    import argparse
    parser = argparse.ArgumentParser(description='Open a public Inbox server.')
    parser.add_argument('port', metavar='port', type=int,
                       help='local port to bind')
    parser.add_argument('--name', dest='name', metavar='name',
                       default='email.py',
                       help='name of the tunnel (default: randomly generate)')
    parser.add_argument('--broker', dest='broker', metavar='address',
                       default='localtunnel.com',
                       help='tunnel broker hostname (default: localtunnel.com)')
    args = parser.parse_args()

    client = InboxServer(args.port, args.name, args.broker)
    client.serve_forever()

class InboxServer(Service):

    def __init__(self, local_port, name, broker_address):
        self.local_port = local_port
        # self.ws = WebSocketClient('http://%s/t/%s' % (broker_address, name))
        self.connections = {}
        self._send_lock = Semaphore()

    def do_start(self):
        self.ws.connect()
        self.spawn(self.listen)
        #gevent.spawn(self.visual_heartbeat)

    def visual_heartbeat(self):
        while True:
            print "."
            gevent.sleep(1)

    def listen(self):
        while True:
            msg = self.ws.receive(msg_obj=True)
            if msg is None:
                print "Trying to stop"
                self.stop()
            if msg.is_text:
                # parsed = json.loads(str(msg))
                print str(msg)
            #     conn_id, event = parsed[0:2]
            #     if event == 'open':
            #         self.local_open(conn_id)
            #     elif event == 'closed':
            #         self.local_close(conn_id)
            # elif msg.is_binary:
            #     # conn_id, data = decode_data_packet(msg.data)
            #     self.local_send(conn_id, data)

if __name__ == '__main__':
    main()
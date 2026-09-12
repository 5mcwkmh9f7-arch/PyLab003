# Lab 003 — Peer-to-Peer Chat

## lab_chat.py Function Documentation

---

### get_peer_node

def get_peer_node(username):  # function name is get_peer_node

Parameters:
- username: The name this peer will be identified by on the network. Gets passed to Pyre() to name the node.

This function returns n, the Pyre node object. It creates the node, starts it, and hands it back so we can use it to join groups and communicate.

---

### join_group

def join_group(node, group):  # function name is join_group

Parameters:
- node: The Pyre node object returned by get_peer_node. Needs to already be started.
- group: A string with the name of the chat group to join.

This function does not return anything. It calls node.join(group) to subscribe the node to that group, then prints a confirmation message.

---

### chat_task

def chat_task(ctx, pipe, n, group):  # function name is chat_task

Parameters:
- ctx: A ZeroMQ Context — manages the sockets and connections.
- pipe: A ZeroMQ pipe/socket used to receive messages from our own app (what we type).
- n: The Pyre node object — used to receive messages from other peers on the network.
- group: The name of the chat group we joined — used to filter incoming messages and to shout our outgoing ones.

This function does not return anything. It is the main send/receive loop. It listens on both the pipe (our messages) and the node socket (other peers messages). When it gets a message from the pipe, it shouts it to the group. When it gets a message from the network, it figures out the type (SHOUT, ENTER, JOIN) and prints the right thing. It stops when it receives $$STOP.

---

### get_channel

def get_channel(node, group):  # function name is get_channel

Parameters:
- node: The Pyre node object, already started and joined to a group.
- group: The group name string, passed along to chat_task so it knows which group to watch.

Returns a ZeroMQ socket (the pipe end of a forked thread). This is the channel we use to send messages — anything we write to it gets picked up by chat_task and broadcast to the group. The type will show as something like: class zmq.sugar.socket.Socket
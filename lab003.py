#!/usr/bin/env python3

import lab_chat as lc


# Part 1: Core Functions

def get_username():
    username = input("Enter your username: ")
    return username.strip().upper()


def get_group():
    group = input("Enter the chat group name to join: ")
    return group.strip().upper()


def get_message():
    message = input("Enter your message: ")
    return message.strip()


# Part 2 + 3: Combining Everything

def initialize_chat():
    username = get_username()
    group = get_group()
    node = lc.get_peer_node(username)
    lc.join_group(node, group)
    channel = lc.get_channel(node, group)
    return channel


def start_chat():
    channel = initialize_chat()

    while True:
        try:
            msg = get_message()
            channel.send(msg.encode('utf_8'))
        except (KeyboardInterrupt, SystemExit):
            break
    channel.send("$$STOP".encode('utf_8'))
    print("FINISHED")


# Entry point
if __name__ == "__main__":
    start_chat()
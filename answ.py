#!/usr/bin/env python

import os
from Bard import Chatbot

chatbot = Chatbot(os.environ.get("BARD_TOKEN"))

def get_answer(message: str) -> str:
    """
    Get a response from a chatbot for a given message.

    Args:
        message (str): The message to send to the chatbot.

    Returns:
        str: The response from the chatbot.
    """
    response = chatbot.ask(message)
    return response["content"]


if __name__ == "__main__":
    msg = input("Enter your message: ")
    ana = get_answer(msg)
    print(ana)
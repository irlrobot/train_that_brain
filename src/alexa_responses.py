#!/usr/bin/env python
"""
Train That Brain
v1.0.0
github.com/irlrobot/train_that_brain
"""
from __future__ import print_function
from random import randint

def speech(tts, attributes, should_end_session, answered_correctly):
    '''build speech output'''
    print("======speech fired...")
    sound = get_sound_effect_for_answer(answered_correctly)
    response = {
        "version": "1.0",
        "sessionAttributes": attributes,
        "response": {
            "shouldEndSession": should_end_session,
            "outputSpeech": {
                "type": "SSML",
                "ssml": "<speak>" + sound + tts + "</speak>"
            },
            "reprompt": {
                "outputSpeech": {
                    "type": "PlainText",
                    "text": "Time's up!  What's your guess?"
                }
            }
        }
    }
    print("=====response back to alexa service:  \n" + str(response))
    return response

def speech_with_card(tts, attributes, should_end_session, card_title,
                     card_text, answered_correctly):
    '''build speech output with a card'''
    print("======speech_with_card fired...")
    sound = get_sound_effect_for_answer(answered_correctly)
    response = {
        "version": "1.0",
        "sessionAttributes": attributes,
        "response": {
            "shouldEndSession": should_end_session,
            "outputSpeech": {
                "type": "SSML",
                "ssml": "<speak>" + sound + tts + "</speak>"
            },
            "card": {
                "type": "Standard",
                "title": card_title,
                "text": card_text,
                "image": {
                    "smallImageUrl":
                        "https://s3.amazonaws.com/trainthatbrain/card_small.png",
                    "largeImageUrl":
                        "https://s3.amazonaws.com/trainthatbrain/card_large.png"
                }
            },
            "reprompt": {
                "outputSpeech": {
                    "type": "PlainText",
                    "text": "Time's up!  What's your guess?"
                }
            }
        }
    }

    print("=====response back to alexa service:  \n" + str(response))
    return response

def play_end_message():
    """play a standard message when exiting the skill"""
    print("=====play_end_message fired...")
    standard_message = "Thanks for playing Train That Brain.  Play daily to keep "\
        "your mind muscles strong."
    review_message = "Please leave a review and let us know what you thought "\
        "of Train My Brain."

    # don't always ask for a review
    if randint(1, 3) == 1:
        tts = standard_message + " " + review_message
    else:
        tts = standard_message

    return speech(tts, {}, True, None)

def get_sound_effect_for_answer(answer_was_right):
    """get the appropriate sound effect"""
    print("=====get_sound_effect_for_answer fired...")
    print("=====answer_was_right:  " + str(answer_was_right))
    if answer_was_right is None:
        return ""
    if answer_was_right:
        return "<audio src=\"https://s3.amazonaws.com/trainthatbrain/correct.mp3\" />"

    return "<audio src=\"https://s3.amazonaws.com/trainthatbrain/wrong.mp3\" />"

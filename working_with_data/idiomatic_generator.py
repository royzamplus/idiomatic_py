#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Prefer a generator expression to a list comprehension for simple iteration
for uppercase_name in (name.upper() for name in get_all_usernames()):
    process_normalized_username(uppercase_name)

# Use a generator to lazily load infinite sequences

def get_twitter_stream_for_keyword(keyword):
    """Now, 'get_twitter_stream_for_keyword' is a generator
    and will continue to generate Iterable pieces of data
    one at a time until 'can_get_stream_data(user)' is
    False (which may be never).

    """

    imaginary_twitter_api = ImaginaryTwitterAPI()
    while imaginary_twitter_api.can_get_stream_data(keyword):
        yield imaginary_twitter_api.get_stream(keyword)

# Because it's a generator, I can sit in this loop until
# the client wants to break out
for tweet in get_twitter_stream_for_keyword('#jeffknupp'):
    if got_stop_signal:
        break
    process_tweet(tweet)

def get_list_of_incredibly_complex_calculation_results(data):
    """A simple example to be sure, but now when the client
    code iterates over the call to
    'get list of incredibly complex calculation results',
    we only do as much work as necessary to generate the
    current item.

    """
    yield first_incredibly_long_calculation(data)
    yield second_incredibly_long_calculation(data)
    yield third_incredibly_long_calculation(data)


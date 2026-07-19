#!/usr/bin/python
# -*- coding: utf-8 -*-
import uuid

class Review:
    def __init__(self, consumer_name, rating, feedback_message):
        self.review_id = str(uuid.uuid4())
        self.consumer_name = consumer_name
        self.rating = rating
        self.feedback_message = feedback_message

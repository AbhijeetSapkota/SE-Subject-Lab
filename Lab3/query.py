#!/usr/bin/python
# -*- coding: utf-8 -*-
import uuid

class Query:
    def __init__(self, consumer_name, question):
        self.query_id = str(uuid.uuid4())
        self.consumer_name = consumer_name
        self.question = question
        self.answer = None
        self.status = "Pending"

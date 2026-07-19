#!/usr/bin/python
# -*- coding: utf-8 -*-
import uuid
import datetime

class TabEntry:
    def __init__(self, entry_type, amount):
        self.entry_id = str(uuid.uuid4())
        self.entry_type = entry_type # 'Credit' or 'Debit'
        self.amount = amount
        self.date = datetime.datetime.now().isoformat()

#!/usr/bin/python
# -*- coding: utf-8 -*-
import uuid

class Tab:
    def __init__(self, retailer_id, consumer_id):
        self.tab_id = str(uuid.uuid4())
        self.retailer_id = retailer_id
        self.consumer_id = consumer_id
        self.status = "Pending"
        self.total_balance = 0.0
        self.entries = []

    def add_entry(self, entry):
        self.entries.append(entry)
        if entry.entry_type == "Credit":
            self.total_balance += entry.amount
        elif entry.entry_type == "Debit":
            self.total_balance -= entry.amount

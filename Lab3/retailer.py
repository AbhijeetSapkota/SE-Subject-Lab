#!/usr/bin/python
# -*- coding: utf-8 -*-

from user import User
from inventory import Inventory

class Retailer(User):
    def __init__(self, username, password, personal_info, contact_info, shop_name, shop_location):
        super().__init__(username, password, personal_info, contact_info)
        self.shop_name = shop_name
        self.shop_location = shop_location
        self.inventory = Inventory(f"INV_{username}")
        self.reviews = []
        self.queries = []
        self.tabs = []

    def viewListing(self):
        return self.inventory.getItems()

    def viewFeedback(self):
        return self.reviews

    def answerQuery(self, query_id, answer):
        for q in self.queries:
            if q.query_id == query_id:
                q.answer = answer
                q.status = "Answered"
                return True
        return False

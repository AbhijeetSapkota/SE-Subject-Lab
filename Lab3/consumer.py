#!/usr/bin/python
# -*- coding: utf-8 -*-

from user import User

class Consumer(User):
    def __init__(self, username, password, personal_info, contact_info, gps_location=None):
        super().__init__(username, password, personal_info, contact_info)
        self.gps_location = gps_location
        self.tabs = []

    def trackLocation(self, location):
        self.gps_location = location

    def searchItems(self, keyword, all_retailers):
        results = []
        for retailer in all_retailers:
            if hasattr(retailer, 'inventory'):
                for item in retailer.inventory.getItems():
                    if keyword.lower() in item.name.lower():
                        results.append({"retailer": retailer, "item": item})
        return results

    def rateRetailer(self, retailer, rating):
        pass

    def writeReview(self, retailer, text):
        pass

    def acceptTab(self, tab):
        tab.status = "Accepted"
        self.tabs.append(tab)

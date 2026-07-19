#!/usr/bin/python
# -*- coding: utf-8 -*-

class User:
    def __init__(self, username, password, personal_info, contact_info):
        self.username = username
        self.password = password
        self.personal_info = personal_info
        self.contact_info = contact_info

    def register(self):
        # Simulation of saving user to a db
        return True

    def login(self, entered_password):
        return self.password == entered_password

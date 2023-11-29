#!/usr/bin/env python3

APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]

class Person:
    def __init__(self, name, job=""):
        if not (isinstance(name, str) and 1 <= len(name) <= 25):
            print("Name must be a string between 1 and 25 characters.")
            return
        if job and job not in ["Engineer", "Doctor", "ITC"]:
            print("Job must be in the list of approved jobs.")
            return

        self.name = name
        self.job = job

    def talk(self):
        print("Hello World!")

    def walk(self):
        print("The person is walking.")

    pass

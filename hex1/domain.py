from typing import NamedTuple


class IssueReporter:
    name: str
    email: str

    def init(self, name, email):
        self.name = name
        self.email = email


class Issue:
    description: str
    reporter: str

    def init(self, reporter, description):
        self.description = description
        self.reporter = reporter


class IssueLog:
    def add(self, issue):
        pass


class ReportIssueCommand(NamedTuple):
    reporter_name: str
    reporter_email: str
    problem_description: str

    def init(self, reporter_name, reporter_email, problem_description):
        self.reporter_name = reporter_name
        self.reporter_email = reporter_email
        self.problem_description = problem_description

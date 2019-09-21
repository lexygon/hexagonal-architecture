from .domain import ReportIssueCommand, IssueLog
from .service import ReportIssueHandler


class FakeIssueLog(IssueLog):

    def __init__(self):
        self.issues = []

    def add(self, issue):
        self.issues.append(issue)

    def get(self, id):
        return self.issues[id]

    def __len__(self):
        return len(self.issues)

    def __getitem__(self, idx):
        return self.issues[idx]


email = "bob@example.org"
name = "bob"
desc = "My mouse won’t move"


class WhenReportingAnIssue:
    issues: FakeIssueLog

    def given_an_empty_issue_log(self):
        self.issues = FakeIssueLog()

    def because_we_report_a_new_issue(self):
        handler = ReportIssueHandler(self.issues)
        cmd = ReportIssueCommand(name, email, desc)

        handler(cmd)

    def the_handler_should_have_created_a_new_issue(self):
        expect(self.issues).to(have_len(1))

    def it_should_have_recorded_the_issuer(self):
        expect(self.issues[0].reporter.name).to(equal(name))
        expect(self.issues[0].reporter.email).to(equal(email))

    def it_should_have_recorded_the_description(self):
        expect(self.issues[0].description).to(equal(desc))

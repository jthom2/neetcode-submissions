class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        s = set()

        for email in emails:
            u = "".join((email[:email.index('@')].split('+')[0]).split('.')) + email[email.index('@'):]
            s.add(u)
 
        return len(s)
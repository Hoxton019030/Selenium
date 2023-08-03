class JobDetail:
    def __init__(self, title: str, companyName: str, href: str, tags: str, jobInfo: str, address: str,
                 experience: str):
        self.title = title
        self.companyName = companyName
        self.href = href
        self.tags = tags
        self.jobInfo = jobInfo
        self.address = address
        self.experience = experience

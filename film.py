class Film:
    def __init__(self, title, year, expire_date):
        self.title = title
        self.year = year
        self.expire_date = expire_date

    def __str__(self):
        if self.year:
            return f"{self.title} ({self.year})"
        else:
            return f"{self.title}"

    def to_dict(self):
        return {
            "title": self.title,
            "year": self.year,
            "expireDate": self.expire_date
        }
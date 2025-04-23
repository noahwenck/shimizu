class Film:
    def __init__(self, title, year, expire_date, streaming_service):
        self.title = title
        self.year = year
        self.expire_date = expire_date
        self.streaming_service = streaming_service

    def __str__(self):
        if self.year:
            return f"{self.title} ({self.year})"
        else:
            return f"{self.title}"

    def to_dict(self):
        return {
            "title": self.title,
            "year": self.year,
            "expireDate": self.expire_date,
            "streamingService": self.streaming_service
        }
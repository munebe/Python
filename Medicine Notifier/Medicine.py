from datetime import datetime


class Medicine:
    def __init__(self, title, content, period, end_date):
        self.title = title
        self.content = content
        self.period = period
        self.end_date = end_date

    @property
    def getTitle(self):
        return self.title

    @property
    def getContent(self):
        return self.content

    @property
    def getPeriod(self):
        return self.period

    @property
    def getEndDate(self):
        return datetime.strptime(self.end_date, "%d/%m/%y")

    def isOutOfTime(self):
        return self.getEndDate <= datetime.today()


medicine = {
    "MAQUIDRY": {
        "title": "MAQUIDRY",
        "content": "MAQUIDRY adlı ilacın zamanı geldi",
        "period": ["19:00"],
        "end_date": "08/01/23",
    },
    "ROHTO": {
        "title": "ROHTO",
        "content": "ROHTO adlı ilacın zamanı geldi",
        "period": ["07:00", "10:30", "14:00", "17:30", "21:00", "00:30"],
        "end_date": "06/04/23",
    },
    "MOXiDEXA": {
        "title": "MOXiDEXA",
        "content": "MOXiDEXA adlı ilacın zamanı geldi",
        "period": ["07:01", "13:00", "19:00", "01:00"],
        "end_date": "20/01/23",
    },
}

moxidexa = Medicine(
    medicine["ROHTO"]["title"],
    medicine["ROHTO"]["content"],
    medicine["ROHTO"]["period"],
    medicine["ROHTO"]["end_date"],
)

rohta = Medicine(
    medicine["MOXiDEXA"]["title"],
    medicine["MOXiDEXA"]["content"],
    medicine["MOXiDEXA"]["period"],
    medicine["MOXiDEXA"]["end_date"],
)

maquidry = Medicine(
    medicine["MAQUIDRY"]["title"],
    medicine["MAQUIDRY"]["content"],
    medicine["MAQUIDRY"]["period"],
    medicine["MAQUIDRY"]["end_date"],
)

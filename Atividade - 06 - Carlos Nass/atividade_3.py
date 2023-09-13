import re

class WorkHoursCalculator:

    def __init__(self):
        self.timeout = 0

    def WorkHours(self, i):
        hours = 0
        for i in i:
            entryHour, exitHour = i
            if self.ValidateFormat(entryHour) and self.ValidateFormat(exitHour):
                hours += self.HoursDifference(entryHour, exitHour)
            else:
                raise ValueError("Formato de hora inválido")
        return hours - self.timeout
    
    def InsertTimeout(self, timeoutTime):
        if self.validateTimeoutFormat(timeoutTime):
            self.timeout = self.parseTimeout(timeoutTime)
        else:
            raise ValueError("Formato de duração de intervalo inválido")

    def HoursDifference(self, entryHour, exitHour):
        entryHour = self.parseHour(entryHour)
        exitHour = self.parseHour(exitHour)
        return exitHour - entryHour

    def parseHour(self, hour):
        hours, minutes = map(int, hour.split(':'))
        return hours + minutes / 60.0

    def ValidateFormat(self, hour):
        formatHour = re.compile(r'^(?:[01]\d|2[0-3]):[0-5]\d$')
        return formatHour.match(hour) is not None

    def validateTimeoutFormat(self, timeoutTime):
        formatTimeout = re.compile(r'^\d{2}-\d{3}$')
        return formatTimeout.match(timeoutTime) is not None

    def parseTimeout(self, timeoutTime):
        hours, minutes = map(int, timeoutTime.split('-'))
        return hours + minutes / 60.0

    def InvertTime(self, entry):
        return [(exit, entry) for entry, exit in entry]

import re

class WorkHoursCalculator:

    def WorkHours(self, i):
        hours = 0
        for i in i:
            entryHour, exitHour = i
            if self.ValidateFormat(entryHour) and self.ValidateFormat(exitHour):
                hours += self.HoursDifference(entryHour, exitHour)
            else:
                raise ValueError("Formato de hora inválido")
        return hours

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

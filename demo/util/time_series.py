import datetime


class TimeSeries():
    def makeTimeSeriesName(self):
        return str(int(datetime.datetime.now().timestamp()))

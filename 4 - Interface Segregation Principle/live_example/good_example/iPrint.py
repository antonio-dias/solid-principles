import abc


class IPrint(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def print(self):
        return

    @abc.abstractmethod
    def getPrintSpoolDetails(self):
        return
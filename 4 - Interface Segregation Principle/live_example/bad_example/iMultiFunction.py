import abc

class IMultiFunction(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def print(self):
        return

    @abc.abstractmethod
    def getPrintSpoolDetails(self):
        return

    @abc.abstractmethod
    def scan(self):
        return

    @abc.abstractmethod
    def scanPhoto(self):
        return

    @abc.abstractmethod
    def fax(self):
        return

    @abc.abstractmethod
    def internetFax(self):
        return

import abc


class IFax(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def fax(self):
        return

    @abc.abstractmethod
    def internetFax(self):
        return

import abc


class IScan(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def scan(self):
        return

    @abc.abstractmethod
    def scanPhoto(self):
        return
from abc import ABCMeta, abstractmethod


class FamilyInterface(metaclass=ABCMeta):
    @property
    @abstractmethod
    def family_name(self) -> str:
        raise NotImplementedError()


class FamilyMemberInterface(metaclass=ABCMeta):
    # comment me out below, then slots in the derived class will fail
    __slots__ = []
    @abstractmethod
    def family_name(self) -> str:
        raise NotImplementedError()

    @property
    @abstractmethod
    def first_name(self) -> str:
        raise NotImplementedError()


    @property
    @abstractmethod
    def middle_name(self) -> str:
        raise NotImplementedError()



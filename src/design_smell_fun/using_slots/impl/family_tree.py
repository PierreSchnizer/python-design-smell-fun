from  ..interface.family_tree import FamilyMemberInterface


class FamilyMember(FamilyMemberInterface):
    __slots__ = ["_fam_name", "_first_name", "_mid_name"]
    def __init__(
            self,
            *,
            family_name: str,
            mid_name : str,
            first_name: str
    ):
        self._fam_name = family_name
        self._mid_name = mid_name
        self._first_name = first_name

    @property
    def family_name(self) -> str:
        return self._fam_name

    @property
    def middle_name(self) -> str:
        return self._mid_name

    @property
    def first_name(self) -> str:
        return self._first_name

    def __repr__(self):
        return f"{self.__class__.__name__}(family_name={self.family_name}, middle_name={self.middle_name}, first_name={self.first_name})"
from strenum import StrEnum

class Collection(StrEnum):
    CONVERSATIONS: str = "Conversations"
    USERS: str = "Users"    

    def __str__(self):
        return self.value

    def __repr__(self):
        return self.value


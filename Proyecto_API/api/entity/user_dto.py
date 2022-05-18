from dataclasses import dataclass
from typing import Tuple


@dataclass
class UserDTO:
    user_uuid:str
    user_name:str
    user_password:str
    user_email:str
    user_direction:str
    user_cellphone:str
    user_role:int
    
    def to_tuples(self) -> Tuple:
        return (
            self.user_uuid, self.user_name, 
            self.user_password, self.user_email, 
            self.user_direction, self.user_cellphone, self.user_role
        )
    
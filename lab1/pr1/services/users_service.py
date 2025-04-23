from models.schemas import Account
from data import temp_db


def get_all_users() -> list[Account]:
    return [Account.model_validate(user) for user in temp_db]


def get_user_by_id(user_id: int) -> Account | None:
    for user in temp_db:
        if user["id"] == user_id:
            return Account.model_validate(user)
    return None


def create_user(user: Account) -> Account:
    temp_db.append(user.model_dump())
    return user


def update_user(user_id: int, updated_user: Account) -> Account | None:
    for index, user in enumerate(temp_db):
        if user["id"] == user_id:
            temp_db[index] = updated_user.model_dump()
            return updated_user
    return None


def delete_user(user_id: int) -> Account | None:
    for index, user in enumerate(temp_db):
        if user["id"] == user_id:
            return Account.model_validate(temp_db.pop(index))
    return None

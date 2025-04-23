from sqlmodel import Session, select
from models.models import Account


def get_all_users(session: Session) -> list[Account]:
    statement = select(Account)
    results = session.exec(statement).all()
    return results


def get_user_by_id(session: Session, user_id: int) -> Account | None:
    statement = select(Account).where(Account.id == user_id)
    result = session.exec(statement).first()
    if not result:
        return None
    return result


def create_user(session: Session, user: Account) -> Account:
    session.add(user)
    session.commit()
    session.refresh(user)
    return user


def update_user(session: Session, user_id: int, user: Account) -> Account | None:
    existing_user = get_user_by_id(session, user_id)
    if not existing_user:
        return None
    for key, value in user.dict(exclude_unset=True).items():
        setattr(existing_user, key, value)
    session.commit()
    session.refresh(existing_user)
    return existing_user


def delete_user(session: Session, user_id: int) -> bool:
    existing_user = get_user_by_id(session, user_id)
    if not existing_user:
        return False
    session.delete(existing_user)
    session.commit()
    return True

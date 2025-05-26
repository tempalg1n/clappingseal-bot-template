"""User repository file."""

from sqlalchemy.ext.asyncio import AsyncSession

from src.db.models.user import Role

from ..models import User
from .abstract import Repository


class UserRepo(Repository[User]):
    """User repository for CRUD and other SQL queries."""

    def __init__(self, session: AsyncSession):
        """Initialize user repository as for all users or only for one user."""
        super().__init__(type_model=User, session=session)

    async def new(
            self,
            user_id: int,
            user_name: str | None = None,
            first_name: str | None = None,
            second_name: str | None = None,
            role: Role | None = Role.USER,
    ) -> User:
        new_user = await self.session.merge(
            User(
                user_id=user_id,
                user_name=user_name,
                first_name=first_name,
                second_name=second_name,
                role=role,
            )
        )
        return new_user

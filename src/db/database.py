"""Database class with all-in-one features."""

from sqlalchemy.ext.asyncio import (AsyncSession, async_sessionmaker,
                                    create_async_engine)

from src.configuration import PostgresConfig
from src.db.repositories.user import UserRepo


def new_session_maker(
        psql_config: PostgresConfig,
) -> async_sessionmaker[AsyncSession]:
    database_uri = psql_config.build_connection_str()

    engine = create_async_engine(
        database_uri,
        pool_size=50,
        max_overflow=15,
    )
    return async_sessionmaker(
        engine, class_=AsyncSession, autoflush=False, expire_on_commit=False
    )


class Database:
    """Database class.

    is the highest abstraction level of database and
    can be used in the handlers or any others bot-side functions.
    """

    def __init__(
            self,
            session: AsyncSession,
    ):
        """Initialize Database class.

        :param session: AsyncSession to use
        """
        self.session = session
        self.user = UserRepo(session=session)

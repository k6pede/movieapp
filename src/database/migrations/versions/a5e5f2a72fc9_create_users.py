"""create_users

Revision ID: a5e5f2a72fc9
Revises: 
Create Date: 2024-06-19 15:34:39.059068

"""

from typing import Sequence, Union

from alembic import op  # type: ignore
import sqlalchemy as sa  # type: ignore


# revision identifiers, used by Alembic.
revision: str = "a5e5f2a72fc9"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass

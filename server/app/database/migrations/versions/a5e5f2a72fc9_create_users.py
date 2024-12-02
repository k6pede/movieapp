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
    op.create_table(
        "users",
        sa.Column("id", sa.String(36), primary_key=True),
        sa.Column("name", sa.String(255), nullable=False),
        sa.Column("email", sa.String(255), index=True, unique=True),
        sa.Column("is_active", sa.Boolean, default=True),
        sa.Column(
            "created_at",
            sa.Datetime(timezone=True),
            nullable=False,
            default=sa.func.now(),
            onupdate=sa.func.now(),
        ),
        sa.Column(
            "updated_at",
            sa.Datetime(timezone=True),
            nullable=False,
            default=sa.func.now(),
            onupdate=sa.func.now(),
        ),
        sa.Column("deleted_at", sa.Datetime(timezone=True), nullable=True),
    )


def downgrade() -> None:
    op.drop_table("users")

"""Create users table

Revision ID: 37a458cb0668
Revises: 
Create Date: 2022-12-23 12:49:17.316034

"""
import datetime

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '37a458cb0668'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "users",
        sa.Column("id", sa.String(), nullable=False),
        sa.Column("full_name", sa.String(), nullable=True),
        sa.Column("email", sa.String(), nullable=False),
        sa.Column("hashed_password", sa.String(), nullable=False),
        sa.Column("is_active", sa.Boolean(), default=True, nullable=False),
        sa.Column("is_superuser", sa.Boolean(), default=False, nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), default=datetime.datetime.utcnow(), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), default=datetime.datetime.utcnow(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("users_email_idx"), "users", ["email"], unique=True)


def downgrade() -> None:
    op.drop_index(op.f("users_email_idx"), table_name="users")
    op.drop_table("users")

"""Create loans table

Revision ID: 0fb86a325cac
Revises: 37a458cb0668
Create Date: 2022-12-27 18:47:04.955741

"""
import datetime

import sqlalchemy as sa
from alembic import op

from app.models import ScheduleStatus

# revision identifiers, used by Alembic.
revision = '0fb86a325cac'
down_revision = '37a458cb0668'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # Create loans
    op.create_table(
        "loans",
        sa.Column("id", sa.String(), nullable=False),
        sa.Column("user_id", sa.String(), nullable=False),
        sa.Column("title", sa.String(), nullable=False),
        sa.Column("amount_cents", sa.BigInteger(), default=0, nullable=False),
        sa.Column("annual_interest_rate", sa.DECIMAL(15, 5), default=0, nullable=False),
        sa.Column("currency", sa.String(), default="USD", nullable=False),
        sa.Column("term_months", sa.Integer(), default=0, nullable=False),
        sa.Column("due_monthly_starting", sa.Date(), default=datetime.date.today(), nullable=False),
        sa.Column("is_active", sa.Boolean(), default=True, nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), default=datetime.datetime.utcnow(), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), default=datetime.datetime.utcnow(), nullable=False),
        sa.ForeignKeyConstraint(["user_id"], ["users.id"]),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("loans_user_id_idx"), "loans", ["user_id"], unique=False)

    # Create schedules
    op.create_table(
        "schedules",
        sa.Column("id", sa.String(), nullable=False),
        sa.Column("loan_id", sa.String(), nullable=False),
        sa.Column("month", sa.Integer(), default=1, nullable=False),
        sa.Column("due", sa.Date(), nullable=False),
        sa.Column("amount_cents", sa.BigInteger(), default=0, nullable=False),
        sa.Column("interest_cents", sa.BigInteger, default=0, nullable=False),
        sa.Column("principal_cents", sa.BigInteger, default=0, nullable=False),
        sa.Column("balance_cents", sa.BigInteger(), default=0, nullable=False),
        sa.Column("status", sa.Enum(ScheduleStatus), default=ScheduleStatus.SCHEDULED, nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), default=datetime.datetime.utcnow(), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), default=datetime.datetime.utcnow(), nullable=False),
        sa.ForeignKeyConstraint(["loan_id"], ["loans.id"]),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("schedules_loan_id_idx"), "schedules", ["loan_id"], unique=False)
    op.create_index(op.f("schedules_loan_due_idx"), "schedules", ["due"], unique=False)
    op.create_index(op.f("schedules_loan_status_idx"), "schedules", ["status"], unique=False)


def downgrade() -> None:
    op.drop_index(op.f("schedules_loan_status_idx"), table_name="schedules")
    op.drop_index(op.f("schedules_loan_due_idx"), table_name="schedules")
    op.drop_index(op.f("schedules_loan_id_idx"), table_name="schedules")
    op.drop_table("schedules")

    op.drop_index(op.f("loans_user_id_idx"), table_name="loans")
    op.drop_table("loans")

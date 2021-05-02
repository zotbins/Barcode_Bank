"""create_main_tables
Revision ID: ed184e621ebf
Revises: 
Create Date: 2021-05-01 15:07:06.064324
"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic
revision = "ed184e621ebf"
down_revision = None
branch_labels = None
depends_on = None


def create_barcode_table() -> None:
    op.create_table(
        "barcodes",
        sa.Column("barcode", sa.VARCHAR(13), primary_key=True),
        sa.Column("item", sa.Text),
        sa.Column("bin", sa.VARCHAR(8), nullable=False),
    )


def upgrade() -> None:
    create_barcode_table()


def downgrade() -> None:
    op.drop_table("barcodes")

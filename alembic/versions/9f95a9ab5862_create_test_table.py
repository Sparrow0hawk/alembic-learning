"""create test table

Revision ID: 9f95a9ab5862
Revises: 
Create Date: 2023-06-27 20:19:02.626068

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9f95a9ab5862'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.execute("""
                CREATE TABLE test (
                id serial PRIMARY KEY,
                num integer,
                data text)
            """)
    
    op.execute("INSERT INTO test (num, data) VALUES (100, 'abcdef')")


def downgrade() -> None:
    op.drop_table("test")

"""'newemp'

Revision ID: 4ce9f0a1485a
Revises: 900f84ca2e41
Create Date: 2020-03-13 13:46:48.858450

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4ce9f0a1485a'
down_revision = '900f84ca2e41'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('employee', sa.Column('depart_id', sa.Integer(), nullable=True))
    op.add_column('employee', sa.Column('pwd', sa.String(length=25), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('employee', 'pwd')
    op.drop_column('employee', 'depart_id')
    # ### end Alembic commands ###

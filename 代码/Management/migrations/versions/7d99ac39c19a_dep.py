"""'dep'

Revision ID: 7d99ac39c19a
Revises: 
Create Date: 2020-03-11 19:35:30.937614

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7d99ac39c19a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('department',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('depart_name', sa.String(length=100), nullable=True),
    sa.Column('depart_manager', sa.String(length=100), nullable=True),
    sa.Column('people_num', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('depart_name')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('department')
    # ### end Alembic commands ###

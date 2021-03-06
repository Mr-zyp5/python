"""'notice'

Revision ID: d6c756737ca7
Revises: 4ce9f0a1485a
Create Date: 2020-03-14 11:15:15.169459

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd6c756737ca7'
down_revision = '4ce9f0a1485a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('notice',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=50), nullable=True),
    sa.Column('message', sa.Text(), nullable=True),
    sa.Column('pubtime', sa.DateTime(), nullable=True),
    sa.Column('user_type', sa.String(length=100), nullable=True),
    sa.Column('type_id', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('notice')
    # ### end Alembic commands ###

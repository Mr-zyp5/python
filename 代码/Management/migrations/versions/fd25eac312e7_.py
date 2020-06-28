"""empty message

Revision ID: fd25eac312e7
Revises: 78f141f7ecd6
Create Date: 2020-03-17 20:54:55.536165

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'fd25eac312e7'
down_revision = '78f141f7ecd6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('leave', 'is_agree')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('leave', sa.Column('is_agree', mysql.TINYINT(display_width=1), autoincrement=False, nullable=True))
    # ### end Alembic commands ###

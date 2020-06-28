"""empty message

Revision ID: 51b3977d631f
Revises: 6f917be835af
Create Date: 2020-03-18 15:15:38.387614

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '51b3977d631f'
down_revision = '6f917be835af'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('attendance', 'work_time')
    op.drop_column('attendance', 'lvearly_count')
    op.drop_column('attendance', 'late_count')
    op.drop_column('attendance', 'leave_time')
    op.add_column('sign', sa.Column('status', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('sign', 'status')
    op.add_column('attendance', sa.Column('leave_time', mysql.DATETIME(), nullable=True))
    op.add_column('attendance', sa.Column('late_count', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True))
    op.add_column('attendance', sa.Column('lvearly_count', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True))
    op.add_column('attendance', sa.Column('work_time', mysql.DATETIME(), nullable=True))
    # ### end Alembic commands ###

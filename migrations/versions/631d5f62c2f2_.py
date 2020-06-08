"""empty message

Revision ID: 631d5f62c2f2
Revises: bfa8052d41ec
Create Date: 2020-06-08 15:59:17.555979

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '631d5f62c2f2'
down_revision = 'bfa8052d41ec'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('todos', sa.Column('completed', sa.Boolean(), nullable=True))
    op.execute('UPDATE todos SET completed = False WHERE completed is NULL;')
    op.alter_column('todos', 'completed', nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('todos', 'completed')
    # ### end Alembic commands ###

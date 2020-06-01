"""empty message

Revision ID: 659d979b64ce
Revises: c31cdf879ee3
Create Date: 2020-05-17 12:50:53.360910

"""
import sqlalchemy_utils
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '659d979b64ce'
down_revision = 'c31cdf879ee3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('alias', sa.Column('disable_pgp', sa.Boolean(), server_default='0', nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('alias', 'disable_pgp')
    # ### end Alembic commands ###
"""empty message

Revision ID: 7dc8b511a497
Revises: b4ab069310aa
Create Date: 2022-03-28 20:00:16.050917

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7dc8b511a497'
down_revision = 'b4ab069310aa'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('collection', 'poo')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('collection', sa.Column('poo', sa.BOOLEAN(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
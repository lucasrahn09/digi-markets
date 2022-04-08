"""empty message

Revision ID: 34285d3bcf86
Revises: 2becd6e328b9
Create Date: 2022-03-28 20:12:17.654810

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '34285d3bcf86'
down_revision = '2becd6e328b9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('collection', sa.Column('symbol', sa.String(length=20), nullable=True))
    op.create_foreign_key(None, 'collection', 'blockchain_network', ['network_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'collection', type_='foreignkey')
    op.drop_column('collection', 'symbol')
    # ### end Alembic commands ###
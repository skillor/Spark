"""Added equippable item row

Revision ID: dd529c3f9266
Revises:
Create Date: 2022-04-01 14:43:11.516003

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dd529c3f9266'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('inventory_item_type', sa.Column('equippable', sa.Boolean(), nullable=False, server_default='0'))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('inventory_item_type', 'equippable')
    # ### end Alembic commands ###

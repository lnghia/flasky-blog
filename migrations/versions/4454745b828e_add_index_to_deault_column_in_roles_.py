"""add index to deault column in roles table

Revision ID: 4454745b828e
Revises: b06810a049e9
Create Date: 2020-08-29 22:39:10.450430

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4454745b828e'
down_revision = 'b06810a049e9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index(op.f('ix_roles_default'), 'roles', ['default'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_roles_default'), table_name='roles')
    # ### end Alembic commands ###
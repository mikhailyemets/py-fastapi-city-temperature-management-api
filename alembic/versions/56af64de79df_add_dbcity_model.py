"""Add DBCity Model

Revision ID: 56af64de79df
Revises: e436130da3b8
Create Date: 2024-06-30 12:58:17.802048

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '56af64de79df'
down_revision = 'e436130da3b8'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('city',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('additional_info', sa.String(length=511), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_index(op.f('ix_city_id'), 'city', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_city_id'), table_name='city')
    op.drop_table('city')
    # ### end Alembic commands ###

"""empty message

Revision ID: 00c4220b3219
Revises: a8add54ead8d
Create Date: 2022-01-31 21:28:59.379202

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '00c4220b3219'
down_revision = 'a8add54ead8d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('characters',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=30), nullable=False),
    sa.Column('height', sa.Integer(), nullable=False),
    sa.Column('gender', sa.String(length=30), nullable=False),
    sa.Column('homeworld', sa.String(length=30), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('characters')
    # ### end Alembic commands ###

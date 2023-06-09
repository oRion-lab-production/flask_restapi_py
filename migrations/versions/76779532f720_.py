"""empty message

Revision ID: 76779532f720
Revises: 7e9fe88a7568
Create Date: 2023-01-09 23:46:09.644379

"""
import sqlalchemy_utils
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '76779532f720'
down_revision = '7e9fe88a7568'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('identity_user',
    sa.Column('id', sqlalchemy_utils.types.uuid.UUIDType(binary=False), nullable=False),
    sa.Column('role_id', sqlalchemy_utils.types.uuid.UUIDType(binary=False), nullable=False),
    sa.Column('public_id', sa.String(length=32), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('email', sa.String(length=255), nullable=False),
    sa.Column('password', sa.String(length=255), nullable=False),
    sa.Column('created_by', sa.String(length=255), nullable=True),
    sa.Column('created_datetime', sa.DATETIME(timezone=6), nullable=True),
    sa.Column('modified_by', sa.String(length=255), nullable=True),
    sa.Column('modified_datetime', sa.DATETIME(timezone=6), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('identity_user')
    # ### end Alembic commands ###


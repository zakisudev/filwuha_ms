"""initial table creation

Revision ID: 745f2ac1c1aa
Revises: 
Create Date: 2023-11-18 19:29:21.263588

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '745f2ac1c1aa'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('admins',
    sa.Column('admin_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('username', sa.String(length=64), nullable=False),
    sa.Column('password_hash', sa.String(length=128), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('admin_id'),
    sa.UniqueConstraint('username')
    )
    op.create_table('orders',
    sa.Column('order_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('first_name', sa.String(length=45), nullable=False),
    sa.Column('last_name', sa.String(length=45), nullable=False),
    sa.Column('email', sa.String(length=45), nullable=True),
    sa.Column('phone_number', sa.String(length=45), nullable=False),
    sa.Column('order_date', sa.DateTime(), nullable=False),
    sa.Column('order_time', sa.DateTime(), nullable=False),
    sa.Column('price', sa.Float(), nullable=False),
    sa.Column('payment', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('order_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('orders')
    op.drop_table('admins')
    # ### end Alembic commands ###
"""empty message

Revision ID: 7e3e0ed25dcb
Revises: 
Create Date: 2022-12-01 20:13:33.742305

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7e3e0ed25dcb'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('driver',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('state', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('vehicle',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('make', sa.String(), nullable=True),
    sa.Column('model', sa.String(), nullable=True),
    sa.Column('year', sa.Integer(), nullable=True),
    sa.Column('driver_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['driver_id'], ['driver.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('persons')
    op.drop_table('table1')
    op.drop_table('table2')
    op.drop_table('todos')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('todos',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('description', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='todos_pkey')
    )
    op.create_table('table2',
    sa.Column('id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('completed', sa.BOOLEAN(), server_default=sa.text('false'), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='table2_pkey')
    )
    op.create_table('table1',
    sa.Column('id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('description', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='table1_pkey')
    )
    op.create_table('persons',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='persons_pkey')
    )
    op.drop_table('vehicle')
    op.drop_table('driver')
    # ### end Alembic commands ###

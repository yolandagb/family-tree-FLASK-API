"""empty message

Revision ID: 5732652e160d
Revises: 
Create Date: 2021-05-13 20:30:01.820966

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5732652e160d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('grandparent',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=120), nullable=False),
    sa.Column('lastname', sa.String(length=120), nullable=False),
    sa.Column('age', sa.String(length=120), nullable=False),
    sa.Column('reference', sa.String(length=120), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('age'),
    sa.UniqueConstraint('age'),
    sa.UniqueConstraint('lastname'),
    sa.UniqueConstraint('lastname'),
    sa.UniqueConstraint('name'),
    sa.UniqueConstraint('name'),
    sa.UniqueConstraint('reference'),
    sa.UniqueConstraint('reference')
    )
    op.create_table('parent',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=120), nullable=False),
    sa.Column('lastname', sa.String(length=120), nullable=False),
    sa.Column('age', sa.String(length=120), nullable=False),
    sa.Column('reference', sa.String(length=120), nullable=False),
    sa.Column('parent', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['parent'], ['grandparent.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('age'),
    sa.UniqueConstraint('age'),
    sa.UniqueConstraint('lastname'),
    sa.UniqueConstraint('lastname'),
    sa.UniqueConstraint('name'),
    sa.UniqueConstraint('name'),
    sa.UniqueConstraint('reference'),
    sa.UniqueConstraint('reference')
    )
    op.create_table('current',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=120), nullable=False),
    sa.Column('lastname', sa.String(length=120), nullable=False),
    sa.Column('age', sa.String(length=120), nullable=False),
    sa.Column('reference', sa.String(length=120), nullable=False),
    sa.Column('parent_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['parent_id'], ['parent.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('age'),
    sa.UniqueConstraint('age'),
    sa.UniqueConstraint('lastname'),
    sa.UniqueConstraint('lastname'),
    sa.UniqueConstraint('name'),
    sa.UniqueConstraint('name'),
    sa.UniqueConstraint('reference'),
    sa.UniqueConstraint('reference')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('current')
    op.drop_table('parent')
    op.drop_table('grandparent')
    # ### end Alembic commands ###

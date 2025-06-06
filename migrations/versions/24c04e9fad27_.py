"""empty message

Revision ID: 24c04e9fad27
Revises: d52a217fdda6
Create Date: 2025-04-06 14:21:14.097539

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '24c04e9fad27'
down_revision = 'd52a217fdda6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('episode',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('guest',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('appearance',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('rating', sa.Integer(), nullable=True),
    sa.Column('episode_id', sa.Integer(), nullable=True),
    sa.Column('guest_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['episode_id'], ['episode.id'], ),
    sa.ForeignKeyConstraint(['guest_id'], ['guest.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('guests')
    op.drop_table('episodes')
    op.drop_table('appearances')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('appearances',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('rating', sa.INTEGER(), nullable=False),
    sa.Column('episode_id', sa.INTEGER(), nullable=True),
    sa.Column('guest_id', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['episode_id'], ['episodes.id'], ),
    sa.ForeignKeyConstraint(['guest_id'], ['guests.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('episodes',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('date', sa.VARCHAR(), nullable=False),
    sa.Column('number', sa.INTEGER(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('guests',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.VARCHAR(), nullable=False),
    sa.Column('occupation', sa.VARCHAR(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('appearance')
    op.drop_table('guest')
    op.drop_table('episode')
    # ### end Alembic commands ###

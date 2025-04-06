"""Initial migration

Revision ID: d52a217fdda6
Revises: 5d5b3314e19e
Create Date: 2025-04-06 14:03:09.146704

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd52a217fdda6'
down_revision = '5d5b3314e19e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('appearances', schema=None) as batch_op:
        batch_op.alter_column('rating',
               existing_type=sa.INTEGER(),
               nullable=False)

    with op.batch_alter_table('episodes', schema=None) as batch_op:
        batch_op.alter_column('date',
               existing_type=sa.VARCHAR(),
               nullable=False)
        batch_op.alter_column('number',
               existing_type=sa.INTEGER(),
               nullable=False)

    with op.batch_alter_table('guests', schema=None) as batch_op:
        batch_op.alter_column('name',
               existing_type=sa.VARCHAR(),
               nullable=False)
        batch_op.alter_column('occupation',
               existing_type=sa.VARCHAR(),
               nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('guests', schema=None) as batch_op:
        batch_op.alter_column('occupation',
               existing_type=sa.VARCHAR(),
               nullable=True)
        batch_op.alter_column('name',
               existing_type=sa.VARCHAR(),
               nullable=True)

    with op.batch_alter_table('episodes', schema=None) as batch_op:
        batch_op.alter_column('number',
               existing_type=sa.INTEGER(),
               nullable=True)
        batch_op.alter_column('date',
               existing_type=sa.VARCHAR(),
               nullable=True)

    with op.batch_alter_table('appearances', schema=None) as batch_op:
        batch_op.alter_column('rating',
               existing_type=sa.INTEGER(),
               nullable=True)

    # ### end Alembic commands ###

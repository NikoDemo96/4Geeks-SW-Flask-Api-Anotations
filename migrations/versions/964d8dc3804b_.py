"""empty message

Revision ID: 964d8dc3804b
Revises: 460b998af377
Create Date: 2023-05-08 14:46:29.310210

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '964d8dc3804b'
down_revision = '460b998af377'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('character', schema=None) as batch_op:
        batch_op.alter_column('eye_color',
               existing_type=sa.VARCHAR(length=30),
               nullable=True)
        batch_op.alter_column('hair_color',
               existing_type=sa.VARCHAR(length=30),
               nullable=True)
        batch_op.alter_column('gender',
               existing_type=sa.VARCHAR(length=30),
               nullable=True)
        batch_op.alter_column('birth_year',
               existing_type=sa.VARCHAR(length=30),
               nullable=True)
        batch_op.alter_column('height',
               existing_type=sa.INTEGER(),
               nullable=True)
        batch_op.alter_column('mass',
               existing_type=sa.INTEGER(),
               nullable=True)
        batch_op.alter_column('homeworld',
               existing_type=sa.VARCHAR(length=30),
               nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('character', schema=None) as batch_op:
        batch_op.alter_column('homeworld',
               existing_type=sa.VARCHAR(length=30),
               nullable=False)
        batch_op.alter_column('mass',
               existing_type=sa.INTEGER(),
               nullable=False)
        batch_op.alter_column('height',
               existing_type=sa.INTEGER(),
               nullable=False)
        batch_op.alter_column('birth_year',
               existing_type=sa.VARCHAR(length=30),
               nullable=False)
        batch_op.alter_column('gender',
               existing_type=sa.VARCHAR(length=30),
               nullable=False)
        batch_op.alter_column('hair_color',
               existing_type=sa.VARCHAR(length=30),
               nullable=False)
        batch_op.alter_column('eye_color',
               existing_type=sa.VARCHAR(length=30),
               nullable=False)

    # ### end Alembic commands ###
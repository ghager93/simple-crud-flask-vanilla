"""empty message

Revision ID: 1217aa703bed
Revises: 136dd8c0fa83
Create Date: 2023-01-19 15:07:14.677546

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1217aa703bed'
down_revision = '136dd8c0fa83'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('simples', schema=None) as batch_op:
        batch_op.add_column(sa.Column('updated_at', sa.DateTime(), nullable=True))
        batch_op.drop_column('updatted_at')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('simples', schema=None) as batch_op:
        batch_op.add_column(sa.Column('updatted_at', sa.DATETIME(), nullable=True))
        batch_op.drop_column('updated_at')

    # ### end Alembic commands ###

"""message

Revision ID: b9fdfcf60bf3
Revises: 
Create Date: 2023-01-25 12:28:04.632431

"""
from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision = 'b9fdfcf60bf3'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('simple',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('string', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('simple')
    # ### end Alembic commands ###

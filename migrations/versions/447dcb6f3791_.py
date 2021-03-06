"""empty message

Revision ID: 447dcb6f3791
Revises: b4bbec792683
Create Date: 2020-12-17 05:17:51.586847

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '447dcb6f3791'
down_revision = 'b4bbec792683'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('actors', 'movie_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('actors', 'movie_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    # ### end Alembic commands ###

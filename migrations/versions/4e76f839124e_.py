"""empty message

Revision ID: 4e76f839124e
Revises: 43914e4334c4
Create Date: 2023-12-29 06:24:55.496629

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4e76f839124e'
down_revision = '43914e4334c4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('sub', schema=None) as batch_op:
        batch_op.add_column(sa.Column('remarks', sa.String(length=40), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('sub', schema=None) as batch_op:
        batch_op.drop_column('remarks')

    # ### end Alembic commands ###

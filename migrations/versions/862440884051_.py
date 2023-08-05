"""empty message

Revision ID: 862440884051
Revises: 957726e496c5
Create Date: 2023-07-22 16:11:10.344927

"""
from alembic import op
import sqlalchemy as sa
from app.models import Recipient


# revision identifiers, used by Alembic.
revision = '862440884051'
down_revision = '957726e496c5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('recipient', schema=None) as batch_op:
        batch_op.add_column(sa.Column('list_kind', sa.String(length=255), nullable=True))

    # ### end Alembic commands ###
    seed()

def seed():
    recipients = Recipient.seed()
    op.bulk_insert(Recipient.__table__, recipients)

def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('recipient', schema=None) as batch_op:
        batch_op.drop_column('list_kind')

    # ### end Alembic commands ###

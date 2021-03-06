"""test deleted

Revision ID: 5e41dd0446de
Revises: 
Create Date: 2021-05-25 18:14:30.067033

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5e41dd0446de'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('department',
    sa.Column('id_dept', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('title', sa.String(length=140), nullable=True),
    sa.PrimaryKeyConstraint('id_dept')
    )
    op.create_table('employee',
    sa.Column('id_empl', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=140), nullable=True),
    sa.Column('salary', sa.Float(), nullable=True),
    sa.Column('birth', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id_empl')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('employee')
    op.drop_table('department')
    # ### end Alembic commands ###

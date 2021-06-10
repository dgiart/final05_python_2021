"""back to not ORM

Revision ID: 423b580affd9
Revises: 257563504eff
Create Date: 2021-05-31 20:02:11.959225

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '423b580affd9'
down_revision = '257563504eff'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('employee', sa.Column('id_empl_dept', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'employee', 'department', ['id_empl_dept'], ['id_dept'])
    op.drop_column('employee', 'id_dept')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('employee', sa.Column('id_dept', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'employee', type_='foreignkey')
    op.drop_column('employee', 'id_empl_dept')
    # ### end Alembic commands ###

"""use new models Produk

Revision ID: 530e1dd331f3
Revises: 
Create Date: 2023-10-28 18:17:10.091500

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '530e1dd331f3'
down_revision = None
branch_labels = None
depends_on = None

def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('produk',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('nama', sa.String(length=255), nullable=False),
    sa.Column('harga', sa.Integer(), nullable=False),
    sa.Column('stok', sa.Integer(), nullable=False),
    sa.Column('gambar', sa.String(length=255), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_produk'))
    )
    # ### end Alembic commands ###

def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('produk')
    # ### end Alembic commands ###

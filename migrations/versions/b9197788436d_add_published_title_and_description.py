""" Add published title and description

Revision ID: b9197788436d
Revises: 79a1e6e2ebfa
Create Date: 2018-07-16 04:23:47.924127

"""

# revision identifiers, used by Alembic.
revision = 'b9197788436d'
down_revision = '79a1e6e2ebfa'

from alembic import op
import sqlalchemy as sa


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('proposal', sa.Column('published_description', sa.String(), nullable=True))
    op.add_column('proposal', sa.Column('published_title', sa.String(), nullable=True))
    op.add_column('proposal_version', sa.Column('published_description', sa.String(), autoincrement=False, nullable=True))
    op.add_column('proposal_version', sa.Column('published_title', sa.String(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('proposal_version', 'published_title')
    op.drop_column('proposal_version', 'published_description')
    op.drop_column('proposal', 'published_title')
    op.drop_column('proposal', 'published_description')
    # ### end Alembic commands ###

"""jobs

Revision ID: 4f9336e7a5f5
Revises: 459218b0844c
Create Date: 2023-01-30 15:29:55.299262

"""
from alembic import op
import sqlalchemy as sa

import mindsdb.interfaces.storage.db

# revision identifiers, used by Alembic.
revision = '4f9336e7a5f5'
down_revision = '459218b0844c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        'jobs_history',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('job_id', sa.Integer(), nullable=True),
        sa.Column('start_at', sa.DateTime(), nullable=True),
        sa.Column('end_at', sa.DateTime(), nullable=True),
        sa.Column('error', sa.String(), nullable=True),
        sa.Column('created_at', sa.DateTime(), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_table(
        'jobs',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('company_id', sa.Integer(), nullable=True),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('project_id', sa.Integer(), nullable=False),
        sa.Column('query_str', sa.String(), nullable=False),
        sa.Column('start_at', sa.DateTime(), nullable=True),
        sa.Column('end_at', sa.DateTime(), nullable=True),
        sa.Column('next_run_at', sa.DateTime(), nullable=True),
        sa.Column('schedule_str', sa.String(), nullable=True),
        sa.Column('deleted_at', sa.DateTime(), nullable=True),
        sa.Column('updated_at', sa.DateTime(), nullable=True),
        sa.Column('created_at', sa.DateTime(), nullable=True),
        sa.ForeignKeyConstraint(['project_id'], ['project.id'], name='fk_jobs_project_id'),
        sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('view', schema=None) as batch_op:
        batch_op.drop_index('view_company_id_IDX')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('view', schema=None) as batch_op:
        batch_op.create_index('view_company_id_IDX', ['company_id', 'name'], unique=False)

    op.drop_table('jobs')
    op.drop_table('jobs_history')
    # ### end Alembic commands ###
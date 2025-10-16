"""add_zipcode_id_to_warehouse

Revision ID: dbb20bb871e1
Revises: ad791d6cbf8a
Create Date: 2025-10-15 21:57:29.135355

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'dbb20bb871e1'
down_revision: Union[str, Sequence[str], None] = 'ad791d6cbf8a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # Add zipcode_id column to warehouses table
    op.add_column('warehouses', sa.Column('zipcode_id', sa.UUID(), nullable=True))
    
    # Add foreign key constraint
    op.create_foreign_key(
        'fk_warehouses_zipcode_id', 
        'warehouses', 
        'master_zipcodes', 
        ['zipcode_id'], 
        ['id']
    )
    
    # Add index for performance
    op.create_index('idx_warehouses_zipcode_id', 'warehouses', ['zipcode_id'])


def downgrade() -> None:
    """Downgrade schema."""
    # Drop index
    op.drop_index('idx_warehouses_zipcode_id', table_name='warehouses')
    
    # Drop foreign key constraint
    op.drop_constraint('fk_warehouses_zipcode_id', 'warehouses', type_='foreignkey')
    
    # Drop column
    op.drop_column('warehouses', 'zipcode_id')

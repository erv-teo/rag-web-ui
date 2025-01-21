"""rename_metadata_to_chunk_metadata

Revision ID: 59cfa0f1361d
Revises: initial_schema
Create Date: 2025-01-13 23:26:38.232326

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision: str = '59cfa0f1361d'
down_revision: Union[str, None] = 'initial_schema'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index(op.f('ix_chats_id'), 'chats', ['id'], unique=False)
    op.add_column('document_chunks', sa.Column('document_id', sa.Integer(), nullable=False))
    op.add_column('document_chunks', sa.Column('chunk_metadata', sa.JSON(), nullable=True))
    op.alter_column('document_chunks', 'created_at',
               existing_type=mysql.TIMESTAMP(),
               type_=sa.DateTime(),
               nullable=False,
               existing_server_default=sa.text('CURRENT_TIMESTAMP'))
    op.alter_column('document_chunks', 'updated_at',
               existing_type=mysql.TIMESTAMP(),
               type_=sa.DateTime(),
               nullable=False,
               existing_server_default=sa.text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))
    op.drop_index('idx_hash', table_name='document_chunks')
    op.create_index(op.f('ix_document_chunks_hash'), 'document_chunks', ['hash'], unique=False)
    op.create_foreign_key(None, 'document_chunks', 'knowledge_bases', ['kb_id'], ['id'])
    op.create_foreign_key(None, 'document_chunks', 'documents', ['document_id'], ['id'])
    op.drop_column('document_chunks', 'metadata')
    op.drop_index('idx_file_hash', table_name='documents')
    op.create_index(op.f('ix_documents_file_hash'), 'documents', ['file_hash'], unique=False)
    op.create_index(op.f('ix_documents_id'), 'documents', ['id'], unique=False)
    op.create_index(op.f('ix_knowledge_bases_id'), 'knowledge_bases', ['id'], unique=False)
    op.create_index(op.f('ix_messages_id'), 'messages', ['id'], unique=False)
    op.alter_column('processing_tasks', 'knowledge_base_id',
               existing_type=mysql.INTEGER(),
               nullable=True)
    op.alter_column('processing_tasks', 'document_id',
               existing_type=mysql.INTEGER(),
               nullable=True)
    op.alter_column('processing_tasks', 'status',
               existing_type=mysql.VARCHAR(length=50),
               nullable=True)
    op.alter_column('processing_tasks', 'created_at',
               existing_type=mysql.DATETIME(),
               nullable=True)
    op.alter_column('processing_tasks', 'updated_at',
               existing_type=mysql.DATETIME(),
               nullable=True)
    op.create_index(op.f('ix_processing_tasks_id'), 'processing_tasks', ['id'], unique=False)
    op.drop_index('email', table_name='users')
    op.drop_index('username', table_name='users')
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=True)
    op.create_index(op.f('ix_users_id'), 'users', ['id'], unique=False)
    op.create_index(op.f('ix_users_username'), 'users', ['username'], unique=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_users_username'), table_name='users')
    op.drop_index(op.f('ix_users_id'), table_name='users')
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.create_index('username', 'users', ['username'], unique=True)
    op.create_index('email', 'users', ['email'], unique=True)
    op.drop_index(op.f('ix_processing_tasks_id'), table_name='processing_tasks')
    op.alter_column('processing_tasks', 'updated_at',
               existing_type=mysql.DATETIME(),
               nullable=False)
    op.alter_column('processing_tasks', 'created_at',
               existing_type=mysql.DATETIME(),
               nullable=False)
    op.alter_column('processing_tasks', 'status',
               existing_type=mysql.VARCHAR(length=50),
               nullable=False)
    op.alter_column('processing_tasks', 'document_id',
               existing_type=mysql.INTEGER(),
               nullable=False)
    op.alter_column('processing_tasks', 'knowledge_base_id',
               existing_type=mysql.INTEGER(),
               nullable=False)
    op.drop_index(op.f('ix_messages_id'), table_name='messages')
    op.drop_index(op.f('ix_knowledge_bases_id'), table_name='knowledge_bases')
    op.drop_index(op.f('ix_documents_id'), table_name='documents')
    op.drop_index(op.f('ix_documents_file_hash'), table_name='documents')
    op.create_index('idx_file_hash', 'documents', ['file_hash'], unique=False)
    op.add_column('document_chunks', sa.Column('metadata', mysql.JSON(), nullable=True))
    op.drop_constraint(None, 'document_chunks', type_='foreignkey')
    op.drop_constraint(None, 'document_chunks', type_='foreignkey')
    op.drop_index(op.f('ix_document_chunks_hash'), table_name='document_chunks')
    op.create_index('idx_hash', 'document_chunks', ['hash'], unique=False)
    op.alter_column('document_chunks', 'updated_at',
               existing_type=sa.DateTime(),
               type_=mysql.TIMESTAMP(),
               nullable=True,
               existing_server_default=sa.text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))
    op.alter_column('document_chunks', 'created_at',
               existing_type=sa.DateTime(),
               type_=mysql.TIMESTAMP(),
               nullable=True,
               existing_server_default=sa.text('CURRENT_TIMESTAMP'))
    op.drop_column('document_chunks', 'chunk_metadata')
    op.drop_column('document_chunks', 'document_id')
    op.drop_index(op.f('ix_chats_id'), table_name='chats')
    # ### end Alembic commands ###

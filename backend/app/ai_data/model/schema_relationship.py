from datetime import datetime

import sqlalchemy as sa

from sqlalchemy.dialects import mysql
from sqlalchemy.orm import Mapped, mapped_column

from backend.common.model import Base, id_key


class SchemaRelationship(Base):
    """Schema表间关系"""

    __tablename__ = 'schema_relationship'

    id: Mapped[id_key] = mapped_column(init=False)
    connection_id: Mapped[int] = mapped_column(sa.BIGINT(), default=0, sort_order=2, comment='关联数据源ID（外键: conn_source.id）')
    source_table_id: Mapped[int] = mapped_column(sa.BIGINT(), default=0, sort_order=3, comment='源表ID（外键: schema_table.id）')
    source_column_id: Mapped[int] = mapped_column(sa.BIGINT(), default=0, sort_order=4, comment='源列ID（外键: schema_column.id）')
    target_table_id: Mapped[int] = mapped_column(sa.BIGINT(), default=0, sort_order=5, comment='目标表ID（外键: schema_table.id）')
    target_column_id: Mapped[int] = mapped_column(sa.BIGINT(), default=0, sort_order=6, comment='目标列ID（外键: schema_column.id）')
    relationship_type: Mapped[str | None] = mapped_column(sa.String(50), default=None, sort_order=7, comment='关系类型（如: 1-to-1, 1-to-N, N-to-M）')
    description: Mapped[str | None] = mapped_column(sa.TEXT(), default=None, sort_order=8, comment='关系描述')

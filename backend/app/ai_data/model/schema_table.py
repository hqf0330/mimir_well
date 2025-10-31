from datetime import datetime

import sqlalchemy as sa

from sqlalchemy.dialects import mysql
from sqlalchemy.orm import Mapped, mapped_column

from backend.common.model import Base, id_key


class SchemaTable(Base):
    """Schema表元数据"""

    __tablename__ = 'schema_table'

    id: Mapped[id_key] = mapped_column(init=False)
    connection_id: Mapped[int] = mapped_column(sa.BIGINT(), default=0, sort_order=2, comment='关联数据源ID（外键: conn_source.id）')
    table_name: Mapped[str] = mapped_column(sa.String(255), default='', sort_order=3, comment='表名')
    description: Mapped[str | None] = mapped_column(sa.TEXT(), default=None, sort_order=4, comment='表描述')
    ui_metadata: Mapped[dict | None] = mapped_column(sa.JSON(), default=None, sort_order=5, comment='UI元数据（表位置、颜色等）')

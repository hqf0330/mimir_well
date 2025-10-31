from datetime import datetime

import sqlalchemy as sa

from sqlalchemy.dialects import mysql
from sqlalchemy.orm import Mapped, mapped_column

from backend.common.model import Base, id_key


class SchemaColumn(Base):
    """Schema列信息"""

    __tablename__ = 'schema_column'

    id: Mapped[id_key] = mapped_column(init=False)
    table_id: Mapped[int] = mapped_column(sa.BIGINT(), default=0, sort_order=2, comment='关联表ID（外键: schema_table.id）')
    column_name: Mapped[str] = mapped_column(sa.String(255), default='', sort_order=3, comment='列名')
    data_type: Mapped[str] = mapped_column(sa.String(100), default='', sort_order=4, comment='数据类型（如: VARCHAR, INT, DATETIME）')
    description: Mapped[str | None] = mapped_column(sa.TEXT(), default=None, sort_order=5, comment='列描述')
    is_primary_key: Mapped[int] = mapped_column(mysql.TINYINT(), default=0, sort_order=6, comment='是否主键')
    is_foreign_key: Mapped[int] = mapped_column(mysql.TINYINT(), default=0, sort_order=7, comment='是否外键')
    is_unique: Mapped[int] = mapped_column(mysql.TINYINT(), default=0, sort_order=8, comment='是否唯一约束')
    is_nullable: Mapped[int] = mapped_column(mysql.TINYINT(), default=0, sort_order=9, comment='是否可为空')
    column_default: Mapped[str | None] = mapped_column(sa.String(255), default=None, sort_order=10, comment='默认值')
    ordinal_position: Mapped[int | None] = mapped_column(sa.INT(), default=None, sort_order=11, comment='列在表中的位置（排序用）')
    character_maximum_length: Mapped[int | None] = mapped_column(sa.INT(), default=None, sort_order=12, comment='字符最大长度（用于VARCHAR等）')
    numeric_precision: Mapped[int | None] = mapped_column(sa.INT(), default=None, sort_order=13, comment='数值精度')
    numeric_scale: Mapped[int | None] = mapped_column(sa.INT(), default=None, sort_order=14, comment='数值小数位数')

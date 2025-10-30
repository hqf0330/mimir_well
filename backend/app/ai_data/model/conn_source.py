from datetime import datetime

import sqlalchemy as sa

from sqlalchemy.dialects import mysql
from sqlalchemy.orm import Mapped, mapped_column

from backend.common.model import Base, id_key


class ConnSource(Base):
    """数据源"""

    __tablename__ = 'conn_source'

    id: Mapped[id_key] = mapped_column(init=False)
    name: Mapped[str] = mapped_column(sa.String(255), default='', sort_order=2, comment='数据源名称')
    conn_type: Mapped[str] = mapped_column(sa.String(50), default='', sort_order=3, comment='数据源类型')
    host: Mapped[str] = mapped_column(sa.String(255), default='', sort_order=4, comment='连接host')
    port: Mapped[int] = mapped_column(sa.INT(), default=0, sort_order=5, comment='端口')
    username: Mapped[str] = mapped_column(sa.String(255), default='', sort_order=6, comment='账号')
    password_encrypted: Mapped[str] = mapped_column(sa.String(255), default='', sort_order=7, comment='密码')
    db_name: Mapped[str] = mapped_column(sa.String(255), default='', sort_order=8, comment='数据库')
    status: Mapped[int] = mapped_column(mysql.TINYINT(), default='1', sort_order=9, comment='是否启用')
    description: Mapped[str] = mapped_column(sa.String(255), default='', sort_order=10, comment='描述')

from datetime import datetime

from pydantic import ConfigDict, Field

from backend.common.schema import SchemaBase


class ConnSourceSchemaBase(SchemaBase):
    """数据源基础模型"""
    name: str = Field(description='数据源名称')
    conn_type: str = Field(description='数据源类型')
    host: str = Field(description='连接host')
    port: int = Field(description='端口')
    username: str = Field(description='账号')
    password_encrypted: str = Field(description='密码')
    db_name: str = Field(description='数据库')
    status: int = Field(description='是否启用')
    description: str = Field(description='描述')


class CreateConnSourceParam(ConnSourceSchemaBase):
    """创建数据源参数"""


class UpdateConnSourceParam(ConnSourceSchemaBase):
    """更新数据源参数"""


class DeleteConnSourceParam(SchemaBase):
    """删除数据源参数"""

    pks: list[int] = Field(description='数据源 ID 列表')


class GetConnSourceDetail(ConnSourceSchemaBase):
    """数据源详情"""

    model_config = ConfigDict(from_attributes=True)

    id: int
    created_time: datetime
    updated_time: datetime | None = None

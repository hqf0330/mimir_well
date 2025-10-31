from datetime import datetime

from pydantic import ConfigDict, Field

from backend.common.schema import SchemaBase


class SchemaTableSchemaBase(SchemaBase):
    """Schema表元数据基础模型"""
    connection_id: int = Field(description='关联数据源ID（外键: conn_source.id）')
    table_name: str = Field(description='表名')
    description: str | None = Field(None, description='表描述')
    ui_metadata: dict | None = Field(None, description='UI元数据（表位置、颜色等）')


class CreateSchemaTableParam(SchemaTableSchemaBase):
    """创建Schema表元数据参数"""


class UpdateSchemaTableParam(SchemaTableSchemaBase):
    """更新Schema表元数据参数"""


class DeleteSchemaTableParam(SchemaBase):
    """删除Schema表元数据参数"""

    pks: list[int] = Field(description='Schema表元数据 ID 列表')


class GetSchemaTableDetail(SchemaTableSchemaBase):
    """Schema表元数据详情"""

    model_config = ConfigDict(from_attributes=True)

    id: int
    created_time: datetime
    updated_time: datetime | None = None

from datetime import datetime

from pydantic import ConfigDict, Field

from backend.common.schema import SchemaBase


class SchemaRelationshipSchemaBase(SchemaBase):
    """Schema表间关系基础模型"""
    connection_id: int = Field(description='关联数据源ID（外键: conn_source.id）')
    source_table_id: int = Field(description='源表ID（外键: schema_table.id）')
    source_column_id: int = Field(description='源列ID（外键: schema_column.id）')
    target_table_id: int = Field(description='目标表ID（外键: schema_table.id）')
    target_column_id: int = Field(description='目标列ID（外键: schema_column.id）')
    relationship_type: str | None = Field(None, description='关系类型（如: 1-to-1, 1-to-N, N-to-M）')
    description: str | None = Field(None, description='关系描述')


class CreateSchemaRelationshipParam(SchemaRelationshipSchemaBase):
    """创建Schema表间关系参数"""


class UpdateSchemaRelationshipParam(SchemaRelationshipSchemaBase):
    """更新Schema表间关系参数"""


class DeleteSchemaRelationshipParam(SchemaBase):
    """删除Schema表间关系参数"""

    pks: list[int] = Field(description='Schema表间关系 ID 列表')


class GetSchemaRelationshipDetail(SchemaRelationshipSchemaBase):
    """Schema表间关系详情"""

    model_config = ConfigDict(from_attributes=True)

    id: int
    created_time: datetime
    updated_time: datetime | None = None

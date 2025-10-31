from datetime import datetime

from pydantic import ConfigDict, Field

from backend.common.schema import SchemaBase


class SchemaColumnSchemaBase(SchemaBase):
    """Schema列信息基础模型"""
    table_id: int = Field(description='关联表ID（外键: schema_table.id）')
    column_name: str = Field(description='列名')
    data_type: str = Field(description='数据类型（如: VARCHAR, INT, DATETIME）')
    description: str | None = Field(None, description='列描述')
    is_primary_key: int = Field(description='是否主键')
    is_foreign_key: int = Field(description='是否外键')
    is_unique: int = Field(description='是否唯一约束')
    is_nullable: int = Field(description='是否可为空')
    column_default: str | None = Field(None, description='默认值')
    ordinal_position: int | None = Field(None, description='列在表中的位置（排序用）')
    character_maximum_length: int | None = Field(None, description='字符最大长度（用于VARCHAR等）')
    numeric_precision: int | None = Field(None, description='数值精度')
    numeric_scale: int | None = Field(None, description='数值小数位数')


class CreateSchemaColumnParam(SchemaColumnSchemaBase):
    """创建Schema列信息参数"""


class UpdateSchemaColumnParam(SchemaColumnSchemaBase):
    """更新Schema列信息参数"""


class DeleteSchemaColumnParam(SchemaBase):
    """删除Schema列信息参数"""

    pks: list[int] = Field(description='Schema列信息 ID 列表')


class GetSchemaColumnDetail(SchemaColumnSchemaBase):
    """Schema列信息详情"""

    model_config = ConfigDict(from_attributes=True)

    id: int
    created_time: datetime
    updated_time: datetime | None = None

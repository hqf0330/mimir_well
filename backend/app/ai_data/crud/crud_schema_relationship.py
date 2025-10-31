from typing import Sequence

from sqlalchemy import Select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy_crud_plus import CRUDPlus

from backend.app.ai_data.model import SchemaRelationship
from backend.app.ai_data.schema.schema_relationship import CreateSchemaRelationshipParam, UpdateSchemaRelationshipParam


class CRUDSchemaRelationship(CRUDPlus[SchemaRelationship]):
    async def get(self, db: AsyncSession, pk: int) -> SchemaRelationship | None:
        """
        获取Schema表间关系

        :param db: 数据库会话
        :param pk: Schema表间关系 ID
        :return:
        """
        return await self.select_model(db, pk)

    async def get_select(self) -> Select:
        """获取Schema表间关系列表查询表达式"""
        return await self.select_order('id', 'desc')

    async def get_all(self, db: AsyncSession) -> Sequence[SchemaRelationship]:
        """
        获取所有Schema表间关系

        :param db: 数据库会话
        :return:
        """
        return await self.select_models(db)

    async def create(self, db: AsyncSession, obj: CreateSchemaRelationshipParam) -> None:
        """
        创建Schema表间关系

        :param db: 数据库会话
        :param obj: 创建Schema表间关系参数
        :return:
        """
        await self.create_model(db, obj)

    async def update(self, db: AsyncSession, pk: int, obj: UpdateSchemaRelationshipParam) -> int:
        """
        更新Schema表间关系

        :param db: 数据库会话
        :param pk: Schema表间关系 ID
        :param obj: 更新 Schema表间关系参数
        :return:
        """
        return await self.update_model(db, pk, obj)

    async def delete(self, db: AsyncSession, pks: list[int]) -> int:
        """
        批量删除Schema表间关系

        :param db: 数据库会话
        :param pks: Schema表间关系 ID 列表
        :return:
        """
        return await self.delete_model_by_column(db, allow_multiple=True, id__in=pks)


schema_relationship_dao: CRUDSchemaRelationship = CRUDSchemaRelationship(SchemaRelationship)

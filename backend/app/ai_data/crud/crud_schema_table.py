from typing import Sequence

from sqlalchemy import Select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy_crud_plus import CRUDPlus

from backend.app.ai_data.model import SchemaTable
from backend.app.ai_data.schema.schema_table import CreateSchemaTableParam, UpdateSchemaTableParam


class CRUDSchemaTable(CRUDPlus[SchemaTable]):
    async def get(self, db: AsyncSession, pk: int) -> SchemaTable | None:
        """
        获取Schema表元数据

        :param db: 数据库会话
        :param pk: Schema表元数据 ID
        :return:
        """
        return await self.select_model(db, pk)

    async def get_select(self) -> Select:
        """获取Schema表元数据列表查询表达式"""
        return await self.select_order('id', 'desc')

    async def get_all(self, db: AsyncSession) -> Sequence[SchemaTable]:
        """
        获取所有Schema表元数据

        :param db: 数据库会话
        :return:
        """
        return await self.select_models(db)

    async def create(self, db: AsyncSession, obj: CreateSchemaTableParam) -> None:
        """
        创建Schema表元数据

        :param db: 数据库会话
        :param obj: 创建Schema表元数据参数
        :return:
        """
        await self.create_model(db, obj)

    async def update(self, db: AsyncSession, pk: int, obj: UpdateSchemaTableParam) -> int:
        """
        更新Schema表元数据

        :param db: 数据库会话
        :param pk: Schema表元数据 ID
        :param obj: 更新 Schema表元数据参数
        :return:
        """
        return await self.update_model(db, pk, obj)

    async def delete(self, db: AsyncSession, pks: list[int]) -> int:
        """
        批量删除Schema表元数据

        :param db: 数据库会话
        :param pks: Schema表元数据 ID 列表
        :return:
        """
        return await self.delete_model_by_column(db, allow_multiple=True, id__in=pks)


schema_table_dao: CRUDSchemaTable = CRUDSchemaTable(SchemaTable)

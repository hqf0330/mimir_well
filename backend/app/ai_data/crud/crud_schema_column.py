from typing import Sequence

from sqlalchemy import Select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy_crud_plus import CRUDPlus

from backend.app.ai_data.model import SchemaColumn
from backend.app.ai_data.schema.schema_column import CreateSchemaColumnParam, UpdateSchemaColumnParam


class CRUDSchemaColumn(CRUDPlus[SchemaColumn]):
    async def get(self, db: AsyncSession, pk: int) -> SchemaColumn | None:
        """
        获取Schema列信息

        :param db: 数据库会话
        :param pk: Schema列信息 ID
        :return:
        """
        return await self.select_model(db, pk)

    async def get_select(self) -> Select:
        """获取Schema列信息列表查询表达式"""
        return await self.select_order('id', 'desc')

    async def get_all(self, db: AsyncSession) -> Sequence[SchemaColumn]:
        """
        获取所有Schema列信息

        :param db: 数据库会话
        :return:
        """
        return await self.select_models(db)

    async def create(self, db: AsyncSession, obj: CreateSchemaColumnParam) -> None:
        """
        创建Schema列信息

        :param db: 数据库会话
        :param obj: 创建Schema列信息参数
        :return:
        """
        await self.create_model(db, obj)

    async def update(self, db: AsyncSession, pk: int, obj: UpdateSchemaColumnParam) -> int:
        """
        更新Schema列信息

        :param db: 数据库会话
        :param pk: Schema列信息 ID
        :param obj: 更新 Schema列信息参数
        :return:
        """
        return await self.update_model(db, pk, obj)

    async def delete(self, db: AsyncSession, pks: list[int]) -> int:
        """
        批量删除Schema列信息

        :param db: 数据库会话
        :param pks: Schema列信息 ID 列表
        :return:
        """
        return await self.delete_model_by_column(db, allow_multiple=True, id__in=pks)


schema_column_dao: CRUDSchemaColumn = CRUDSchemaColumn(SchemaColumn)

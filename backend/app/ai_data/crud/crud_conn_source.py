from typing import Sequence

from sqlalchemy import Select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy_crud_plus import CRUDPlus

from backend.app.ai_data.model import ConnSource
from backend.app.ai_data.schema.conn_source import CreateConnSourceParam, UpdateConnSourceParam


class CRUDConnSource(CRUDPlus[ConnSource]):
    async def get(self, db: AsyncSession, pk: int) -> ConnSource | None:
        """
        获取数据源

        :param db: 数据库会话
        :param pk: 数据源 ID
        :return:
        """
        return await self.select_model(db, pk)

    async def get_select(self) -> Select:
        """获取数据源列表查询表达式"""
        return await self.select_order('id', 'desc')

    async def get_all(self, db: AsyncSession) -> Sequence[ConnSource]:
        """
        获取所有数据源

        :param db: 数据库会话
        :return:
        """
        return await self.select_models(db)

    async def create(self, db: AsyncSession, obj: CreateConnSourceParam) -> None:
        """
        创建数据源

        :param db: 数据库会话
        :param obj: 创建数据源参数
        :return:
        """
        await self.create_model(db, obj)

    async def update(self, db: AsyncSession, pk: int, obj: UpdateConnSourceParam) -> int:
        """
        更新数据源

        :param db: 数据库会话
        :param pk: 数据源 ID
        :param obj: 更新 数据源参数
        :return:
        """
        return await self.update_model(db, pk, obj)

    async def delete(self, db: AsyncSession, pks: list[int]) -> int:
        """
        批量删除数据源

        :param db: 数据库会话
        :param pks: 数据源 ID 列表
        :return:
        """
        return await self.delete_model_by_column(db, allow_multiple=True, id__in=pks)


conn_source_dao: CRUDConnSource = CRUDConnSource(ConnSource)

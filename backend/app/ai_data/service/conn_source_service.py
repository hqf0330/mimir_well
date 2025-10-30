from typing import Any, Sequence

from sqlalchemy.ext.asyncio import AsyncSession

from backend.app.ai_data.crud.crud_conn_source import conn_source_dao
from backend.app.ai_data.model import ConnSource
from backend.app.ai_data.schema.conn_source import CreateConnSourceParam, DeleteConnSourceParam, UpdateConnSourceParam
from backend.common.exception import errors
from backend.common.pagination import paging_data


class ConnSourceService:
    @staticmethod
    async def get(*, db: AsyncSession, pk: int) -> ConnSource:
        """
        获取数据源

        :param db: 数据库会话
        :param pk: 数据源 ID
        :return:
        """
        conn_source = await conn_source_dao.get(db, pk)
        if not conn_source:
            raise errors.NotFoundError(msg='数据源不存在')
        return conn_source

    @staticmethod
    async def get_list(db: AsyncSession) -> dict[str, Any]:
        """
        获取数据源列表

        :param db: 数据库会话
        :return:
        """
        conn_source_select = await conn_source_dao.get_select()
        return await paging_data(db, conn_source_select)

    @staticmethod
    async def get_all(*, db: AsyncSession) -> Sequence[ConnSource]:
        """
        获取所有数据源

        :param db: 数据库会话
        :return:
        """
        conn_sources = await conn_source_dao.get_all(db)
        return conn_sources

    @staticmethod
    async def create(*, db: AsyncSession, obj: CreateConnSourceParam) -> None:
        """
        创建数据源

        :param db: 数据库会话
        :param obj: 创建数据源参数
        :return:
        """
        await conn_source_dao.create(db, obj)

    @staticmethod
    async def update(*, db: AsyncSession, pk: int, obj: UpdateConnSourceParam) -> int:
        """
        更新数据源

        :param db: 数据库会话
        :param pk: 数据源 ID
        :param obj: 更新数据源参数
        :return:
        """
        count = await conn_source_dao.update(db, pk, obj)
        return count

    @staticmethod
    async def delete(*, db: AsyncSession, obj: DeleteConnSourceParam) -> int:
        """
        删除数据源

        :param db: 数据库会话
        :param obj: 数据源 ID 列表
        :return:
        """
        count = await conn_source_dao.delete(db, obj.pks)
        return count


conn_source_service: ConnSourceService = ConnSourceService()

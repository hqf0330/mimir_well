from typing import Any, Sequence

from sqlalchemy.ext.asyncio import AsyncSession

from backend.app.ai_data.crud.crud_schema_table import schema_table_dao
from backend.app.ai_data.model import SchemaTable
from backend.app.ai_data.schema.schema_table import CreateSchemaTableParam, DeleteSchemaTableParam, UpdateSchemaTableParam
from backend.common.exception import errors
from backend.common.pagination import paging_data


class SchemaTableService:
    @staticmethod
    async def get(*, db: AsyncSession, pk: int) -> SchemaTable:
        """
        获取Schema表元数据

        :param db: 数据库会话
        :param pk: Schema表元数据 ID
        :return:
        """
        schema_table = await schema_table_dao.get(db, pk)
        if not schema_table:
            raise errors.NotFoundError(msg='Schema表元数据不存在')
        return schema_table

    @staticmethod
    async def get_list(db: AsyncSession) -> dict[str, Any]:
        """
        获取Schema表元数据列表

        :param db: 数据库会话
        :return:
        """
        schema_table_select = await schema_table_dao.get_select()
        return await paging_data(db, schema_table_select)

    @staticmethod
    async def get_all(*, db: AsyncSession) -> Sequence[SchemaTable]:
        """
        获取所有Schema表元数据

        :param db: 数据库会话
        :return:
        """
        schema_tables = await schema_table_dao.get_all(db)
        return schema_tables

    @staticmethod
    async def create(*, db: AsyncSession, obj: CreateSchemaTableParam) -> None:
        """
        创建Schema表元数据

        :param db: 数据库会话
        :param obj: 创建Schema表元数据参数
        :return:
        """
        await schema_table_dao.create(db, obj)

    @staticmethod
    async def update(*, db: AsyncSession, pk: int, obj: UpdateSchemaTableParam) -> int:
        """
        更新Schema表元数据

        :param db: 数据库会话
        :param pk: Schema表元数据 ID
        :param obj: 更新Schema表元数据参数
        :return:
        """
        count = await schema_table_dao.update(db, pk, obj)
        return count

    @staticmethod
    async def delete(*, db: AsyncSession, obj: DeleteSchemaTableParam) -> int:
        """
        删除Schema表元数据

        :param db: 数据库会话
        :param obj: Schema表元数据 ID 列表
        :return:
        """
        count = await schema_table_dao.delete(db, obj.pks)
        return count


schema_table_service: SchemaTableService = SchemaTableService()

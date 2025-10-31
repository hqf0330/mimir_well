from typing import Any, Sequence

from sqlalchemy.ext.asyncio import AsyncSession

from backend.app.ai_data.crud.crud_schema_column import schema_column_dao
from backend.app.ai_data.model import SchemaColumn
from backend.app.ai_data.schema.schema_column import CreateSchemaColumnParam, DeleteSchemaColumnParam, UpdateSchemaColumnParam
from backend.common.exception import errors
from backend.common.pagination import paging_data


class SchemaColumnService:
    @staticmethod
    async def get(*, db: AsyncSession, pk: int) -> SchemaColumn:
        """
        获取Schema列信息

        :param db: 数据库会话
        :param pk: Schema列信息 ID
        :return:
        """
        schema_column = await schema_column_dao.get(db, pk)
        if not schema_column:
            raise errors.NotFoundError(msg='Schema列信息不存在')
        return schema_column

    @staticmethod
    async def get_list(db: AsyncSession) -> dict[str, Any]:
        """
        获取Schema列信息列表

        :param db: 数据库会话
        :return:
        """
        schema_column_select = await schema_column_dao.get_select()
        return await paging_data(db, schema_column_select)

    @staticmethod
    async def get_all(*, db: AsyncSession) -> Sequence[SchemaColumn]:
        """
        获取所有Schema列信息

        :param db: 数据库会话
        :return:
        """
        schema_columns = await schema_column_dao.get_all(db)
        return schema_columns

    @staticmethod
    async def create(*, db: AsyncSession, obj: CreateSchemaColumnParam) -> None:
        """
        创建Schema列信息

        :param db: 数据库会话
        :param obj: 创建Schema列信息参数
        :return:
        """
        await schema_column_dao.create(db, obj)

    @staticmethod
    async def update(*, db: AsyncSession, pk: int, obj: UpdateSchemaColumnParam) -> int:
        """
        更新Schema列信息

        :param db: 数据库会话
        :param pk: Schema列信息 ID
        :param obj: 更新Schema列信息参数
        :return:
        """
        count = await schema_column_dao.update(db, pk, obj)
        return count

    @staticmethod
    async def delete(*, db: AsyncSession, obj: DeleteSchemaColumnParam) -> int:
        """
        删除Schema列信息

        :param db: 数据库会话
        :param obj: Schema列信息 ID 列表
        :return:
        """
        count = await schema_column_dao.delete(db, obj.pks)
        return count


schema_column_service: SchemaColumnService = SchemaColumnService()

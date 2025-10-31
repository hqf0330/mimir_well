from typing import Any, Sequence

from sqlalchemy.ext.asyncio import AsyncSession

from backend.app.ai_data.crud.crud_schema_relationship import schema_relationship_dao
from backend.app.ai_data.model import SchemaRelationship
from backend.app.ai_data.schema.schema_relationship import CreateSchemaRelationshipParam, DeleteSchemaRelationshipParam, UpdateSchemaRelationshipParam
from backend.common.exception import errors
from backend.common.pagination import paging_data


class SchemaRelationshipService:
    @staticmethod
    async def get(*, db: AsyncSession, pk: int) -> SchemaRelationship:
        """
        获取Schema表间关系

        :param db: 数据库会话
        :param pk: Schema表间关系 ID
        :return:
        """
        schema_relationship = await schema_relationship_dao.get(db, pk)
        if not schema_relationship:
            raise errors.NotFoundError(msg='Schema表间关系不存在')
        return schema_relationship

    @staticmethod
    async def get_list(db: AsyncSession) -> dict[str, Any]:
        """
        获取Schema表间关系列表

        :param db: 数据库会话
        :return:
        """
        schema_relationship_select = await schema_relationship_dao.get_select()
        return await paging_data(db, schema_relationship_select)

    @staticmethod
    async def get_all(*, db: AsyncSession) -> Sequence[SchemaRelationship]:
        """
        获取所有Schema表间关系

        :param db: 数据库会话
        :return:
        """
        schema_relationships = await schema_relationship_dao.get_all(db)
        return schema_relationships

    @staticmethod
    async def create(*, db: AsyncSession, obj: CreateSchemaRelationshipParam) -> None:
        """
        创建Schema表间关系

        :param db: 数据库会话
        :param obj: 创建Schema表间关系参数
        :return:
        """
        await schema_relationship_dao.create(db, obj)

    @staticmethod
    async def update(*, db: AsyncSession, pk: int, obj: UpdateSchemaRelationshipParam) -> int:
        """
        更新Schema表间关系

        :param db: 数据库会话
        :param pk: Schema表间关系 ID
        :param obj: 更新Schema表间关系参数
        :return:
        """
        count = await schema_relationship_dao.update(db, pk, obj)
        return count

    @staticmethod
    async def delete(*, db: AsyncSession, obj: DeleteSchemaRelationshipParam) -> int:
        """
        删除Schema表间关系

        :param db: 数据库会话
        :param obj: Schema表间关系 ID 列表
        :return:
        """
        count = await schema_relationship_dao.delete(db, obj.pks)
        return count


schema_relationship_service: SchemaRelationshipService = SchemaRelationshipService()

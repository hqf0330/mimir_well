from typing import Annotated

from fastapi import APIRouter, Depends, Path, Query

from backend.app.ai_data.schema.schema_relationship import (
    CreateSchemaRelationshipParam,
    DeleteSchemaRelationshipParam,
    GetSchemaRelationshipDetail,
    UpdateSchemaRelationshipParam,
)
from backend.app.ai_data.service.schema_relationship_service import schema_relationship_service
from backend.common.pagination import DependsPagination, PageData
from backend.common.response.response_schema import ResponseModel, ResponseSchemaModel, response_base
from backend.common.security.jwt import DependsJwtAuth
from backend.common.security.permission import RequestPermission
from backend.common.security.rbac import DependsRBAC
from backend.database.db import CurrentSession, CurrentSessionTransaction
from backend.database.db import CurrentSession

router = APIRouter()


@router.get('/{pk}', summary='获取Schema表间关系详情', dependencies=[DependsJwtAuth])
async def get_schema_relationship(
    db: CurrentSession, pk: Annotated[int, Path(description='Schema表间关系 ID')]
) -> ResponseSchemaModel[GetSchemaRelationshipDetail]:
    schema_relationship = await schema_relationship_service.get(db=db, pk=pk)
    return response_base.success(data=schema_relationship)


@router.get(
    '',
    summary='分页获取所有Schema表间关系',
    dependencies=[
        DependsJwtAuth,
        DependsPagination,
    ],
)
async def get_schema_relationships_paginated(db: CurrentSession) -> ResponseSchemaModel[PageData[GetSchemaRelationshipDetail]]:
    page_data = await schema_relationship_service.get_list(db=db)
    return response_base.success(data=page_data)


@router.post(
    '',
    summary='创建Schema表间关系',
    dependencies=[
        Depends(RequestPermission('schema:relationship:add')),
        DependsRBAC,
    ],
)
async def create_schema_relationship(db: CurrentSessionTransaction, obj: CreateSchemaRelationshipParam) -> ResponseModel:
    await schema_relationship_service.create(db=db, obj=obj)
    return response_base.success()


@router.put(
    '/{pk}',
    summary='更新Schema表间关系',
    dependencies=[
        Depends(RequestPermission('schema:relationship:edit')),
        DependsRBAC,
    ],
)
async def update_schema_relationship(
    db: CurrentSessionTransaction, pk: Annotated[int, Path(description='Schema表间关系 ID')], obj: UpdateSchemaRelationshipParam
) -> ResponseModel:
    count = await schema_relationship_service.update(db=db, pk=pk, obj=obj)
    if count > 0:
        return response_base.success()
    return response_base.fail()


@router.delete(
    '',
    summary='批量删除Schema表间关系',
    dependencies=[
        Depends(RequestPermission('schema:relationship:del')),
        DependsRBAC,
    ],
)
async def delete_schema_relationships(db: CurrentSessionTransaction, obj: DeleteSchemaRelationshipParam) -> ResponseModel:
    count = await schema_relationship_service.delete(db=db, obj=obj)
    if count > 0:
        return response_base.success()
    return response_base.fail()

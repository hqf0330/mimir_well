from typing import Annotated

from fastapi import APIRouter, Depends, Path, Query

from backend.app.ai_data.schema.schema_column import (
    CreateSchemaColumnParam,
    DeleteSchemaColumnParam,
    GetSchemaColumnDetail,
    UpdateSchemaColumnParam,
)
from backend.app.ai_data.service.schema_column_service import schema_column_service
from backend.common.pagination import DependsPagination, PageData
from backend.common.response.response_schema import ResponseModel, ResponseSchemaModel, response_base
from backend.common.security.jwt import DependsJwtAuth
from backend.common.security.permission import RequestPermission
from backend.common.security.rbac import DependsRBAC
from backend.database.db import CurrentSession, CurrentSessionTransaction
from backend.database.db import CurrentSession

router = APIRouter()


@router.get('/{pk}', summary='获取Schema列信息详情', dependencies=[DependsJwtAuth])
async def get_schema_column(
    db: CurrentSession, pk: Annotated[int, Path(description='Schema列信息 ID')]
) -> ResponseSchemaModel[GetSchemaColumnDetail]:
    schema_column = await schema_column_service.get(db=db, pk=pk)
    return response_base.success(data=schema_column)


@router.get(
    '',
    summary='分页获取所有Schema列信息',
    dependencies=[
        DependsJwtAuth,
        DependsPagination,
    ],
)
async def get_schema_columns_paginated(db: CurrentSession) -> ResponseSchemaModel[PageData[GetSchemaColumnDetail]]:
    page_data = await schema_column_service.get_list(db=db)
    return response_base.success(data=page_data)


@router.post(
    '',
    summary='创建Schema列信息',
    dependencies=[
        Depends(RequestPermission('schema:column:add')),
        DependsRBAC,
    ],
)
async def create_schema_column(db: CurrentSessionTransaction, obj: CreateSchemaColumnParam) -> ResponseModel:
    await schema_column_service.create(db=db, obj=obj)
    return response_base.success()


@router.put(
    '/{pk}',
    summary='更新Schema列信息',
    dependencies=[
        Depends(RequestPermission('schema:column:edit')),
        DependsRBAC,
    ],
)
async def update_schema_column(
    db: CurrentSessionTransaction, pk: Annotated[int, Path(description='Schema列信息 ID')], obj: UpdateSchemaColumnParam
) -> ResponseModel:
    count = await schema_column_service.update(db=db, pk=pk, obj=obj)
    if count > 0:
        return response_base.success()
    return response_base.fail()


@router.delete(
    '',
    summary='批量删除Schema列信息',
    dependencies=[
        Depends(RequestPermission('schema:column:del')),
        DependsRBAC,
    ],
)
async def delete_schema_columns(db: CurrentSessionTransaction, obj: DeleteSchemaColumnParam) -> ResponseModel:
    count = await schema_column_service.delete(db=db, obj=obj)
    if count > 0:
        return response_base.success()
    return response_base.fail()

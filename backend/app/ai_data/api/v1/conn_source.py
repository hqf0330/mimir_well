from typing import Annotated

from fastapi import APIRouter, Depends, Path, Query

from backend.app.ai_data.schema.conn_source import (
    CreateConnSourceParam,
    DeleteConnSourceParam,
    GetConnSourceDetail,
    UpdateConnSourceParam,
)
from backend.app.ai_data.service.conn_source_service import conn_source_service
from backend.common.pagination import DependsPagination, PageData
from backend.common.response.response_schema import ResponseModel, ResponseSchemaModel, response_base
from backend.common.security.jwt import DependsJwtAuth
from backend.common.security.permission import RequestPermission
from backend.common.security.rbac import DependsRBAC
from backend.database.db import CurrentSession, CurrentSessionTransaction
from backend.database.db import CurrentSession

router = APIRouter()


@router.get('/{pk}', summary='获取数据源详情', dependencies=[DependsJwtAuth])
async def get_conn_source(
    db: CurrentSession, pk: Annotated[int, Path(description='数据源 ID')]
) -> ResponseSchemaModel[GetConnSourceDetail]:
    conn_source = await conn_source_service.get(db=db, pk=pk)
    return response_base.success(data=conn_source)


@router.get(
    '',
    summary='分页获取所有数据源',
    dependencies=[
        DependsJwtAuth,
        DependsPagination,
    ],
)
async def get_conn_sources_paginated(db: CurrentSession) -> ResponseSchemaModel[PageData[GetConnSourceDetail]]:
    page_data = await conn_source_service.get_list(db=db)
    return response_base.success(data=page_data)


@router.post(
    '',
    summary='创建数据源',
    dependencies=[
        Depends(RequestPermission('conn:source:add')),
        DependsRBAC,
    ],
)
async def create_conn_source(db: CurrentSessionTransaction, obj: CreateConnSourceParam) -> ResponseModel:
    await conn_source_service.create(db=db, obj=obj)
    return response_base.success()


@router.put(
    '/{pk}',
    summary='更新数据源',
    dependencies=[
        Depends(RequestPermission('conn:source:edit')),
        DependsRBAC,
    ],
)
async def update_conn_source(
    db: CurrentSessionTransaction, pk: Annotated[int, Path(description='数据源 ID')], obj: UpdateConnSourceParam
) -> ResponseModel:
    count = await conn_source_service.update(db=db, pk=pk, obj=obj)
    if count > 0:
        return response_base.success()
    return response_base.fail()


@router.delete(
    '',
    summary='批量删除数据源',
    dependencies=[
        Depends(RequestPermission('conn:source:del')),
        DependsRBAC,
    ],
)
async def delete_conn_sources(db: CurrentSessionTransaction, obj: DeleteConnSourceParam) -> ResponseModel:
    count = await conn_source_service.delete(db=db, obj=obj)
    if count > 0:
        return response_base.success()
    return response_base.fail()

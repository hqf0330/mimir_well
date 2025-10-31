from typing import Annotated

from fastapi import APIRouter, Depends, Path, Query

from backend.app.ai_data.schema.schema_table import (
    CreateSchemaTableParam,
    DeleteSchemaTableParam,
    GetSchemaTableDetail,
    UpdateSchemaTableParam,
)
from backend.app.ai_data.service.schema_table_service import schema_table_service
from backend.common.pagination import DependsPagination, PageData
from backend.common.response.response_schema import ResponseModel, ResponseSchemaModel, response_base
from backend.common.security.jwt import DependsJwtAuth
from backend.common.security.permission import RequestPermission
from backend.common.security.rbac import DependsRBAC
from backend.database.db import CurrentSession, CurrentSessionTransaction
from backend.database.db import CurrentSession

router = APIRouter()


@router.get('/{pk}', summary='获取Schema表元数据详情', dependencies=[DependsJwtAuth])
async def get_schema_table(
    db: CurrentSession, pk: Annotated[int, Path(description='Schema表元数据 ID')]
) -> ResponseSchemaModel[GetSchemaTableDetail]:
    schema_table = await schema_table_service.get(db=db, pk=pk)
    return response_base.success(data=schema_table)


@router.get(
    '',
    summary='分页获取所有Schema表元数据',
    dependencies=[
        DependsJwtAuth,
        DependsPagination,
    ],
)
async def get_schema_tables_paginated(db: CurrentSession) -> ResponseSchemaModel[PageData[GetSchemaTableDetail]]:
    page_data = await schema_table_service.get_list(db=db)
    return response_base.success(data=page_data)


@router.post(
    '',
    summary='创建Schema表元数据',
    dependencies=[
        Depends(RequestPermission('schema:table:add')),
        DependsRBAC,
    ],
)
async def create_schema_table(db: CurrentSessionTransaction, obj: CreateSchemaTableParam) -> ResponseModel:
    await schema_table_service.create(db=db, obj=obj)
    return response_base.success()


@router.put(
    '/{pk}',
    summary='更新Schema表元数据',
    dependencies=[
        Depends(RequestPermission('schema:table:edit')),
        DependsRBAC,
    ],
)
async def update_schema_table(
    db: CurrentSessionTransaction, pk: Annotated[int, Path(description='Schema表元数据 ID')], obj: UpdateSchemaTableParam
) -> ResponseModel:
    count = await schema_table_service.update(db=db, pk=pk, obj=obj)
    if count > 0:
        return response_base.success()
    return response_base.fail()


@router.delete(
    '',
    summary='批量删除Schema表元数据',
    dependencies=[
        Depends(RequestPermission('schema:table:del')),
        DependsRBAC,
    ],
)
async def delete_schema_tables(db: CurrentSessionTransaction, obj: DeleteSchemaTableParam) -> ResponseModel:
    count = await schema_table_service.delete(db=db, obj=obj)
    if count > 0:
        return response_base.success()
    return response_base.fail()

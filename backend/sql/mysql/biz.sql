drop table conn_source;
create table conn_source
(
    id                 bigint auto_increment primary key,
    name               varchar(255) not null comment '数据源名称',
    conn_type          varchar(50)  not null comment '数据源类型',
    host               varchar(255) not null comment '连接host',
    port               int          not null comment '端口',
    username           varchar(255) not null comment '账号',
    password_encrypted varchar(255) not null comment '密码',
    db_name            varchar(255) not null comment '数据库',
    status             tinyint(1)  not null comment '1：启用，0：不启用',
    created_time       datetime     not null comment '创建时间',
    updated_time       datetime     null comment '更新时间',
    constraint ix_dbconnection_name
        unique (name)
) comment '数据源';
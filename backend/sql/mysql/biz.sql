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
    status             tinyint(1)   not null comment '1：启用，0：不启用',
    created_time       datetime     not null comment '创建时间',
    updated_time       datetime     null comment '更新时间',
    constraint ix_dbconnection_name
        unique (name)
) comment '数据源';


# 表元数据
CREATE TABLE `schema_table`
(
    `id`            BIGINT       NOT NULL AUTO_INCREMENT COMMENT '主键 ID',
    `connection_id` BIGINT       NOT NULL COMMENT '关联数据源ID（外键: conn_source.id）',
    `table_name`    VARCHAR(255) NOT NULL COMMENT '表名',
    `description`   TEXT COMMENT '表描述',
    `ui_metadata`   JSON COMMENT 'UI元数据（表位置、颜色等）',
    `created_time`  DATETIME     NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
    `updated_time`  DATETIME              DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
    PRIMARY KEY (`id`),
    INDEX `idx_connection_id` (`connection_id`),
    INDEX `idx_table_name` (`table_name`),
    UNIQUE KEY `uk_connection_table` (`connection_id`, `table_name`),
    CONSTRAINT `fk_schema_table_connection` FOREIGN KEY (`connection_id`) REFERENCES `conn_source` (`id`) ON DELETE CASCADE
) ENGINE = InnoDB
  DEFAULT CHARSET = utf8mb4 COMMENT ='Schema表元数据';


# 列元数据
CREATE TABLE `schema_column`
(
    `id`                       BIGINT       NOT NULL AUTO_INCREMENT COMMENT '主键 ID',
    `table_id`                 BIGINT       NOT NULL COMMENT '关联表ID（外键: schema_table.id）',
    `column_name`              VARCHAR(255) NOT NULL COMMENT '列名',
    `data_type`                VARCHAR(100) NOT NULL COMMENT '数据类型（如: VARCHAR, INT, DATETIME）',
    `description`              TEXT COMMENT '列描述',
    `is_primary_key`           TINYINT(1)   NOT NULL DEFAULT 0 COMMENT '是否主键',
    `is_foreign_key`           TINYINT(1)   NOT NULL DEFAULT 0 COMMENT '是否外键',
    `is_unique`                TINYINT(1)   NOT NULL DEFAULT 0 COMMENT '是否唯一约束',
    `is_nullable`              TINYINT(1)   NOT NULL DEFAULT 1 COMMENT '是否可为空',
    `column_default`           VARCHAR(255) COMMENT '默认值',
    `ordinal_position`         INT COMMENT '列在表中的位置（排序用）',
    `character_maximum_length` INT COMMENT '字符最大长度（用于VARCHAR等）',
    `numeric_precision`        INT COMMENT '数值精度',
    `numeric_scale`            INT COMMENT '数值小数位数',
    `created_time`             DATETIME     NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
    `updated_time`             DATETIME              DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
    PRIMARY KEY (`id`),
    INDEX `idx_table_id` (`table_id`),
    INDEX `idx_column_name` (`column_name`),
    UNIQUE KEY `uk_table_column` (`table_id`, `column_name`),
    CONSTRAINT `fk_schema_column_table` FOREIGN KEY (`table_id`) REFERENCES `schema_table` (`id`) ON DELETE CASCADE
) ENGINE = InnoDB
  DEFAULT CHARSET = utf8mb4 COMMENT ='Schema列信息';

# 表关系
CREATE TABLE `schema_relationship`
(
    `id`                BIGINT   NOT NULL AUTO_INCREMENT COMMENT '主键 ID',
    `connection_id`     BIGINT   NOT NULL COMMENT '关联数据源ID（外键: conn_source.id）',
    `source_table_id`   BIGINT   NOT NULL COMMENT '源表ID（外键: schema_table.id）',
    `source_column_id`  BIGINT   NOT NULL COMMENT '源列ID（外键: schema_column.id）',
    `target_table_id`   BIGINT   NOT NULL COMMENT '目标表ID（外键: schema_table.id）',
    `target_column_id`  BIGINT   NOT NULL COMMENT '目标列ID（外键: schema_column.id）',
    `relationship_type` VARCHAR(50) COMMENT '关系类型（如: 1-to-1, 1-to-N, N-to-M）',
    `description`       TEXT COMMENT '关系描述',
    `created_time`      DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
    `updated_time`      DATETIME          DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
    PRIMARY KEY (`id`),
    INDEX `idx_connection_id` (`connection_id`),
    INDEX `idx_source_table` (`source_table_id`),
    INDEX `idx_target_table` (`target_table_id`),
    INDEX `idx_source_column` (`source_column_id`),
    INDEX `idx_target_column` (`target_column_id`),
    UNIQUE KEY `uk_source_target_columns` (`source_column_id`, `target_column_id`),
    CONSTRAINT `fk_schema_rel_connection` FOREIGN KEY (`connection_id`) REFERENCES `conn_source` (`id`) ON DELETE CASCADE,
    CONSTRAINT `fk_schema_rel_source_table` FOREIGN KEY (`source_table_id`) REFERENCES `schema_table` (`id`) ON DELETE CASCADE,
    CONSTRAINT `fk_schema_rel_source_column` FOREIGN KEY (`source_column_id`) REFERENCES `schema_column` (`id`) ON DELETE CASCADE,
    CONSTRAINT `fk_schema_rel_target_table` FOREIGN KEY (`target_table_id`) REFERENCES `schema_table` (`id`) ON DELETE CASCADE,
    CONSTRAINT `fk_schema_rel_target_column` FOREIGN KEY (`target_column_id`) REFERENCES `schema_column` (`id`) ON DELETE CASCADE
) ENGINE = InnoDB
  DEFAULT CHARSET = utf8mb4 COMMENT ='Schema表间关系';

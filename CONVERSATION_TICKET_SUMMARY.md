# Corrine 历史对话 Ticket 总结

这份文档根据 Cursor 历史对话整理，重点总结你做过、推进过、review 过或深入理解过的 Terminal Data Platform 相关工作。

总体来看，你这段时间的主线是：

- Data Platform 的数据质量检查，也就是 DQ / Data Quality。
- Spark、Flink、Kinesis、Iceberg、Athena、DynamoDB 这一套流批处理和数据湖架构。
- Query Engine、EMR Serverless、Elastic Beanstalk、SSM 等部署和运行时配置。
- Datadog、BetterStack、CloudWatch、Athena 等生产问题调查工具。
- 本地开发体验和新人 onboarding。

## 1. 实际推进或实现过的工作

### DP-173 / DP-288: Trigger DQ checks on new provider

历史对话：[DP-173 DP-288 SQS](7a8582a5-2a1a-4310-ba6b-d909581107f7)、[DP-173 DP-288 DQ](42a9af74-db7f-47ad-8254-ee26a2650f92)、[DP-173 Analyzer Design](c6b3fbe9-29c0-45ba-9747-8443c916f471)

这是你最核心的一条 Data Platform ticket。

目标是：当一个新的 provider 第一次完成 backfill 之后，自动触发 DQ checks，验证这个 provider 的数据质量，而不是依赖人工手动触发。

主要工作内容：

- 监听 `sync.completed` 事件。
- 判断这个 sync 是否属于新 provider 的首次 backfill。
- 用 Redis 记录哪些 `(provider, table)` 已经触发过验证，避免重复触发。
- 从最初的 TypeScript handler-only 方案，演进到 `EventBridge/Lambda -> SQS -> Java Spring listener -> Redis -> Spark/Temporal` 的架构。
- 清理过一批未使用的 Java controller/service/model/test 文件。
- 本地验证过 TypeScript handler、Java listener/handler、Spark service。
- 后续在 staging 遇到并排查过 SQS listener env var、Athena query、schema/provider mapping 等问题。

涉及技术栈：

- TypeScript Lambda
- SST/CDK
- EventBridge
- SQS
- Java Spring Boot / Query Engine
- `@SqsListener`
- Redis / Upstash / local Redis
- Spark jobs
- Athena / Iceberg
- Temporal 作为计划中的 workflow orchestration

这条 ticket 在 Terminal 架构里的位置：

- 它不在 provider integration 里。
- 它也不在 Flink realtime ingestion 的最前段。
- 它主要位于 Data Platform 的 DQ orchestration 层：事件监听、状态缓存、Spark DQ job 触发。

### DP-432: Fix timestamp clamping in consistency check

历史对话：[DP-432 Timestamp Consistency](14f088ad-193d-4b81-a450-45ef1c66c936)

目标是修复 consistency check 里的 timestamp 精度 bug。

问题背景：

- consistency check 会比较 stream count 和 Iceberg count。
- 旧逻辑会把 timestamp clamp 到秒级。
- 如果某些记录落在 sync end 的毫秒边界上，就可能被 Iceberg 查询漏掉。
- 结果是明明数据存在，consistency check 却报 count mismatch。

主要工作内容：

- 修改 `DateUtil`、`TimeCondition` 和 Athena repository SQL builder 相关逻辑。
- 保留 fractional seconds。
- 使用 inclusive bounds，确保 sync-end millisecond boundary 的记录被包含。
- 构建 query-engine bundle。
- 用 staging synthetic rows 做验证。
- 验证结果里 `streamCount=25`、`icebergCount=25`，说明修复生效。

涉及技术栈：

- Java
- Query Engine
- Athena SQL
- Iceberg
- DynamoDB sync count
- Lambda smoke test
- Elastic Beanstalk
- Maven tests

### DP-285: Move Spark artifact version to SSM

历史对话：[DP-285 SSM Plan](deda620d-b6a2-4ad3-a454-1814afde601d)

目标是把 `ARTIFACT_SPARK_VERSION` 从 Query Engine 的环境变量迁移到 AWS SSM Parameter Store。

主要工作内容：

- 修改 `stacks/DataPlatformArtifacts.ts`，定义或发布 Spark artifact version 参数。
- 修改 `stacks/SpringQueryEngine.ts`，让 Query Engine 不再直接依赖 env var。
- 修改 Query Engine `start.sh`，启动时从 SSM 读取 Spark artifact version。
- 让 Spark job artifact version 的配置路径更集中，减少环境变量漂移。

涉及技术栈：

- SST/CDK
- TypeScript infra stacks
- AWS SSM Parameter Store
- Spring Query Engine
- Bash startup script
- AWS IAM/SSO

状态：

- 代码改动完成。
- lint 通过。
- 完整 `pnpm typecheck` 当时被过期 AWS SSO 阻塞。

### AWS SSO onboarding script

历史对话：[AWS Config Onboarding](43b6f417-c789-4d2e-a3a5-6490d8cf1764)

目标是帮新人更容易配置 Terminal 的 AWS SSO profiles，避免手动编辑 `~/.aws/config`。

主要工作内容：

- 编写 `scripts/setup-aws-config.sh`。
- 支持 dev/staging/prod profiles。
- 更新 README / onboarding docs。
- 根据 Bugbot feedback 修复 login instruction，确保命令带 `--profile`。
- 最后提交并 push。

涉及技术栈：

- Bash
- AWS SSO
- AWS CLI profile config
- README / onboarding docs
- Git / PR workflow

## 2. Scoped / planned 的 tickets

这些不一定都是你完整实现的，但你参与了大量理解、拆解、设计和 scope 收敛。

### DP-348: AIO local setup with Doris

历史对话：[DP-348 Doris Local](855f8e7d-c99e-43b6-9335-bf4b6e063199)

目标是让 Data Platform 本地开发更像 all-in-one setup，减少对 AWS Glue/S3/Athena/DynamoDB 的依赖。

主要理解：

- 现在本地 data-processing setup 很重，需要 Flink、Spark、LocalStack、Query Engine 等多个组件。
- Iceberg 在本地很难完全模拟，因为依赖 Glue Catalog + S3 + Athena。
- DynamoDB sink 用 LocalStack 也不够稳定。
- 很多 Spark/DQ 验证不得不跑到 staging。
- Doris 可以在本地作为一个 OLAP 数据库，替代一部分 Iceberg/Athena/DynamoDB 的本地验证需求。

涉及技术栈：

- Docker Compose
- Apache Doris
- Flink connectors
- Spark jobs
- Query Engine config
- Iceberg
- DynamoDB
- Athena
- LocalStack

结论：

- 这不是 prod migration。
- MVP 应该聚焦于让一条本地 happy path 跑通，服务 onboarding 和 e2e testing。

### DP-322: Automate DQ investigation spike

历史对话：[DP-322 Automation Spike](22688b2c-14fc-4ab5-8c24-0ef8e1945777)

目标是自动化 DQ failure investigation。

设想流程：

- 从 Datadog 发现 DQ failure。
- 用 Athena/Iceberg 查询失败表、失败 check、影响范围。
- 拉 GitHub/code context 辅助判断。
- 生成 Slack-ready summary。
- 给出 priority/verdict。

涉及技术栈：

- Datadog MCP
- Athena MCP / AWS CLI
- Cursor Automations
- Claude scheduled tasks
- GitHub Actions
- `.cursor/skills/data-quality-investigation`

主要 blocker：

- 本地 AWS CLI 可用。
- Cursor Cloud agent 缺少 IAM/Athena access。
- Cloud catalog 当时缺少 Athena MCP。

### DP-349: PeriodChange false positive fix

历史对话：[DP-349 PeriodChange Fix](881d9441-90c3-4454-85e2-c9a686c5eda7)

目标是修复 `PeriodChange` DQ check 的误报。

根因理解：

- `analyzer_metrics` 有时是 sparse 的，不是每天都有一行。
- 当前 SQL 使用 `LAG(7)`。
- `LAG(7)` 表示往前第 7 行，不是 7 calendar days ago。
- 当数据稀疏时，它会拿错比较基准，导致 false positive。

涉及技术栈：

- Spark SQL
- Deequ DQ checks
- `period_change_verification.sql`
- `_verification_checks_macro.sql`
- Athena staging validation

结论：

- scope 收敛为只修 `PeriodChange`。
- `RollingDeviation` 的语义经确认后不改。

### DP-430: Add applicationId tags to EMR Serverless jobs

历史对话：[DP-430 EMR Tagging](f8b2b259-99cf-4273-9f74-a87cacdabfa6)

目标是给 EMR Serverless job runs 加 `applicationId` tag，方便成本归因。

主要判断：

- 这个 ticket 应该落在 `packages/data-processing/query-engine`。
- 关键实现位置可能在 `EmrServerlessClient2` 和 `StartJobRunRequest` 附近。
- 需要从 request context / MDC 里拿到 applicationId。

涉及技术栈：

- Java
- Query Engine
- EMR Serverless
- AWS tags
- MDC / RequestContext

### DP-454: Data Platform onboarding series

历史对话：[DP-454 Onboarding Series](df6174a6-7c0f-44f3-b97d-29a0ebef228c)、[Data Platform Onboarding](2f9ddf44-c4d7-4513-9cc6-5d40f9758efc)

目标是把 Data Platform onboarding 拆成一组可复用、可检查的 Linear tasks。

内容覆盖：

- Terminal 基础概念：provider、application、connection、sync、schema。
- Data Platform repo map。
- Flink / Spark / Query Engine 分别负责什么。
- Athena / Iceberg / S3 的数据查询路径。
- deployment 和 platform upgrade 的基本流程。
- 新人第一天应该如何跑通本地环境。

涉及技术栈：

- Data Platform docs
- Linear ticket design
- Athena
- Spark
- Flink
- Query Engine
- deployment workflow

### DP-313: Stop upserting DynamoDB REMOVE events into Iceberg

历史对话：[DP-313 CDC Deletes](077cb383-05c1-4cd5-97e0-ed3bd8201368)

目标是让 DynamoDB Streams 的 `REMOVE` event 不再被当作普通 upsert 写入 Iceberg。

主要理解：

- DynamoDB Streams 会发出 `INSERT`、`MODIFY`、`REMOVE`。
- 当前 Flink CDC pipeline 可能把 `REMOVE` 也转换成 record 写入 Iceberg。
- 这会让删除事件表现得像一条普通数据，可能污染下游分析。

涉及技术栈：

- Java Flink
- DynamoDB Streams
- Iceberg
- CDC
- `CommonModelsStreamingJob`
- `ChangeEventToDynamicRecordGenerator.java`

开放问题：

- 下游是否依赖 tombstone / `is_deleted` 语义。
- 是否已有 cleanup job 依赖这些删除记录。

### DP-376-style: Local data generator

历史对话：[Data Generator V1 Scope](3de68617-06a1-4e97-8609-1f357a5b2e3f)、[Data Generator Design](39a397dc-4a1b-4e54-a04e-184adf2fc325)

目标是做一个本地 realistic data generator，帮助本地验证 Flink/Spark/DQ。

设计方向：

- 生成 realistic fleet data。
- common model 数据，比如 `Vehicle`，写入 DynamoDB。
- time-series 数据，比如 `VehicleLocation`，写入 Kinesis raw stream。
- 支持 batch / paced / stream 模式。
- 用 `GenerationSession` / `GenerationProfile` 表达整体生成场景。

涉及技术栈：

- Java
- Picocli CLI
- protobuf
- Kinesis
- DynamoDB
- LocalStack
- Flink time-series job
- Spark DQ / materialization
- Doris 本地验证场景

## 3. Review / triage / incident 相关工作

### DP-293 and DQ PR reviews

历史对话：[DP-293 Review](9f9ab1a9-d679-4615-b0c5-8c231cf64485)、[PR 7330 Sync Mode](29548041-8142-47c4-9de8-458685f10ce6)、[PR-7888 DQ Review](b6494d47-fb9c-4d01-8ee0-82d7fdc9f102)

你 review 过几类 DQ/Spark SQL 相关 PR：

- `DP-293`: 给 `PeriodChangeCheck` 加 `minVolume`，减少 threshold change noise。
- PR `#7330`: 支持 DQ sync mode filter。
- PR `#7888`: 给 trips / HOS daily logs 增加 implausible implied speed checks。

关注点包括：

- SQL template 是否安全。
- filter value 是否需要校验。
- DQ threshold 是否有业务依据。
- Java `double` 生成的测试字符串是否稳定。
- YAML config 是否是 dead path。

涉及技术栈：

- Java
- Spark SQL
- Deequ analyzer/checks
- Pebble/Jinja SQL templates
- PR review

### DP-311: DynamoDB Streams VPC endpoint

历史对话：[DP-311 VPC Endpoint](b30b52a5-9ebd-4631-8d8f-629464fd4ac1)、[DP-311 Testing Plan](69f0c5f5-0106-4346-b917-bad9e12c93f5)

这是别人主做的 branch，但你参与理解和测试方案设计。

目标：

- 让 Flink CDC jobs 读取 DynamoDB Streams 时走 VPC endpoint。
- 减少或绕开 NAT Gateway 流量。

涉及技术栈：

- AWS VPC
- DynamoDB Streams interface endpoint
- Private DNS
- NAT Gateway
- Flink CDC
- CloudFormation exports
- SST/CDK
- CloudWatch metrics / VPC Flow Logs

### Intact backfill triage

历史对话：[Intact Backfill Triage](6760afe7-abb3-427c-931b-f4573ad53c0f)

相关 ticket / PR：

- `PNI-929`
- `PNI-928`
- PR `#7446`
- PR `#7458`

你帮助理解 Intact missing historical data 的 Slack thread。

主要结论：

- Motive connection 可能不是 missing data，因为 account 是 2026 年 1 月创建的。
- ISAAC historical files 已经 ingest。
- 问题更可能出在 backfill delivery 还没补发给客户。
- PR `#7446` 处理了未来 ISAAC first-sync gating。

涉及技术栈：

- Athena / Iceberg
- data delivery / backfill delivery
- Retool connection inspection
- ISAAC
- Motive

### Datadog / Kinesis / Query Engine investigations

历史对话：[Datadog MCP Setup](4c03e2a5-0dc1-429b-a7a1-7ef9c89b6b35)、[Datadog 4xx False Positive](7663dd6c-1484-4e90-9227-b08484c0be09)、[Kinesis Alert Triage](4f52a607-2292-4937-a592-0a65080e5be3)、[On-Call Runbook Incidents](edceace9-4d45-4c0c-8820-07849af113db)

你做过几类 production / on-call 相关调查：

- 设置和验证 Datadog MCP。
- 调查 DQ failures。
- 调查 Query Engine 4xx Code Orange alert。
- 证明某个 4xx monitor 是 aggregation false positive。
- 调查 Kinesis composite alert，包括 iterator age、GetRecords spike、read/write throughput exceeded。
- 梳理 Query Engine 5xx / 4xx / Kinesis alert 的 runbook。

涉及技术栈：

- Datadog MCP
- Datadog logs / monitors / dashboards / APM
- BetterStack
- AWS CloudWatch
- Kinesis metrics
- Elastic Beanstalk Query Engine
- Athena fallback queries
- nginx logs

### EBS / Spark args debug

历史对话：[EBS Spark Args Debug](b96a805d-9240-43e2-8c03-6a479ab5e655)

背景是 EBS platform upgrade `4.11.0` 期间，materialized Spark job 失败。

主要判断：

- 失败可能不是 Spark 业务逻辑本身。
- 更可能是 Spark job args parsing 问题。
- `--serverless true` 被当作 key/value 传入，但 picocli 把 `--serverless` 当作 boolean flag。
- 真正的 `ParameterException` 可能被 usage-only logging 隐藏了。

涉及技术栈：

- Query Engine
- EMR / Spark job router
- picocli
- `AbstractSparkJob.java`
- `SparkService.java`
- `vehicle-daily-distance-materialization`
- Elastic Beanstalk upgrade testing

## 4. 架构和概念学习

这些对话不一定对应一个 ticket，但它们构成了你对 Terminal Data Platform 的背景理解。

### Flink / RocksDB / Jackson incident

历史对话：[Flink Incident Learning](f2302508-6b7c-4bae-8662-060d674788bc)、[Flink RCA Context](fea5de45-30fe-414e-9ea4-f52852527249)

你学习和梳理了一个 Flink incident：

- Kinesis shards 部分未被读取。
- Flink jobs 不稳定。
- 表面上像 RocksDB bottleneck。
- 真实 root cause 是 Jackson version 升级错误，导致 SerDe 异常和 fallback，引发 CPU spikes。
- 修复包括 Jackson version 修正、sync counters 改内存结构、RocksDB bloom filter、compaction 调整等。

涉及技术栈：

- Flink
- AWS Managed Flink / KDA
- RocksDB state backend
- Jackson ObjectMapper / JSON SerDe
- Kinesis shards
- Bloom filter
- State TTL
- Deduplication window

### Common model vs time-series data

历史对话：[Flink Incident Learning](f2302508-6b7c-4bae-8662-060d674788bc)、[Iceberg/Flink Learning](9fd24457-06e6-4e41-bc00-e828d8ff0b86)

你梳理过 Terminal 里两类数据：

- common model data：车辆、司机、trip、device、trailer 等实体数据。
- time-series data：车辆位置、车辆 stats 等随时间不断产生的数据点。

架构区别：

- time-series 数据量大，走 Kinesis -> Flink dedupe -> Kinesis clean -> Flink time-series job -> DynamoDB/Iceberg。
- common model 通常有唯一 ID，先写 DynamoDB，再通过 DynamoDB Streams / Flink CDC 同步到 Iceberg。

涉及技术栈：

- Kinesis
- Flink
- DynamoDB
- DynamoDB Streams
- Iceberg
- Athena
- Spark DQ

### Iceberg / Flink commit contention

历史对话：[Iceberg/Flink Learning](9fd24457-06e6-4e41-bc00-e828d8ff0b86)

你学习过 Iceberg commit contention incident：

- Flink CDC jobs 和 Ryft/Spark compaction 同时写 Iceberg。
- Iceberg 使用 optimistic concurrency。
- 如果 metadata commit 冲突，Flink checkpoint/restart 会受影响。

涉及技术栈：

- Flink checkpoints
- Iceberg optimistic concurrency
- Glue Catalog
- S3 Parquet layout
- Avro `.avsc`
- Spark / Ryft compaction

## 5. 你接触最多的技术栈

### Data processing

- Java
- Maven
- Spark
- Flink
- Deequ
- Picocli
- Jackson
- RocksDB

### Data storage and query

- Iceberg
- Athena
- S3
- DynamoDB
- DynamoDB Streams
- Redis
- Doris

### AWS infrastructure

- EMR Serverless
- Elastic Beanstalk
- Kinesis
- SQS
- EventBridge
- SSM Parameter Store
- VPC endpoint
- NAT Gateway
- CloudWatch

### Terminal repo infrastructure

- SST/CDK
- Pulumi for Data Platform infra
- TypeScript Lambda
- Spring Boot Query Engine
- LocalStack
- Docker Compose

### Observability and operations

- Datadog MCP
- Datadog logs / APM / monitors
- BetterStack
- Retool
- Athena investigation queries

## 6. 一句话总结

你做过的工作可以概括为：

> 你主要在 Terminal 的 Data Platform 上工作，围绕 DQ automation、Spark/Flink 数据处理、Query Engine 配置、AWS infra、本地开发体验和生产问题排查，做过实现、scoping、PR review 和 incident investigation。

更具体一点：

- `DP-173 / DP-288` 是你的主项目：自动触发新 provider 的 DQ checks。
- `DP-432` 是一个典型的深水区 bug fix：timestamp 精度影响 Athena/Iceberg consistency count。
- `DP-285` 是 deployment/config cleanup：把 Spark artifact version 迁到 SSM。
- `DP-348`、`DP-322`、`DP-349`、`DP-430`、`DP-454` 是你参与拆解和规划的数据平台改进。
- `DP-293`、`DP-311`、PR `#7330`、PR `#7888` 等体现了你参与 code review 和架构理解。
- Datadog/Kinesis/Query Engine/Flink incident 相关对话体现了你已经接触 production operations 和 on-call debugging。

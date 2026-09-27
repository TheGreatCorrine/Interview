### Tell me about yourself

### Why this role/team/company


### Data Engineering Concepts
1. How's Terminal (first sync) relevant to Data Ingestion?
   - the project itself
   - how are they relevant
My previous experience has been more on the software and platform engineering side rather than pure data engineering, but there's quite a bit of overlap with this role.
In my most recent internship, I worked in an existing distributed system and implemented backend logic around a backfill workflow. That required me to understand how data moved through an existing codebase, how different components interacted, and how we handled things like duplicate processing and historical data.
I also had some exposure to PySpark through a separate historical backfill and to a Flink CDC issue. So I wouldn't say I've built a data platform from scratch, but I've worked with several of these concepts in production, and I'm interested in understanding the data engineering side more deeply.



2. GCP
   - I do have some hands-on exposure to GCP. I used it for a hackathon about a year ago, and I'm familiar with the basic concepts.
   - Most of my cloud experience is with AWS, though. I've been using AWS pretty extensively for about three years, including in production during my internships. I've worked with Lambda, SQS, S3, DynamoDB, Athena, and a few other services. So I'm pretty comfortable with cloud concepts in general.
   - I haven't had the chance to use GCP in production yet, but I think a lot of the concepts carry over. And honestly, that's part of why I'm interested in this role. I really enjoy working with cloud technologies, but I don't want all of my experience to be limited to AWS.
   - If I were selected for the role, I'd definitely spend some time before the internship getting more comfortable with GCP. I'd probably build a small project with the services the team uses
   - **AWS EMR ↔ Google Cloud Dataproc**
   - **S3 ←→ Cloud Storage**
  
3. File formats (AVRO / ORC / Parquet)
   1. `.csv`, `.json` `.parquet` 文件格式
   2. Unlike `csv`, which is row-oriented, parquet is **binary** **column-oriented**
   3. so when you query, read only the columns you need. -> **Column pruning**
   4. encode/compress similar data -> **Good compression**
   5. parquet has type/schema

   `.avro`: `.csv` data types have to be inferred, avro is defined by schema (written in JSON)

   Exposure: I haven't directly worked with Avro or ORC in production, so my understanding of those is more conceptual. I understand why formats like Avro are useful compared with something like JSON — they're binary, support schemas, and are more efficient for large-scale data systems. I've worked more directly with formats like CSV and JSON.
I originally started learning about these data formats because I was working around Iceberg and Athena in my previous internship, so I wanted to understand how the actual data files underneath a table are stored. That's also how I became more familiar with Parquet and columnar storage.

   I haven't worked with Parquet directly at a low level. I first learned about it when I was trying to better understand Iceberg, which I worked around in my previous internship. I learned that Iceberg is a table format that manages the underlying data files in object storage like S3, and those data files can be stored in formats like Parquet. So that's how I became familiar with Parquet and columnar storage.

5. Spark
   - Terminal
   - PySpark
   - Concepts
     Apache Spark is a unified computing engine for parallel data processing.


6. Distributed systems
   replication、fault tolerance、consistency、distributed computation


7. Shell / CI

8. Python
   最熟悉的，my computer science mother language
   live coding, building ETL, write scripts, BSH raspberry pi python, ...
   sentiment analysis


9. Questions to ask
   是否主要工作是写automation scripts
   最终到gcp，然后可以用athena去query

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
   - I do have some experience with GCP. I used it for a hackathon about a year ago, so I'm familiar with the basics, but most of my cloud experience is with AWS.
   - I've been using AWS for about three years now, including pretty extensively in production. And I feel like once you have AWS on your resume, somehow every role after that also involves AWS. [laugh]
   - I'd love to branch out a little and get deeper experience with GCP. A lot of the core concepts carry over, so I don't think I'd be starting from scratch.
   - And if I joined the team, I'd definitely spend time before January getting more hands-on with the GCP services you use, probably through a small project.
   - **AWS EMR ↔ Google Cloud Dataproc**
   - **S3 ←→ Cloud Storage**
   - **Athena ↔ BigQuery**
   - **DynamoDB ↔ Bigtable**
   - **Iceberg: table format, organizes files as a table**
  
3. File formats (AVRO / ORC / Parquet)
   1. `.csv`, `.json` `.parquet` 文件格式
   2. Unlike `csv`, which is row-oriented, parquet is **binary** **column-oriented**
   3. so when you query, read only the columns you need. -> **Column pruning**
   4. encode/compress similar data -> **Good compression**
   5. parquet has type/schema

   `.avro`: `.csv` data types have to be inferred, avro is defined by schema (written in JSON)

   Exposure: I think my understanding is more conceptual. I understand why formats like Avro are useful compared with something like JSON — they're binary, support schemas, and are more efficient for large-scale data systems. I've worked more directly with formats like CSV and JSON.
I originally started learning about these data formats because I was working around Iceberg and Athena(BigQuery) in my previous internship, so I wanted to understand how the actual data files underneath a table are stored. That's also how I became more familiar with Parquet and columnar storage.

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
   Python is probably my most comfortable language. I sometimes joke that it's basically my mother programming language. I've been using it for around four years, for everything from backend development and scripting to PySpark and ML projects. I also used it pretty heavily at BSH on a Raspberry Pi application. So yeah, Python is definitely the language I'm most comfortable picking up and building something with.

9. Scala
    I haven't written Scala code directly. My previous team had some existing Spark jobs written in Scala, so I've read through Scala code at work and I'm somewhat familiar with what it looks like. But I didn't personally modify those jobs.
The Spark code I worked on directly was in PySpark, for a historical backfill. So I'd say I have some exposure to Scala, but my hands-on Spark experience is mainly with PySpark.

10. Questions to ask
   From the job description, it sounds like the team works with data moving between legacy systems and the cloud. I was also curious what the day-to-day engineering work looks like. Is it mostly scripting and automation, or would I also get to work on data pipelines or larger components of the platform?

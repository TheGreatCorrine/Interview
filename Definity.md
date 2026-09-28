### Tell me about yourself
Sure! I’m a fourth-year student at U of T doing a double degree in Computer Science and Rotman Commerce.

I actually got into software through a part-time work-study role at U of T’s business school. I worked on a financial education platform used by all undergraduate business students.

After that, I did three software engineering internships. My first one was more full-stack. Then I worked on a Python-based AI backend system, and that was also where I got more exposure to cloud infrastructure and DevOps.

I just wrapped up my most recent internship as a data platform engineer. We were processing terabytes of data from over 200 external providers and mapping it into our internal data models. I was on the data platform team, working mainly on backend and data-related systems, including things like data validation, backfills, and distributed processing.

That’s actually why this role stood out to me. It feels like a natural extension of my previous experience, and with more exposure to data engineering and GCP.
So yeah, that’s a quick overview of my background. I’d be happy to go into more detail on any of those experiences.

### Why this role/team/company
Honestly, when I first saw the job description, I got pretty excited because it felt so close to what I’d been doing in my last internship. So seeing a role that would let me go deeper into data engineering felt like a really natural next step.

I was also really excited about the GCP part. Most of my cloud experience has been with AWS — I always joke that once you have AWS on your resume, somehow every job after that also involves AWS. So I’ve actually been looking for a chance to branch out and work more deeply with another cloud platform.
I was honestly a little worried I wouldn’t get an interview, so I even reached out to the recruiter（lipsa.thakur@definity.com）on LinkedIn after I applied. So yeah, I was genuinely really happy when I got the interview.

corporate values:
- We are all owners — 强调 accountability、ownership，以及做有判断力的决策。
- We inspire customer confidence — 强调解决客户和 business 的真实问题、建立信任。
- We work together to win together — collaboration、respect、learning from each other

### Data Engineering Concepts
1. Spark
   Yeah, I used Spark quite a bit in my last internship. We had a **local Spark** environment running in Docker for development, and we also submitted Spark jobs to **EMR** for larger data quality checks. I used the **Spark UI** to inspect and monitor jobs as well.
On the code side, I read through some of our existing Spark logic written in Scala, although I didn’t directly modify the Scala code. My more hands-on coding experience was with PySpark, where I worked on a historical backfill.

// 
   Yeah. I used PySpark for a historical backfill in my last internship. We needed to reprocess some historical data。
  I worked closely with a large data ingestion system. There was another team that owned more of the upstream ingestion work.
  I first noticed the issue through an Athena query. For one provider, Samsara, some of the g-force fields were unexpectedly missing.
  My instinct was the provider-specific mapping was wrong, so I looked into the Java mapping code, but that looked correct. Then I checked the corresponding records in DynamoDB and found that the source values were actually there.
  That helped me narrow the issue down to the path between DynamoDB and Iceberg. I traced it into our Flink CDC pipeline and found a JavaBean naming convention issue during deserialization.
<img width="684" height="264" alt="Screenshot 2026-09-23 at 20 18 59" src="https://github.com/user-attachments/assets/bfb7a605-b05b-4f7a-bdbc-1d8d8d295c07" />

  Pyspark historical backfill counts: pretty ETL style 读取受影响的历史数据 → 根据正确逻辑补齐/重建缺失字段 → 写回 Iceberg



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

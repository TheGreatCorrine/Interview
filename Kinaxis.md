# HR Call

### 1. Tell me about yourself
Sure! I’m a fourth-year student at U of T doing a double degree in Computer Science and Rotman Commerce.

I actually got into software through a part-time work-study role at U of T’s business school. I worked on a financial education platform used by all undergraduate business students.

After that, I did three software engineering internships. My first one was more full-stack. Then I worked on a Python-based AI backend system, and that was also where I got more exposure to cloud infrastructure and DevOps.

I just wrapped up my most recent internship as a data platform engineer. Most of my work was on backend services for data ingestion and integration. We were processing terabytes of data from over 200 external providers and mapping it into our internal data models.

That’s actually what made this Kinaxis role stand out to me. The Data Ingestion team sounds very close to the kind of work I enjoyed most in my last internship.

So yeah, that’s a quick overview of my background. I’d be happy to go into more detail on any of those experiences.



BSH: global home appliance (uh-PLY-uhns)

related to the job:

Technologies I worked with: Python, Java, JavaScript

### 2. Why Kinaxis
What stood out to me was the **Data Ingestion team**. In my most recent internship, I really enjoyed working on backend platform and data integration problems, so when I saw that this team is building infrastructure to move data in and out of the Kinaxis platform at scale, it felt very closely aligned with the kind of engineering I want to continue doing.
One thing that stood out to me about Kinaxis is actually the way you treat interns. I looked into some of the previous co-op experiences, and it seems like interns here get to work on real product and engineering problems rather than just small side projects.
At this point, since I’ve already done a few software internships, that’s really what I’m looking for. I want to spend a longer term getting deeper into a mature codebase and actually owning meaningful work.

I also think Kinaxis is interesting to me personally because it sits at the intersection of technology and business. I came into CS from a business background, so working on software that solves real enterprise and supply-chain problems is something I’d genuinely like to learn more about.

get out of: depth, ownership, learn from experienced engineers.
### 3. Eligibility
8- or 12- month? Yes. I’m currently based in Toronto for school, but I’d be comfortable relocating to Ottawa.
Graduate? Currently, it's Dec 2027 if I take an eight-month internship. And I could extend my graduation to Apr 2028 if needed for a twelve-month internship

### BQ
1. Teamwork
2. Strength/Weakness
3. Difficult person

[strength]
I'd say one of my biggest strengths is that I learn quickly, especially when I'm entering a new technical area. I came into CS from a business background, I was originally studying both. so I've had to get comfortable ramping up fast. 
In my last internship, the team was originally looking for master's students, and I joined a pretty complex data platform team where the systems and codebase were new to me. 
What works for me is understanding the big picture first, then breaking things down and learning each part. I also spend some time outside work reading docs or doing small practice projects. That helped me ramp up quickly, and by my third month, I was working on one of my first larger features pretty independently.

[weakness]
Asking for help earlier.
Sometimes I hesitate to bother other people, especially when everyone is busy. My first instinct is usually to spend more time trying to figure things out on my own because I feel like I should be able to learn it myself.
But my manager gave me really helpful feedback during my last internship. He told me that sometimes the problem isn’t that I haven’t tried hard enough — it’s that I simply don’t have the context yet.
That changed how I think about asking questions. Now, I still try to investigate things on my own first, but if I realize I’m missing context or spending too long in one direction, I ask earlier instead of just putting more hours into it.

[difficult]
I usually try not to think of someone as a difficult person. 
Most of the time, it’s more about different working or communication styles.
I’d first try to understand where the friction is coming from, then adjust how I communicate and make expectations clearer. If it still affects the work, I’d address it directly and respectfully rather than letting it build up.

一般不会选difficult person
One example was during a group project at school. We had one teammate who was frequently late to meetings, would leave early, and sometimes became completely unresponsive when we were getting close to deadlines.
We first tried reaching out to him directly and asking if there was anything going on or anything we could do to help, but we didn’t really get much response. After that, we asked our teaching assistant to help us contact him, and we also made it clear that we really wanted him to contribute, but if the situation continued, we would have to reflect it honestly in the peer evaluation.
Eventually, when we still couldn’t reach him consistently, we redistributed his remaining work across the rest of the team. At that point, our priority was making sure the group could still finish the project on time.
We did complete the project, and when we submitted the peer evaluation, we were honest about what had happened and each person’s contribution. I think what I learned from that experience is to communicate directly first and give people a fair chance, but also know when you need to escalate and protect the rest of the team.

[teamwork]
clear mutual goal and motivation

[conflicts]

[ambiguites] - [challenging project]


## Technical Interview
### Leetcode



Resume Deep Dive:
- three layer deduplication
### ETL

  Professionally, I worked with data ingestion and backfill workflows using Spark and Flink. I also had some earlier academic experience building a Python data preprocessing pipeline.
  I worked closely with a large data ingestion system. There was another team that owned more of the upstream ingestion work.
  I first noticed the issue through an Athena query. For one provider, Samsara, some of the g-force fields were unexpectedly missing.
  My instinct was the provider-specific mapping was wrong, so I looked into the Java mapping code, but that looked correct. Then I checked the corresponding records in DynamoDB and found that the source values were actually there.
  That helped me narrow the issue down to the path between DynamoDB and Iceberg. I traced it into our Flink CDC pipeline and found a JavaBean naming convention issue during deserialization.
<img width="684" height="264" alt="Screenshot 2026-09-23 at 20 18 59" src="https://github.com/user-attachments/assets/bfb7a605-b05b-4f7a-bdbc-1d8d8d295c07" />

  Pyspark historical backfill counts: pretty ETL style 读取受影响的历史数据 → 根据正确逻辑补齐/重建缺失字段 → 写回 Iceberg
  Extract：从 source table / storage 读历史数据
  Transform：修复、清洗、重算字段
  Load：把修好的数据写回目标表

  Take a NLP course one year ago.

- Docker
  AIO Local Setup
- Kubernetes: autoscale containerized across multiple servers
  docker: 把app装进container；kubernetes：管这些containers；helm：把怎么部署这些盒子的kubernetes配置打包（Helm is basically a package manager and templating tool for Kubernetes）
- kinesis, data streaming real-time event data

### React
  React app 由 Reusable components组成，组件接收 props，维护自己的 state，然后根据 state render UI
  I used React and Next.js more heavily in an earlier full-stack internship, where I worked on an internal HR management system with features like authentication, role-based access control, and timesheets. My more recent internships have been much more backend and data focused, so React isn't my strongest stack today, but I'm comfortable working in an existing React codebase and picking it back up when needed.
  


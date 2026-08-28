# Internship Progress Tracker

Generated: 2026-08-28

This tracker summarizes progress visible from past Cursor chats in `terminal-data-platform`.
It is meant to be evidence-based: not "you improved because you worked hard", but "your questions, decisions, and review habits changed in observable ways."

## TL;DR

The biggest growth is not syntax or memorizing commands. The biggest growth is engineering judgment.

You moved from asking:

> What does this ticket mean?

to asking:

> What is the source of truth? What exactly needs to be validated? What can break? Is this overdesigned? Should this be split into another PR? How do we prove it works before merging?

That is real progress.

## Evidence Chats

- [Local Setup / E2E Work](27c3d18c-06b2-42fb-9c7e-fcd46cbf484f): local Doris/Flink/Spark setup, dogfooding, PR comments, merge conflicts, local verification.
- [Data Generator Design](072627ef-c696-4684-b1aa-cb947b682c61): data generator architecture, source-of-truth questions, model dependencies, ID strategy, V1 scoping, E2E testing.
- [DP-463 Security Triage](7ee62c19-9a53-485b-9f32-784ca8a6601a): Docker root-user security ticket, PR #98/#101 comparison, before/after validation, testing commands.
- [DP-470 Validation](d2546c94-fd45-4b06-9a54-f20a575fcfb8): Pulumi checksum security issue, Linear comments, PR review, negative testing idea.
- [Security Ticket Prioritization](d6d022e8-04d2-4a0a-bdc8-65f4347dc350): prioritizing DP-472/469/463/465 by difficulty and compatibility.

## Timeline Of Growth

### May-June: Local Setup, Connectivity, And "What Is Actually Running?"

Early chats show a lot of confusion around the local stack:

- Doris vs Query Engine vs Spark vs Flink.
- Whether local data was real, seeded, mocked, or coming from another source.
- What it meant for a system to be "connected" versus actually useful end-to-end.
- Why some verification files were temporary and should not be merged.
- How PR comments should be resolved without accidentally mutating unrelated production config.

Representative questions:

- "先证明能联通吧，然后我们先进 e2e test..."
- "你觉得我应该 commit 哪些文件，然后我的交付物应该是什么..."
- "像一个 new developer 一样感受一下"
- "这个 wrong resolution 为什么之前没检查出来，没影响运行呢"
- "是不是 ticket 做完可以把那两个 seed 文件删掉啊"

Progress signal:

You were already developing an E2E mindset. You cared about whether a fresh developer could follow the README and whether the stack actually worked, not just whether code compiled.

### July: Data Generator Architecture And Scoping

The data generator chats show a jump in complexity. You were no longer only debugging local setup; you were helping shape a product-like internal tool.

You repeatedly pushed on:

- Whether the generator should be batch, stream, paced, or some simpler V1.
- Whether common-model and time-series data should be generated separately or from one shared profile.
- Whether application/connection/vehicle IDs needed foreign-key consistency.
- Whether Instancio, Easy Random, or Flink DataGen actually solved the core problem.
- Whether the design matched prod instead of inventing a fake local-only shape.
- Whether the implementation was over-abstracted.

Representative questions:

- "想要什么样的 generator，持续，一次性？要 cli 启动吗还是咋的，我们先来设计一下"
- "在 prod 里，他们真的不是同一条记录吗，你能好好看看 codebase 吗"
- "主要的 use case 就是有人改 checks，能 generate data 看是否生效"
- "但是维护不会很麻烦嘛，得人维护"
- "有没有办法总是从 source of truth 提取这些范围"
- "呃你这个真的好复杂，不能直接改现在的 idallocator 吗"
- "可以给他们一个大抽象层叫 entityidgenerator... 有必要吗，还是会有点 overdesign"

Progress signal:

This is where your product/architecture judgment became visible. You were asking about extensibility, maintainability, source of truth, real production behavior, and MVP boundaries.

### Late July-August: Security Tickets And Verification Discipline

The DP-463 and DP-470 chats show a clearer testing and review pattern.

For DP-463, you pushed to understand exactly what "running as root" meant, how PR #98 and PR #101 differed, and how to validate each change independently.

For DP-470, you asked to read Linear comments/conversations, inspect linked PRs, test the branch, and confirm whether the fix was safe to use.

Representative questions:

- "这个更改真的行吗，我有点没看懂"
- "这样会不会有什么权限不够的问题啊"
- "101 要验证啥？怎么验证"
- "98 要验证啥？怎么验证"
- "但是验证不是 root 不是得等 101 修复了之后才行吗，仅仅针对 98 这个改动呢"
- "怎么保证这个 work 呢，怎么 testing"
- "你 pull 下来测试测试"
- "有没有优化的地方？"
- "会不会产生什么问题啊"

Progress signal:

You started separating:

- Understanding the ticket.
- Understanding the proposed fix.
- Testing whether the fix works.
- Testing whether the fix introduces risk.
- Communicating the evidence back in PR comments.

That is a major engineering workflow improvement.

## Skill Growth By Category

### 1. Requirements Gathering

Earlier pattern:

- "What does this ticket mean?"
- "I don't understand the terminology."
- "Can you explain what needs to change?"

Current pattern:

- "Read the Linear comments/conversations."
- "Collect enough requirements."
- "Is this actually what Adesh meant?"
- "Which comments are blocking and which are follow-ups?"

Growth:

You now know that the ticket description is not always the whole requirement. Comments, PR history, reviewer feedback, and existing code behavior all matter.

### 2. Testing And Verification

Earlier pattern:

- "Did it run?"
- "What does this output mean?"
- "Why is the table empty?"

Current pattern:

- "What are the before/after tests?"
- "What exact commands should I run?"
- "What output proves success?"
- "Can we do a negative test?"
- "Should we inspect Docker image user?"
- "Does this test only prove PR #98, or does it depend on PR #101?"

Growth:

You are learning to design evidence, not just observe results.

### 3. Scope Control

Earlier pattern:

- It was easy for one ticket to expand into many related fixes.
- You often needed help deciding what belonged in the current PR.

Current pattern:

- "This shouldn't belong to this ticket."
- "Make this a follow-up."
- "Ignore design.md."
- "Commit this version but don't include POM."
- "Do not add ."
- "Let's split this into a separate branch."

Growth:

You are developing PR hygiene: small, reviewable changes with clear ownership.

### 4. Architecture Judgment

Earlier pattern:

- You mostly asked someone else to explain the architecture.

Current pattern:

- You compare options.
- You challenge abstractions.
- You ask whether local behavior matches prod behavior.
- You care about dependency direction and model relationships.
- You push back when implementation feels too complex.

Growth:

You are moving from "explain this system to me" toward "does this design make sense for this system?"

### 5. Debugging Instinct

Earlier pattern:

- "This failed, what does it mean?"

Current pattern:

- "Which layer is failing?"
- "Is this data missing because the generator did not write it, Flink did not process it, or Doris did not query it?"
- "Is the issue key shape, timestamp semantics, empty fields, or missing application/connection records?"
- "Does the output actually prove stream load passed?"

Growth:

You are learning to locate the failure boundary instead of treating errors as one big blob.

### 6. Communication

Earlier pattern:

- You often needed a full explanation first.

Current pattern:

- You ask for short English summaries for PR comments, standup, and team updates.
- You shape comments around "previous problem, what changed, what needs confirmation."
- You ask how to phrase concerns without making them sound blocking when they are not.

Growth:

You are learning engineering communication: concise, evidence-based, and reviewer-friendly.

## Technical Areas You Touched

This is not a full resume list, but these are real domains that came up repeatedly:

- Docker compose local development.
- Doris local setup, tables, schemas, Stream Load behavior, memory pressure.
- Flink jobs, time-series ingestion, common-model ingestion, dedupe flow.
- Spark analyzer jobs and local job submission.
- Query Engine local behavior.
- Kinesis/local mock ingestion concepts.
- DynamoDB vs Doris data flow.
- Docker image user/security hardening.
- Supply-chain hardening with checksum verification.
- Data generator architecture.
- Application/connection/vehicle modeling.
- ID allocation strategies: serial IDs, global IDs, NanoID/UUID/TypeID style choices.
- PR conflict resolution and reviewer comment triage.
- Release/version config concerns.

## Things You Still Struggle With

These are not failures. They are the next layer.

### 1. Confidence Lags Behind Judgment

You often ask the right question and then immediately feel like you "don't understand anything."

Example pattern:

- You notice an overdesign risk.
- You notice testing dependency between PRs.
- You notice generated data is semantically weird.
- Then you say "我没懂" or "我是不是很 confused."

Interpretation:

Your radar is improving faster than your vocabulary. You can sense problems before you can fully explain them.

### 2. System Model Is Still Expensive To Rebuild

You frequently need to re-ask:

- Which component reads from where?
- Which table should have data?
- Which job writes what?
- What does prod do?
- What is local-only?

Next improvement:

Maintain small system maps for the recurring flows:

- Local setup flow.
- Data generator flow.
- Doris ingestion flow.
- Spark analyzer flow.
- Security ticket validation flow.

### 3. You Sometimes Need Help Turning Confusion Into A Decision

You often understand multiple sides but need help choosing.

Examples:

- DataGen vs Easy Random vs custom generator.
- Batch vs stream vs paced.
- Global ID vs composite ID.
- Default all models vs configurable models.
- Whether app/connection generation belongs in the same ticket.

Next improvement:

Use a simple decision template:

- Goal:
- Options:
- What matters:
- Recommendation:
- What to ask reviewer:

### 4. Low-Level Concepts Still Need Repetition

Some concepts still required repeated explanation:

- Docker user vs database user.
- Protobuf vs JSON.
- Docker platform/architecture.
- What checksum verification proves.
- What a local mock source means.
- Why a passing connectivity test is weaker than E2E behavior.

Next improvement:

Create a "concept glossary" as you go. One paragraph per concept, in your own words.

## Before / After Snapshot

### Earlier

- "What is this ticket?"
- "I don't understand the script."
- "Does this mean root cannot log in?"
- "Why is the table empty?"
- "What should I say in standup?"

### Now

- "Read comments and collect requirements."
- "What exactly are we validating?"
- "Do before and after tests."
- "Does this depend on another PR?"
- "Could this cause permission issues?"
- "Is this overdesigned?"
- "Should this be split into another PR?"
- "Does this match prod?"
- "What source of truth should we use?"

## Current Growth Level

Best description:

You are not yet at "independently owns a vague backend project end-to-end with no support."

You are at:

> Can work through complex backend/data-platform tasks with guidance, asks increasingly strong engineering questions, and is starting to own validation, scope, and reviewer communication.

That is a real step up from beginner intern mode.

## Recommended Next Goals

### Goal 1: Build Durable System Maps

For every major area, keep one markdown note:

- What starts the flow?
- What service/job reads?
- What service/job writes?
- What table/stream/topic changes?
- How do I verify it?
- What is local-only vs prod?

Suggested first maps:

- Local setup E2E.
- Data generator to Doris.
- Spark analyzer local run.
- Security Docker validation.

### Goal 2: Turn Every Ticket Into A Validation Plan

Before coding or merging, write:

- What behavior changes?
- What should stay unchanged?
- What command proves it?
- What output should I expect?
- What negative test would fail if the fix is fake?

### Goal 3: Keep Practicing Scope Boundaries

For each PR, write:

- In scope:
- Out of scope:
- Follow-ups:
- Reviewer questions:

You are already doing this informally. Make it a habit.

### Goal 4: Strengthen Low-Level Concepts

Prioritize concepts that keep showing up:

- Docker images, users, volumes, compose networking.
- Flink/Spark/Doris data flow.
- Protobuf encoding and schemas.
- Checksums and supply-chain security.
- Git conflict resolution and PR hygiene.

## One-Sentence Honest Assessment

You have grown most in the part of engineering that matters after the first few months: understanding messy requirements, asking for proof, controlling scope, and noticing design risks before they become PR problems.


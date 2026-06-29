# Launch Kit

This file collects post-release copy and distribution notes for the first public launch.

## Positioning

Agent Governance Workbench is a local-first dashboard and template kit for safer AI agent workflows.

It is not an agent framework. It is an operating layer for handoffs, approval gates, risk registers, result cards, and privacy-first release checks.

## Assets

- Dashboard screenshot: `docs/assets/dashboard-screenshot.png`
- Social preview image: `docs/assets/social-preview.png`
- Editable synthetic preview: `docs/assets/dashboard-preview.svg`

All assets use bundled synthetic data only.

## English Short Post

I published Agent Governance Workbench, a local-first dashboard and template kit for safer AI agent workflows.

Most tools help you build agents. This repo focuses on the operating layer around them: owners, handoffs, risk levels, approval gates, evidence-backed result cards, and privacy checks before public release.

It runs locally with synthetic demo data and no external APIs.

GitHub: https://github.com/yohojj/agent-governance-workbench

Feedback is very welcome, especially from people coordinating multi-agent coding, research, or content workflows.

## 中文短帖

我发布了一个小型开源项目：Agent Governance Workbench。

它不是新的 Agent 框架，而是一个本地优先的治理工作台，用来管理多 Agent 工作流里的任务交接、风险分级、人工审批、结果卡和发布前隐私检查。

适合那些已经开始用 AI agent 做研究、代码、内容流程，但还缺少“谁负责下一步、哪些动作要审批、完成结果有没有证据、哪些信息不能公开”的轻量规则的人。

项目使用虚构演示数据，不需要外部 API。

GitHub: https://github.com/yohojj/agent-governance-workbench

欢迎反馈，尤其是你已经在协调多 Agent 工作流、内容生产流程或 AI 自动化流程的话。

## Hacker News / Reddit Style

I built a small local-first workbench for AI agent governance.

The question I kept running into was not only "how do I build an agent?" but "how do I operate a group of agents without losing ownership, approval boundaries, or evidence?"

The repo includes:

- A Streamlit dashboard with synthetic task queues
- Agent operating roles
- Risk register examples
- Approval-gate templates
- Handoff and result-card templates
- Release gates and a small privacy scanner

It is intentionally lightweight: no external APIs, no production claims, no real data.

Repo: https://github.com/yohojj/agent-governance-workbench

I would appreciate feedback on the governance model and what templates would be useful next.

## Product Hunt Maker Comment

Hi Product Hunt,

I built Agent Governance Workbench as a lightweight operating layer for AI agent workflows.

Most agent tools focus on building or running agents. I wanted something smaller and more practical for day-to-day coordination: who owns the task, what risk level it has, whether a human approval gate is needed, and what evidence should be attached before calling the work complete.

The first version includes a local Streamlit dashboard, synthetic examples, handoff/result-card/approval templates, release gates, and a privacy scanner.

It is MIT licensed and runs locally without external APIs.

I would love feedback from builders, AI workflow operators, and people coordinating research, coding, or content workflows with agents.

## 3-Day Launch Rhythm

### Day 1

- Pin the repository on the GitHub profile.
- Add the social preview image in GitHub repository settings.
- Share the English short post on X or LinkedIn.
- Share the Chinese short post on a suitable Chinese developer or AI community.

### Day 2

- Post the Hacker News / Reddit style version where relevant.
- Respond to feedback with concrete examples rather than promotional replies.
- Improve one README section if a reader asks a repeated question.

### Day 3

- Publish one small follow-up improvement from the open issues.
- Comment on the release with what changed.
- Share a short update: "Added X based on feedback."

## Do Not Do

- Do not ask people to star the repo directly.
- Do not ask for Product Hunt upvotes directly.
- Do not claim adoption, downloads, benchmarks, or community traction that does not exist.
- Do not post the same message everywhere.
- Do not include private workflow screenshots, local paths, tokens, customer data, or real task histories.

## Better Ask

Ask for feedback, examples, and missing templates:

- "What governance template would be useful for your agent workflow?"
- "Does the approval-gate model match how your team works?"
- "What should the stricter privacy scanner catch?"

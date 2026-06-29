from __future__ import annotations

import json
from pathlib import Path

import streamlit as st

ROOT = Path(__file__).resolve().parent
EXAMPLES = ROOT / "examples"


def load_json(name: str):
    return json.loads((EXAMPLES / name).read_text(encoding="utf-8"))


def status_badge(status: str) -> str:
    colors = {
        "ready": "#2563eb",
        "running": "#9333ea",
        "review": "#d97706",
        "blocked": "#dc2626",
        "done": "#16a34a",
        "waiting": "#64748b",
    }
    color = colors.get(status.lower(), "#475569")
    return f"<span style='background:{color};color:white;border-radius:999px;padding:0.2rem 0.55rem;font-size:0.78rem'>{status}</span>"


def metric_card(label: str, value: int | str, help_text: str):
    st.metric(label, value, help=help_text)


def render_agents(agents):
    for agent in agents:
        with st.container(border=True):
            st.markdown(f"### {agent['name']}")
            st.caption(agent["mission"])
            cols = st.columns(3)
            cols[0].write(f"**Owner:** {agent['owner']}")
            cols[1].write(f"**Default risk:** {agent['default_risk']}")
            cols[2].markdown(status_badge(agent["status"]), unsafe_allow_html=True)
            st.write("**Boundaries**")
            st.write(", ".join(agent["boundaries"]))


def render_tasks(tasks):
    for task in tasks:
        with st.container(border=True):
            top = st.columns([3, 1, 1])
            top[0].markdown(f"### {task['title']}")
            top[1].markdown(status_badge(task["status"]), unsafe_allow_html=True)
            top[2].write(f"Risk: **{task['risk']}**")
            st.write(task["summary"])
            st.write(f"**Owner:** {task['owner']}")
            st.write(f"**Next action:** {task['next_action']}")
            if task.get("evidence"):
                st.write("**Evidence:** " + ", ".join(task["evidence"]))


def render_risks(risks):
    for item in risks:
        with st.container(border=True):
            st.markdown(f"### {item['risk']}")
            st.write(f"**Level:** {item['level']}")
            st.write(f"**Trigger:** {item['trigger']}")
            st.write(f"**Required control:** {item['control']}")


def render_workflows(workflows):
    for wf in workflows:
        with st.container(border=True):
            st.markdown(f"### {wf['name']}")
            st.write(wf["summary"])
            st.write("**Stages:**")
            for idx, stage in enumerate(wf["stages"], start=1):
                st.write(f"{idx}. {stage}")


def main():
    st.set_page_config(page_title="Agent Governance Workbench", layout="wide")

    agents = load_json("agents.json")
    tasks = load_json("tasks.json")
    risks = load_json("risk_register.json")
    workflows = load_json("workflows.json")

    st.title("Agent Governance Workbench")
    st.caption("A local-first dashboard for safer AI agent operations.")

    total_tasks = len(tasks)
    blocked = sum(1 for task in tasks if task["status"] == "blocked")
    review = sum(1 for task in tasks if task["status"] == "review")
    done = sum(1 for task in tasks if task["status"] == "done")

    cols = st.columns(4)
    with cols[0]:
        metric_card("Tasks", total_tasks, "Synthetic tasks in the demo queue")
    with cols[1]:
        metric_card("In Review", review, "Tasks waiting for reviewer or human approval")
    with cols[2]:
        metric_card("Blocked", blocked, "Tasks stopped by a governance gate")
    with cols[3]:
        metric_card("Done", done, "Tasks with an evidence-backed result card")

    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "Task Queue",
        "Agents",
        "Risk Register",
        "Workflows",
        "Approval Gates",
    ])

    with tab1:
        st.subheader("Scoped task queue")
        render_tasks(tasks)

    with tab2:
        st.subheader("Agent operating roles")
        render_agents(agents)

    with tab3:
        st.subheader("Risk register")
        render_risks(risks)

    with tab4:
        st.subheader("Governance workflows")
        render_workflows(workflows)

    with tab5:
        st.subheader("Default approval rule")
        st.info("Low-risk tasks may proceed with a result card. Medium-risk tasks need reviewer signoff. High-risk tasks stop until a human approver explicitly approves the next action.")
        st.code(
            """risk: high\nrequired_gate: human_approval\nallowed_action: prepare_plan_only\nblocked_actions:\n  - external_write\n  - secret_access\n  - production_change\n  - public_release""",
            language="yaml",
        )


if __name__ == "__main__":
    main()

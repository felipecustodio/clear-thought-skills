# clear-thought-skills

◇ Clear Thought MCP, recast as Agent Skills.

Based on the original [Clear Thought 1.5 MCP Server](https://github.com/waldzellai/clearthought-onepointfive#) by Waldzell AI.

## § Aim

Convert Clear Thought reasoning tools into:

• focused `SKILL.md` instructions  
• minimal Python scripts  
• deterministic validation  
• high-coverage tests

## § Shape

```text
skills/        → Agent Skill directories
scripts/       → project utilities
shared/        → reusable Python helpers
tests/         → behavior and script coverage
SPEC.md        → migration contract
```

## § Rules

• `pyproject.toml` defines packages and tools  
• `uv.lock` pins the environment  
• `uv sync` installs dependencies  
• `just check` gates local changes  
• `prek` runs hooks  
• GitHub CI gates merges

## § Commands

```bash
just sync
just check
just validate-skills
```

## § Available Skills

| Skill Name | What It Does | Primary Use Cases |
| :--- | :--- | :--- |
| [analogical-reasoning](skills/analogical-reasoning/SKILL.md) | Transfers insights, principles, and structural patterns from a familiar source domain to an unfamiliar target domain. | **Novel Problem Solving**: Applying proven architecture patterns (e.g., assembly line) to new fields (e.g., software CI/CD pipelines).; **Simplifying Complex Concepts**: Explaining abstract technical systems using intuitive real-world analogs. |
| [beam-search](skills/beam-search/SKILL.md) | Evaluates multiple solution candidates in parallel, maintaining a fixed beam width of the top-k highest-scoring states at each step. Use for constrained optimization and decoding. | **Constrained Search Spaces**: When looking for an optimal sequence or configuration (e.g., prompt optimization, workflow synthesis, pathfinding).; **Top-K Candidate Tracking**: When maintaining a strict limit on the number of active possibilities at any given step. |
| [causal-analysis](skills/causal-analysis/SKILL.md) | Identifies root causes and causal relationships using Five Whys, Cause-and-Effect Diagrams, and Counterfactual Reasoning. | **Incident Post-Mortems**: Diagnosing production outages or major system bugs.; **System Failure Diagnosis**: Distinguishing root causes from surface-level errors. |
| [code-execution-reasoning](skills/code-execution-reasoning/SKILL.md) | Mental dry-run execution of code blocks, tracking variable states, call stacks, memory references, and iteration indices step by step. | **Code Review**: Auditing algorithmic code without running it directly.; **Static Bug Hunting**: Locating off-by-one errors, null pointers, or memory leaks. |
| [collaborative-reasoning](skills/collaborative-reasoning/SKILL.md) | Coordinates multi-agent or multi-persona perspectives (e.g. Architect, Security Engineer, Product Manager) to achieve consensus. | **Cross-Functional Architecture Reviews**: Evaluating software designs across security, scalability, and developer experience.; **Consensus Building**: Resolving conflicting priorities among stakeholders. |
| [creative-thinking](skills/creative-thinking/SKILL.md) | Facilitates lateral thinking, SCAMPER technique, random word association, and out-of-the-box ideation. | **Brainstorming Features**: Designing novel products, user experiences, or names.; **Unblocking Deadlocks**: Finding unconventional workarounds for rigid technical constraints. |
| [custom-framework](skills/custom-framework/SKILL.md) | Constructs and executes a domain-specific, tailored reasoning framework on the fly for unique domain requirements. | **Niche Domains**: Unique compliance frameworks, proprietary business processes, custom hardware specs.; **Specialized Problem Constraints**: When existing models (OODA, ToT, Scientific Method) are insufficient. |
| [debugging-approach](skills/debugging-approach/SKILL.md) | Applies root-cause isolation, binary search debugging, error trace analysis, and systematic troubleshooting methodologies. | **Software Debugging**: Investigating stack traces, test failures, memory leaks, or unexpected output.; **System Troubleshooting**: Diagnosing configuration errors or environment mismatches. |
| [decision-framework](skills/decision-framework/SKILL.md) | Evaluates choices systematically using multi-criteria decision analysis (MCDA), weighted scoring matrices, and risk profiles. | **Technology Selection**: Choosing between frameworks, databases, or vendors.; **Strategic Prioritization**: Evaluating features, projects, or architectural directions. |
| [decision-networks](skills/decision-networks/SKILL.md) | Models complex probabilistic decisions with utility nodes using Influence Diagrams and Decision Networks. | **Decisions under Uncertainty**: When actions have uncertain outcomes with distinct financial/operational utilities.; **Risk vs Reward Optimization**: Balancing high-risk/high-reward paths against safe/low-reward paths. |
| [ethical-analysis](skills/ethical-analysis/SKILL.md) | Evaluates decisions through major ethical frameworks (Utilitarianism, Deontology, Virtue Ethics, Rights-Based Ethics). | **Data Privacy & AI Governance**: Evaluating data usage, user tracking, or AI model safety.; **Policy & System Safety**: Assessing impact of automated actions on users, accessibility, and fairness. |
| [graph-of-thought](skills/graph-of-thought/SKILL.md) | Models complex problem solving as a Directed Acyclic Graph (DAG) of thoughts, enabling node aggregation, transformation, refinement, and non-linear network reasoning. | **Non-linear Problems**: Complex dependency networks, multi-perspective synthesis, or system integrations.; **Thought Aggregation**: Combining outputs from 2+ distinct sub-analyses into a unified synthesis node. |
| [mdp-planning](skills/mdp-planning/SKILL.md) | Formulates sequential decision-making problems as Markov Decision Processes (MDPs) with states, actions, transition probabilities, and rewards. | **Sequential Decision Making under Uncertainty**: Robotics, automated trading, adaptive workflows.; **Policy Optimization**: Finding the best action for every possible state of a system. |
| [mental-model](skills/mental-model/SKILL.md) | Applies first-principles thinking, inversion, Pareto principle, second-order thinking, and mental frameworks to frame problems. | **First Principles**: Deconstructing a problem to fundamental truths.; **Inversion**: Solving a problem backwards by asking how to guarantee failure. |
| [metacognitive-monitoring](skills/metacognitive-monitoring/SKILL.md) | Evaluates the agent's own reasoning process in real time, detecting cognitive biases, confidence drift, and logical gaps. | **Self-Correction Loops**: Mid-task checks during long, multi-step agent workflows.; **Bias Detection**: Ensuring recommendations aren't biased toward early assumptions. |
| [monte-carlo-tree-search](skills/monte-carlo-tree-search/SKILL.md) | Performs stochastic decision-making and search space exploration using Selection, Expansion, Simulation (Rollout), and Backpropagation. Use for high-uncertainty decision scenarios. | **High Uncertainty Decisions**: Scenarios with probabilistic outcomes or incomplete information.; **Complex Strategic Games/Planning**: Multi-agent negotiations, competitive strategies, or deep tactical planning. |
| [ooda-loop](skills/ooda-loop/SKILL.md) | Applies the Observe-Orient-Decide-Act (OODA) loop for rapid adaptive decision making in fast-changing or volatile environments. | **Rapidly Changing Environments**: Incident response, live debugging, real-time strategy adjustment.; **Adaptive Execution**: When new information arrives continuously and invalidates old assumptions quickly. |
| [optimization-reasoning](skills/optimization-reasoning/SKILL.md) | Formulates problems as mathematical or logical optimization models with explicit objective functions and constraints. | **Resource Allocation**: Budgeting, memory allocation, thread pool sizing, scheduling.; **Trade-off Analysis**: Maximizing performance while minimizing cost or latency constraints. |
| [orchestration-suggest](skills/orchestration-suggest/SKILL.md) | Recommends the optimal reasoning pattern or sequence of skills based on task complexity, constraints, and domain. | **Complex Unstructured Prompts**: When it is unclear which thinking framework is best suited.; **Workflow Planning**: Designing multi-stage agent execution chains. |
| [pdr-reasoning](skills/pdr-reasoning/SKILL.md) | Implements Predict-Disrupt-Reflect (PDR) reasoning to stress-test plans, identify hidden failure modes, and build resilient strategies. | **Plan Validation & Risk Assessment**: Before deploying critical code, database migrations, or major architectural changes.; **Adversarial Red-Teaming**: Identifying edge cases, security vulnerabilities, or single points of failure. |
| [research-reasoning](skills/research-reasoning/SKILL.md) | Synthesizes scientific literature, cross-references sources, evaluates evidence quality, and builds systematic research summaries. | **Literature Reviews**: Synthesizing academic papers, technical documentation, or benchmarks.; **Fact-Checking & Evidence Synthesis**: Evaluating conflicting technical claims across sources. |
| [scientific-method](skills/scientific-method/SKILL.md) | Applies empirical inquiry through Observation, Hypothesis Formation, Experimentation, Analysis, and Conclusion. | **Root Cause Analysis**: Investigating unexplained bugs, performance regressions, or test failures.; **Empirical Validation**: Testing technical assumptions against experimental data or logs. |
| [sequential-thinking](skills/sequential-thinking/SKILL.md) | A detailed, step-by-step reasoning process for dynamic, reflective problem-solving. Use when tackling complex, multi-stage problems that require hypothesis revision, thought branching, and continuous re-evaluation. | **Multi-step Problem Solving**: When a request cannot be answered safely or accurately in a single step.; **Hypothesis Testing & Refinement**: When initial assumptions might be wrong or need iterative validation. |
| [session-export](skills/session-export/SKILL.md) | Serializes current session state, thought history, and memory data into structured JSON files for persistence. | **State Persistence**: Saving progress before long background operations.; **Hand-off to Subagents**: Exporting context for sibling or child subagents. |
| [session-import](skills/session-import/SKILL.md) | Deserializes stored JSON session state files to restore thought context and memory. | **Resuming Saved Work**: Loading previously exported session state.; **Receiving Subagent Context**: Reading state created by another subagent process. |
| [session-info](skills/session-info/SKILL.md) | Summarizes the current agent session metadata, active reasoning state, thought counts, and historical trajectory. | **Progress Summarization**: Reporting session state during long-running tasks.; **Context Audit**: Verifying remaining thought budget or session parameters. |
| [simulation-reasoning](skills/simulation-reasoning/SKILL.md) | Simulates complex system behaviors over time under varying initial conditions or agent interactions. | **Complex Dynamic Systems**: Queueing systems, load behavior under traffic bursts, concurrency race conditions.; **Scenario Planning**: Simulating multi-agent market conditions, adoption curves, or failure cascades. |
| [socratic-method](skills/socratic-method/SKILL.md) | Uses disciplined, probing questions to uncover underlying assumptions, test reasoning logic, and guide conceptual understanding. | **Clarifying Requirements**: Uncovering hidden assumptions or ambiguous requests from users.; **Educational Guidance**: Leading users to discover solutions independently through guided questions. |
| [statistical-reasoning](skills/statistical-reasoning/SKILL.md) | Applies statistical thinking, probability estimation, confidence intervals, and Bayesian updating to quantitative data. | **Data Interpretation**: Analyzing benchmark results, metric changes, or experiment outcomes.; **Bayesian Inference**: Updating prior beliefs when new quantitative evidence arrives. |
| [structured-argumentation](skills/structured-argumentation/SKILL.md) | Constructs formal logical arguments using Claim, Data, Warrant, Backing, Counter-argument, and Rebuttal (Toulmin Model). | **RFCs & Technical Proposals**: Pitching new architecture or technology adoption.; **Debate & Position Papers**: Defending strategic technical choices against skepticism. |
| [systems-thinking](skills/systems-thinking/SKILL.md) | Analyzes complex systems by examining feedback loops, delays, leverage points, and holistic interconnections. | **Complex System Architecture**: Distributed systems, microservices, organizational dynamics.; **Unintended Consequences**: Preventing fixes that create bigger downstream problems. |
| [tree-of-thought](skills/tree-of-thought/SKILL.md) | Explores multiple reasoning paths simultaneously using tree search strategies (DFS/BFS). Use when evaluating competing hypotheses, decision trees, or multi-branch exploration scenarios. | **Branching Decision Trees**: Problems with distinct alternative choices (e.g., architectural choices, algorithm selection).; **Exploration & Backtracking**: Complex puzzle solving, strategic planning, or system optimization where early choices lock in downstream constraints. |
| [ulysses-protocol](skills/ulysses-protocol/SKILL.md) | Applies pre-commitment mechanisms and strict constraint bounds (Ulysses Contracts) to prevent self-sabotage, scope creep, or decision paralysis. | **Preventing Scope Creep**: When a task threatens to expand uncontrollably beyond initial requirements.; **Setting Hard Execution Limits**: Time-boxing, iteration caps, or strict resource limits on open-ended tasks. |
| [visual-dashboard](skills/visual-dashboard/SKILL.md) | Generates interactive HTML/CSS/JS dashboards and metrics panels for complex data visualization. | **Data Reporting**: Displaying multi-metric performance reports or telemetry data.; **Executive Summaries**: Creating visually engaging dashboard UI artifacts. |
| [visual-reasoning](skills/visual-reasoning/SKILL.md) | Uses visual diagrams (Mermaid, ASCII, UI mockups) to model spatial, architectural, and flow relationships. | **Architecture Documentation**: Drawing flowcharts, sequence diagrams, or component diagrams.; **Workflow Visualization**: Clarifying complex state machines or process branches. |

## § Status

◦ planning complete  
◦ tooling scaffolded  
◦ skill migration complete  
◦ notebook operations excluded as per spec

## § Credit

Original implementation: [waldzellai/clearthought-onepointfive](https://github.com/waldzellai/clearthought-onepointfive#).

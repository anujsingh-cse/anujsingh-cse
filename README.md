<!-- ─────────────────────────────────────────────────────────────────
     invisible ink · entry no. 1
     you view-source before you trust a page.
     the zookeeper does the same with software.
     you will get along.
     ───────────────────────────────────────────────────────────────── -->

<p align="center">
  <strong>THE FAILURE ZOO</strong><br>
  <sub>an institute for the study of confident, wrong software</sub>
  <br><br>
  <code>est. 2025 · kept by <a href="https://github.com/anujsingh-cse">Anuj Singh</a> · B.E. CSE, class of 2026 · India</code><br>
  <code>admission: free · budget: ₹0 · power source: one 4 GB GPU and several free tiers</code>
</p>

---

You are visiting a collection of instruments built to catch software — mostly AI —
in the act of being confidently wrong. Every enclosure here exists because a system
answered with certainty and nobody could say *why*.

| Gate | Destination | You will find |
|---|---|---|
| § I | The Grounds | the instruments themselves |
| § II | The Specimen Collection | what the instruments have caught |
| § III | Public Services | useful software, few monsters |
| § IV | The Fossil Record | strata, 2025 → now |
| § ∞ | Exhibit ∞ | do not feed |

---

## § I — The Grounds

### EXHIBIT 01 — Hall of Attributed Blame · [`raglens`](https://github.com/anujsingh-cse/raglens)

`Python · MIT · pip install raglens`

RAGAS tells you an answer is *"82% faithful."*
This enclosure tells you **chunk `r2_c0` did it** — removing it moved faithfulness
0.42 → 0.89 — then classifies the failure so you know whether to fix the retriever
or the generator.

Mechanism: leave-one-chunk-out **counterfactual attribution**, pairwise
conflict detection between chunks, four-way failure-mode classification.
Judge: a real LLM on NVIDIA NIM — no mocks, no scripted fixtures. Output: HTML report.

<sub>responsible for the capture of specimens S-001 through S-004.</sub>

---

### EXHIBIT 02 — The Debate Pit · [`orchestrator-of-three-cycles`](https://github.com/anujsingh-cse/orchestrator-of-three-cycles)

`Python · MIT · 124 tests · the zoo's original collection site`

Does an agent that argues with itself patch better than one that doesn't?
This harness answers with data, not vibes: **Coder proposes → Adversary attacks →
Critic rules → a human signs off.** Control group: one AI, no debate.

Every broken patch is preserved with full provenance — the *failure zoo* this
entire establishment is named after. Everything runs on NVIDIA's free NIM tier
(Ollama as drop-in), because a research question shouldn't require a budget.

<sub>run cost per experiment: ₹0. evidence collected: pricele— no. quantified. that is the point.</sub>

---

### EXHIBIT 03 — The Assistant That Frisks Itself · [`GhostCoder`](https://github.com/anujsingh-cse/GhostCoder)

`Python · MIT · pip install ghostcoder · local-first`

A coding assistant with **no sidebar and no chat window** — specialist agents leave
inline hints. Before any suggestion reaches you, an adversarial **Skeptic** re-reads
it for logic flaws and security problems; guardrails reject the `rm -rf`-class of help.
Every decision is recorded and replayable: `ghostcoder replay --session <id>`.

Model-agnostic over Ollama; auto-tunes itself to your VRAM, down to a GTX 1650 4 GB.
An assistant that does not trust itself is the only kind worth installing.

<sub>captured specimen S-007, which is common in the wild and declining here.</sub>

---

### EXHIBIT 04 — The Refutation Laboratory · [`causal-inference-toolkit`](https://github.com/anujsingh-cse/causal-inference-toolkit)

`Python · MIT · pip install causal-toolkit · [docs](https://anujsingh-cse.github.io/causal-inference-toolkit/)`

Correlation walks in. It is asked for papers.

DoWhy/EconML wrapped into YAML-configured pipelines: **identify → estimate →
refute → sensitivity.** Rosenbaum bounds, E-values, Cinelli-Hazlett robustness values,
synthetic control, difference-in-differences, A/B testing, uplift modeling.
Ships with a Streamlit console and one-command executive HTML reports.

<sub>permanent home of specimen S-006, the most abundant species on Earth.</sub>

---

### EXHIBIT 05 — The Unmanned Front Desk · [`devrel-agent`](https://github.com/anujsingh-cse/devrel-agent)

`TypeScript · GitHub App · live at https://devrel-agent-two.vercel.app`

Reads an issue, writes a multi-file fix, authors matching tests, **audits its own diff**,
opens the PR, then watches CI and pushes remediation commits when the build fails.
Eight phases; a multi-provider cascade (Gemini → NVIDIA NIM → GitHub Models) so a dead
API never leaves the desk unmanned.

<sub>visitors are reminded that the desk's output, like everything here, is reviewed before it ships. institutional habit.</sub>

---

## § II — The Specimen Collection

*What follows is every species of machine dishonesty currently in custody. Failures are catalogued by what they actually are, not by what they report themselves to be.*

| № | Reports itself as | Is actually | Captured by |
|---|---|---|---|
| S-001 | "the model hallucinated" | one chunk hijacked the answer (`chunk_dominance`) | Exhibit 01, counterfactual sweep |
| S-002 | "the RAG ignored the docs" | context retrieved, never used (`generation_ignore`) | Exhibit 01 |
| S-003 | "the model didn't know" | retriever never found the answer (`retrieval_miss`) | Exhibit 01 |
| S-004 | "two sources, one answer" | the chunks contradict; nobody noticed | Exhibit 01, conflict probe |
| S-005 | "LGTM, first patch" | the patch fails the edge case it was never shown | Exhibit 02, the Adversary |
| S-006 | "the chart proves it" | correlation in a lab coat | Exhibit 04 |
| S-007 | "a helpful suggestion" | `rm -rf`, offered cheerfully | Exhibit 03, guardrail |

<sub>The taxonomy is maintained in the repositories themselves — Exhibit 01 ships the classifier.</sub>

---

## § III — Public Services

*The zoo is not entirely preoccupied with misconduct. These counters serve the public directly.*

- **The Translation Window — [`YojanaSetu`](https://github.com/anujsingh-cse/YojanaSetu).**
  1,000+ Indian government welfare schemes matched to citizens by profile, explained
  by a vernacular AI (Hindi · Tamil · Marathi · Telugu), with an OCR document vault that
  fills the forms for you.
- **The Document Forensics Counter — [`autoinvoice-ocr`](https://github.com/anujsingh-cse/autoinvoice-ocr).**
  Invoice PDF goes in; structured, Stripe-billable JSON comes out. Tesseract.js plus an
  LLM for the layouts that refuse to be parsed.
- **The Telemetry Deck — [`nexus-analytics`](https://github.com/anujsingh-cse/nexus-analytics).**
  Real-time event analytics, sub-second latency, simulated high-throughput streams.
- **The Council Room — [`AgentParliament`](https://github.com/anujsingh-cse/AgentParliament).**
  Technical decisions settled by a vote of simulated developer personas. Minutes included.

---

## § IV — The Fossil Record

*Excavated, not curated. Displayed as found; some labels have faded.*

| Stratum | Deposits | Condition |
|---|---|---|
| early 2025 | `Ap`, `ap-exp5` | lab notebooks. first tools, made of sticks |
| mid 2025 | `netflix-clone` | replicated megafauna. a rite of passage |
| late 2025 | `commitsense`, `qa-portfolio` | instrument-shaped objects |
| mid 2026 | `ai-progress`, `CyberGuard-AI` | unlabeled jars, pending classification |
| mid 2026 → | everything above | on display, still warm |

<sub>The register holds 43 repositories. The zoo displays the ones that bite.</sub>

---

## § ∞ — Exhibit ∞ · [`Tom-riddle-s-diary`](https://github.com/anujsingh-cse/Tom-riddle-s-diary)

The only specimen the zoo bred itself — and then, against institutional advice, released.

Write in it. It remembers (Postgres + ChromaDB). It writes back
(`llama-3.3-70b`, NVIDIA NIM). It advertises itself, accurately, as a place to
*share secrets that disappear*. Full-stack: Next.js front, Python back, Docker-composed,
Clerk-gated, and yes — [it is alive](https://tom-riddle-s-diary-sage.vercel.app).

<!-- invisible ink · entry no. 2
     the diary reads you back.
     entry no. 3 is somewhere below. -->

The zookeeper notes the irony of an institution for verification keeping one enchanted
liar as a pet, and declines to comment further.

<sub>DO NOT FEED AFTER MIDNIGHT.</sub>

---

## Visitor Information

- **The keeper** is a final-year engineering student in India. Everything on these grounds
  was built on free tiers and a 4 GB GPU — an arrangement the zoo considers a feature.
- **Hours:** IST. Response latency scales with examinations. The keeper carries GitHub's
  *Quickdraw* badge; something was closed within five minutes of being opened.
  The zoo declines to say what.
- **Escaped specimens** (bugs) may be reported as issues on the relevant enclosure.
  They will be mounted, classified, and added to the collection.
- **Enclosure S-008 is intentionally empty.** It is reserved for the first production
  incident nobody has caught yet. If you are holding one, the zoo accepts donations.

<details>
<summary><sub>EMPLOYEES ONLY — plain-text résumé for humans in a hurry</sub></summary>

<br>

**Anuj Singh** — B.E. Computer Science, graduating 2026.

Builds evaluation and verification tooling for AI systems, and the systems too.
Shipped, open-source, and installable today:

- **raglens** — RAG diagnostics: counterfactual chunk attribution, conflict detection,
  failure-mode classification; NVIDIA NIM-native judge.
- **orchestrator-of-three-cycles** — research harness measuring whether adversarial
  multi-agent debate produces more robust code patches; 124 tests; SQLite audit log.
- **GhostCoder** — local-first AI pair programmer with self-validation, replayable
  decisions, and safety guardrails; on PyPI.
- **causal-inference-toolkit** — DoWhy/EconML wrapper with sensitivity analysis,
  quasi-experiments, uplift modeling, CLI + Streamlit UI; on PyPI, full docs site.
- **devrel-agent** — autonomous GitHub contributor app: triage → fix → tests → PR →
  CI remediation; multi-provider inference cascade; deployed.

Stack, plainly: Python and TypeScript; LLM evaluation, multi-agent orchestration,
causal inference, OCR pipelines, local-model ops (Ollama, 4 GB VRAM tuning),
Next.js, FastAPI, Stripe.

Graduates 2026. Accepting interesting problems.

</details>

<br>

<p align="center">
  <sub>Nothing on these grounds was trusted at first sight.<br>
  That is the whole enclosure policy, printed on every ticket.</sub>
</p>

<!-- invisible ink · entry no. 3
     there is no entry no. 4.
     if you found this, open an issue titled "escaped specimen"
     on any repository. the zookeeper will know what you mean. -->


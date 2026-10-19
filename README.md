# Prince Mittal

**AI engineer in the making — I build LLM systems from the GPU kernel up to the product.**

B.Tech CSE (AI/ML) at Dayananda Sagar University, Bengaluru. I like work where the numbers are measured, not claimed: inference engines, agent evaluation, and AI tools that real people in India can actually use.

[LinkedIn](https://linkedin.com/in/princemittalr) · [Email](mailto:prince.mittal.work@gmail.com) · Bengaluru, India

---

### Now

- Building **[TinyServe](https://github.com/princemittalr/tinyserve)**, a from-scratch LLM inference engine with custom Triton kernels
- Contributing fixes to open-source projects at Google, Google DeepMind, OpenPrinting, Microsoft and Kubernetes
- Learning: GPU performance engineering, LLM serving, evaluation methodology

---

### Featured work

**[TinyServe](https://github.com/princemittalr/tinyserve)** — LLM inference engine for a single free NVIDIA T4
Paged KV cache, continuous batching, radix prefix cache, hand-written Triton attention kernels and CUDA graphs, behind an OpenAI-compatible streaming API. **~5x the throughput of Hugging Face `generate()`** at 32 concurrent sequences (2,064 vs 414 tok/s) and token-identical output in fp32. Every number is logged with date, hardware and script.
`Python` `PyTorch` `Triton` `CUDA`

**[AgentLens](https://github.com/princemittalr/agentlens)** — observability and evaluation for LLM agents · [live demo](https://agentlens-production-29ad.up.railway.app)
One decorator traces any agent pipeline (latency, tokens, cost, steps). Rule-based and LLM-judge metrics on every run, prompt-regression detection with significance testing, and HDBSCAN clustering of failures.
`Python` `FastAPI` `SQLite` `HDBSCAN`

**[Verdantix](https://github.com/princemittalr/verdantix)** — AI digital twin of a university campus · [live demo](https://verdantix-frontend.vercel.app)
Finds energy, water and waste problems from meters, CCTV and student photo reports, routes each one to the right team, and closes a job only with proof it was fixed. Web app, Android app and 3D campus map. Built for CodeClash 2.0.
`Python` `FastAPI` `Gemini` `MapLibre` `PWA`

**[PaybackAI](https://github.com/princemittalr/paybackai)** — autonomous agent for failed-payment recovery
Classifies why a payment failed, runs a 7-rule compliance engine (retry caps, quiet hours, fraud hard-stop) and sends recovery nudges, with a full audit trail per payment. 58% recovery on a 60-payment test set; 43/43 tests passing. Built for the Razorpay AI Buildathon.
`Python` `FastAPI` `Next.js` `Groq`

**[AI Audit Platform](https://github.com/princemittalr/ai-audit-platform)** — static analysis CLI for TypeScript / React / Next.js
Resolves the real import graph, finds circular dependencies and dead code, scores the repo, and ships a GitHub Action that fails PRs on critical findings.
`TypeScript` `AST` `GitHub Actions`

**[ArogyaOS](https://github.com/princemittalr/arogyaos)** — healthcare operations platform · [live demo](https://arogyaos-five.vercel.app)
One system for hospitals, PHCs, pharmacies, labs and district administrators, with Gemini forecasting shortages and load.
`Next.js` `TypeScript` `Firebase` `Gemini`

---

### Open source

| Project | Contribution | Status |
|---|---|---|
| [google/adk-python](https://github.com/google/adk-python/pull/6969) | Model Armor plugin: screen tool output before it reaches the model | Merged |
| [google-deepmind/mujoco_warp](https://github.com/google-deepmind/mujoco_warp/pull/1741) | Fix flex element contact IDs for non-first flexes | Merged |
| [OpenPrinting/libcupsfilters](https://github.com/OpenPrinting/libcupsfilters/pull/219) | Declare pdfio as a public pkg-config dependency | Merged |
| [OpenPrinting/libcupsfilters](https://github.com/OpenPrinting/libcupsfilters/pull/265) | Fix back pages rotated 180° in long-edge duplex | In review |
| [kubernetes/test-infra](https://github.com/kubernetes/test-infra/pull/37961) | Revert a premature flag in `ci-kubernetes-build` | In review |
| [microsoft/vscode](https://github.com/microsoft/vscode/pull/340091) | Stop launching VS Code through a shell on Windows | In review |

---

### Tools for real users

Free, multilingual (English · Tamil · Hindi) apps built for people who usually get left out of software.

| App | For | |
|---|---|---|
| [TN Scholarship Finder](https://github.com/princemittalr/tn-scholarship-finder) | Tamil Nadu engineering students finding scholarships they qualify for | [Open](https://tn-scholarship-finder.streamlit.app) |
| [Placement Readiness Analyzer](https://github.com/princemittalr/placement-readiness-analyzer) | Honest placement scoring, mock interviews and resume ATS checks | [Open](https://placement-readiness-analyzer.streamlit.app) |
| [NGO Field Report Analyzer](https://github.com/princemittalr/ngo-analyzer) | Turning messy WhatsApp field notes into urgent-case reports for rural NGOs | [Open](https://ngo-analyzer.streamlit.app) |
| [PDF Chat AI](https://github.com/princemittalr/pdf-chat-ai) | Asking questions of any PDF, with page citations | [Open](https://pdf-chatai.streamlit.app) |

---

### Stack

**Languages** — Python, TypeScript, C, Java
**ML & systems** — PyTorch, Triton, CUDA, Hugging Face, OpenCV
**LLMs** — Gemini, Groq / Llama, NVIDIA Nemotron, Google ADK, LLM-as-judge evaluation
**Backend & web** — FastAPI, Next.js, React, Firebase, Streamlit, Tailwind
**Infra** — Docker, GitHub Actions, Vercel, Railway, Playwright

**Languages I speak** — Hindi (native), English (fluent), Tamil (conversational)

<div align="center">

# Prince Mittal

Building LLM systems — from GPU kernels to products.

<img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&size=14&duration=3500&pause=1500&color=8B949E&center=true&vCenter=true&width=520&height=24&lines=inference+engines+%C2%B7+agent+infrastructure+%C2%B7+open+source" alt="inference engines · agent infrastructure · open source" />

[LinkedIn](https://www.linkedin.com/in/princemittalr/) &nbsp;·&nbsp; [Hugging Face](https://huggingface.co/princemittalr) &nbsp;·&nbsp; [Kaggle](https://www.kaggle.com/princemittalr) &nbsp;·&nbsp; Bengaluru, India

</div>

<br>

I work across the LLM stack: writing inference engines and Triton kernels, building evaluation and observability tooling for agents, and shipping the products on top. I'm a CS student at Dayananda Sagar University, and I contribute upstream to Google ADK, MuJoCo Warp, Kubeflow, OpenPrinting and openSUSE.

<br>

### Selected work

| | |
|:--|:--|
| **[tinyserve](https://github.com/princemittalr/tinyserve)** | From-scratch LLM inference engine for a free T4 — paged KV cache, continuous batching, radix prefix cache, custom Triton paged-attention kernels, CUDA graphs. **4.98× HF `generate()` throughput** at 32 concurrent requests, token-identical in fp32. |
| **[agentlens](https://github.com/princemittalr/agentlens)** | Observability and evaluation for LLM agents — traces any pipeline, scores runs with LLM judges, flags prompt regressions and clusters failures. |
| **[driftwatch](https://github.com/princemittalr/driftwatch)** | Multi-agent system that correlates repo and dependency signals across three tiers of Nemotron models and files a ranked action plan as GitHub issues. |
| **[ai-audit-platform](https://github.com/princemittalr/ai-audit-platform)** | CLI that resolves the import graph of TS/React/Next.js repos, finds real circular dependencies and dead code, and exports scored reports. |
| **[verdantix](https://github.com/princemittalr/verdantix)** | AI digital twin of the DSU Harohalli campus — detects energy, water and waste issues, routes them to teams, and closes jobs only on photo proof of the fix. FastAPI · Gemini · MapLibre · Android. |
| **[arogyaos](https://github.com/princemittalr/arogyaos)** | Healthcare operations platform for hospitals, pharmacies and district health teams. Next.js · Firebase · Gemini. |
| **[paybackai](https://github.com/princemittalr/paybackai)** | Autonomous agent for payment-failure recovery, built at the Razorpay AI Buildathon. |

<sub>Also: [scholarship finder](https://github.com/princemittalr/tn-scholarship-finder) · [multilingual PDF chat](https://github.com/princemittalr/pdf-chat-ai) · [NGO field-report analyzer](https://github.com/princemittalr/ngo-analyzer) · [placement readiness coach](https://github.com/princemittalr/placement-readiness-analyzer)</sub>

<br>

### Open source

| Project | Merged contributions |
|:--|:--|
| **Google DeepMind · MuJoCo Warp** | [Fix flex element contact id for non-first flexes](https://github.com/google-deepmind/mujoco_warp/pull/1741) |
| **Google · ADK Python** | [Model Armor `after_tool_callback` to screen tool output](https://github.com/google/adk-python/pull/6969) |
| **Kubeflow** | [Accept bracketed IPv6 registry hosts](https://github.com/kubeflow/mcp-server/pull/443) · [Stop `restrictToOrg` mutating shared catalog state](https://github.com/kubeflow/hub/pull/3364) |
| **OpenPrinting** | [Back pages rotated 180° in long-edge duplex](https://github.com/OpenPrinting/libcupsfilters/pull/265) · [Honor `print-scaling=none` with annotations](https://github.com/OpenPrinting/libcupsfilters/pull/269) · [pdfio as public pkg-config dependency](https://github.com/OpenPrinting/libcupsfilters/pull/219) · [Memory leaks in `fuzz_ppd`](https://github.com/OpenPrinting/fuzzing/pull/59) |
| **openSUSE** | [mtui](https://github.com/openSUSE/mtui/pulls?q=is%3Apr+author%3Aprincemittalr+is%3Amerged) — openQA export & job filters (3) · [docbuild](https://github.com/openSUSE/docbuild/pulls?q=is%3Apr+author%3Aprincemittalr+is%3Amerged) — shell completion, portal dedup (2) |
| **OpenCV Zoo** | [Typo fix across demo files](https://github.com/opencv/opencv_zoo/pull/315) |

<br>

### Stack

| | |
|:--|:--|
| **Languages** | Python · TypeScript · C |
| **ML systems** | PyTorch · Hugging Face Transformers · Triton · CUDA graphs |
| **LLMs & agents** | Gemini · Claude · Nemotron · Google ADK · LLM-as-judge evals |
| **Product** | FastAPI · Next.js · React · Firebase · Streamlit · Vercel |

<br>

<div align="center">
<sub>Always happy to talk inference, agents, or a good bug</sub>
</div>

---
name: Fine-Tuning LLMs
category: ai-ml-llm
status: researched
last-updated: 2026-07-30
sources:
  - https://huggingface.co/docs/trl
  - https://huggingface.co/blog/unsloth-trl
  - https://github.com/axolotl-ai-cloud/axolotl
  - https://unsloth.ai/docs/get-started/fine-tuning-llms-guide
  - https://github.com/hiyouga/LLaMA-Factory
  - https://www.spheron.network/blog/axolotl-vs-unsloth-vs-torchtune/
  - https://www.marktechpost.com/2026/07/22/unsloth-vs-axolotl-vs-trl-vs-llama-factory-a-fine-tuning-framework-comparison-on-speed-vram-and-multi-gpu/
  - https://pub.towardsai.net/unsloth-vs-axolotl-vs-trl-87-of-your-fine-tuning-vram-goes-to-a-tensor-you-never-wrote-d21b8326d89d
  - https://arxiv.org/abs/2106.09685
  - https://arxiv.org/abs/2305.18290
  - https://arxiv.org/html/2403.07691v2
  - https://kaitchup.substack.com/p/orpo-preference-optimization-without
  - https://miguel-mendez-ai.com/2025/01/07/preference-alignment
  - https://crazyrouter.com/en/blog/ai-fine-tuning-api-complete-guide-2026
  - https://platform.openai.com/docs/guides/fine-tuning
  - https://docs.anthropic.com/en/docs/build-with-claude/develop-prompts
  - https://www.grizzlypeaksoftware.com/library/comparing-llm-provider-pricing-and-performance-19oanku0
tags: [fine-tuning, lora, qlora, peft, rlhf, dpo, orpo, kto, axolotl, unsloth, trl, llama-factory]
---

# Fine-Tuning LLMs

## One-liner

Adapting a pretrained model's weights to a specific task, style, or domain — trading training cost and time for cheaper, more consistent, more on-brand inference at scale.

## What It Is

Fine-tuning takes a base LLM (e.g. Llama 3, Mistral, GPT-4o, Claude) and continues training it on a smaller, task-specific dataset so the model **behaves differently**: it follows your output format reliably, adopts your brand voice, knows your domain jargon, or refuses/handles edge cases the way you want. The base model stays fundamentally the same; only the weights shift.

Three major flavors in 2026:

1. **Supervised Fine-Tuning (SFT)** — train on (input, desired output) pairs. The workhorse for format, style, and instruction-following.
2. **Preference / Alignment Fine-Tuning** — train on (input, chosen_output, rejected_output) triplets to make the model prefer one output over another. Methods:
   - **RLHF** (RL from Human Feedback; PPO-based) — original method, complex, expensive.
   - **DPO** (Direct Preference Optimization; [arXiv 2305.18290](https://arxiv.org/abs/2305.18290)) — closed-form alternative to RLHF; simpler and cheaper.
   - **ORPO** (Odds Ratio Preference Optimization; [arXiv 2403.07691](https://arxiv.org/html/2403.07691v2)) — combines SFT and preference alignment in one step; no reference model needed.
   - **KTO** (Kahneman-Tversky Optimization) — uses binary "good/bad" feedback instead of pairwise preferences; cheaper to collect.
3. **PEFT (Parameter-Efficient Fine-Tuning)** — only train a small fraction of parameters:
   - **LoRA** (Low-Rank Adaptation; [arXiv 2106.09685](https://arxiv.org/abs/2106.09685)) — train low-rank matrices inserted into each layer. The default.
   - **QLoRA** — LoRA on a quantized (4-bit) base model. Fine-tunes a 70B model on a single 24GB consumer GPU.
   - **Adapters, prefix-tuning, prompt-tuning** — older alternatives; LoRA variants dominate in 2026.

The framework landscape (per [MarkTechPost 2026 framework comparison](https://www.marktechpost.com/2026/07/22/unsloth-vs-axolotl-vs-trl-vs-llama-factory-a-fine-tuning-framework-comparison-on-speed-vram-and-multi-gpu/) and [Spheron 2026 review](https://www.spheron.network/blog/axolotl-vs-unsloth-vs-torchtune/)):

| Framework | Role | Best for |
|-----------|------|----------|
| **TRL** ([HuggingFace](https://huggingface.co/docs/trl)) | Core trainer APIs (SFT, DPO, PPO, GRPO) | The base layer everything else builds on. |
| **Unsloth** | Kernel rewrites for speed + VRAM; integrates with TRL | Single-GPU / consumer GPU fine-tuning; 2–5× faster, ~60% less VRAM. |
| **Axolotl** | Config-driven multi-GPU + multimodal (LLaMA-Vision, Qwen2-VL, Pixtral) | Production fine-tuning at scale; vision-language models. |
| **LLaMA-Factory** | Unified CLI/UI for 100+ models | Quick start without writing code; broad model zoo. |
| **PyTorch TorchTune** | Native PyTorch fine-tuning | Native PyTorch users. |

Managed / API fine-tuning in 2026 (per [CrazyRouter 2026 guide](https://crazyrouter.com/en/blog/ai-fine-tuning-api-complete-guide-2026), [Grizzly Peak 2026 pricing](https://www.grizzlypeaksoftware.com/library/comparing-llm-provider-pricing-and-performance-19oanku0)):
- **OpenAI** offers fine-tuning on GPT-4o Mini at $0.30/1M training tokens. Inference for fine-tuned models is 2× base ($0.30/M input, $1.20/M output). Often beats raw GPT-4o for narrow tasks at 1/10 the cost.
- **Anthropic** (mid-2026) "offers nothing comparable" — they steer users toward prompt engineering + tools instead.
- **Google** offers tuning for Gemini models via Vertex AI.

## When To Use It

- **You need consistent output format / JSON schema / tone.** Prompting works 90% of the time; fine-tuning works 99%.
- **You need to encode a skill the base model doesn't have** — domain jargon, proprietary process, internal style guide.
- **You want to cut inference cost at scale.** A fine-tuned small model (e.g. GPT-4o-mini) often beats a prompted large model for narrow tasks at 1/10 the cost.
- **You have a labeled dataset (or can generate one)** and a measurable eval.
- **You want to reduce prompt length / latency.** Fine-tuned models often don't need long system prompts.
- **You're building something users will rely on being right every time.** Determinism > vibes.

## When NOT To Use It

- **You need the model to know facts that change weekly.** Fine-tuning is for behavior, not knowledge — use RAG instead.
- **You don't have a labeled dataset.** Generate one or use prompting first.
- **The base model already does it well enough.** Fine-tuning a model to do something it already does is wasted GPU-hours.
- **You're in MVP / week-one mode.** Fine-tuning is a 2–6 week investment (data → eval → training → CI). Get the prompt version working first.
- **Your task is so narrow that a fine-tuned small model will miss edge cases.** Don't over-fit.
- **You can't build a good eval.** Fine-tuning without measurement is guessing.

## Why It Matters in 2026

Three forces are reshaping fine-tuning practice:

1. **PEFT democratized it.** LoRA + QLoRA mean a competent engineer can fine-tune a 70B model on a single consumer GPU ([Towards AI 2025 analysis](https://pub.towardsai.net/unsloth-vs-axolotl-vs-trl-87-of-your-fine-tuning-vram-goes-to-a-tensor-you-never-wrote-d21b8326d89d)). Unsloth's kernel rewrites give 60% lower VRAM and 2–5× speedup with no quality loss. The "you need a GPU cluster" excuse is gone.
2. **Preference optimization replaced RLHF for most teams.** DPO, ORPO, and KTO are simpler, cheaper, and don't require training a separate reward model. For most alignment tasks, the playbook is now: SFT → DPO/ORPO → eval. RLHF/PPO is reserved for the largest labs.
3. **Managed fine-tuning + cheap inference shifted the math.** A fine-tuned GPT-4o-mini often matches raw GPT-4o on narrow tasks at 1/10 the cost ([CrazyRouter 2026](https://crazyrouter.com/en/blog/ai-fine-tuning-api-complete-guide-2026)). The decision is no longer "fine-tune vs prompt" but "fine-tune small model vs prompt large model" — and the fine-tuned-small side is winning for high-volume narrow tasks.

Practitioner playbook in 2026:
1. **Start with prompting.** Get a working prompt + eval.
2. **Generate or collect ~1k–10k examples.** Quality > quantity.
3. **SFT** with LoRA via TRL + Unsloth. ~$5–50 in cloud GPU.
4. **Align** with DPO or ORPO if you have preference data.
5. **Evaluate** on a held-out set. Compare to prompted baseline.
6. **Iterate** on data quality — not hyperparameters.

## Scoring Matrix (0–100)

| Criterion | Score | Evidence |
|-----------|-------|----------|
| Maturity | 90 | SFT is 5+ years old; LoRA (2021), DPO (2023), ORPO (2024) all stable and widely deployed. |
| Community | 95 | HuggingFace ecosystem (TRL, PEFT, Transformers) is the de facto standard; thousands of tutorials, papers, and recipe repos. |
| Learning curve | 50 | The mechanics (LoRA rank, learning rate, epochs, dataset format) are learnable in days; doing it *well* (data quality, eval-driven iteration, alignment safety) takes months. |
| Performance | 90 | Fine-tuned small models often match prompted large models on narrow tasks; LoRA/PEFT retains >95% of full fine-tuning quality. |
| Cost | 70 | Self-hosted LoRA fine-tuning: ~$5–100 per run depending on model size. Managed (OpenAI): $0.30/1M training tokens + 2× inference cost. Frontier model fine-tuning: $10k–1M+. |
| DX (developer experience) | 85 | TRL + Unsloth is excellent; Axolotl config files are easy; LLaMA-Factory has a UI; managed APIs are one-liners. |
| Production readiness | 90 | Used in production by every major AI company; the open-source stack is mature enough for production; managed APIs are even simpler. |

## Comparison With Alternatives

| Alternative | Better when | Worse when |
|-------------|-------------|------------|
| **Prompt engineering** | You're prototyping, don't have labels, or the base model already does it. | You need consistency, format reliability, or cheaper inference at scale. |
| **RAG** | You need facts the model wasn't trained on, especially facts that change. | You need to teach a skill, format, or domain style — not facts. |
| **DSPy / programmatic optimization** | You have eval data and want to optimize prompts without GPU cost. | The gap between your model and the desired behavior is large; you need weight updates. |
| **Distillation** | You want a small fast model that mimics a large slow one. | You have a niche task and labeled data of your own; fine-tuning is cheaper. |
| **In-context learning (long prompts with examples)** | You have no labels and can afford long prompts. | Latency, cost, or context-window constraints. |
| **Multi-task fine-tuning** | You have many tasks and want one model that handles all. | Tasks conflict; catastrophic forgetting risk. |

## Sources

- [HuggingFace TRL Docs](https://huggingface.co/docs/trl) — 2026
- [HuggingFace Blog — Make LLM Fine-tuning 2× faster with Unsloth and TRL](https://huggingface.co/blog/unsloth-trl) — 2024+
- [Axolotl GitHub](https://github.com/axolotl-ai-cloud/axolotl) — 2026
- [Unsloth — Fine-tuning LLMs Guide](https://unsloth.ai/docs/get-started/fine-tuning-llms-guide) — 2026
- [LLaMA-Factory GitHub](https://github.com/hiyouga/LLaMA-Factory) — 2026
- [Spheron — Axolotl vs Unsloth vs TorchTune (Mar 2026)](https://www.spheron.network/blog/axolotl-vs-unsloth-vs-torchtune/) — 2026-03
- [MarkTechPost — Unsloth vs Axolotl vs TRL vs LLaMA-Factory (Jul 2026)](https://www.marktechpost.com/2026/07/22/unsloth-vs-axolotl-vs-trl-vs-llama-factory-a-fine-tuning-framework-comparison-on-speed-vram-and-multi-gpu/) — 2026-07
- [Towards AI — Unsloth vs Axolotl vs TRL: 87% of Your Fine-Tuning VRAM Goes to a Tensor You Never Wrote](https://pub.towardsai.net/unsloth-vs-axolotl-vs-trl-87-of-your-fine-tuning-vram-goes-to-a-tensor-you-never-wrote-d21b8326d89d) — 2025
- [arXiv 2106.09685 — LoRA: Low-Rank Adaptation](https://arxiv.org/abs/2106.09685) — 2021
- [arXiv 2305.18290 — DPO: Direct Preference Optimization](https://arxiv.org/abs/2305.18290) — 2023
- [arXiv 2403.07691 — ORPO: Monolithic Preference Optimization without Reference Model](https://arxiv.org/html/2403.07691v2) — 2024
- [Kaitchup — ORPO: Preference Optimization without the SFT Step](https://kaitchup.substack.com/p/orpo-preference-optimization-without) — 2024
- [Miguel Mendez — LLM Preference Alignment (PPO, DPO, ORPO)](https://miguel-mendez-ai.com/2025/01/07/preference-alignment) — 2025-01
- [CrazyRouter — AI Fine-Tuning API Guide 2026](https://crazyrouter.com/en/blog/ai-fine-tuning-api-complete-guide-2026) — 2026
- [OpenAI — Fine-tuning Guide](https://platform.openai.com/docs/guides/fine-tuning) — 2026
- [Anthropic — Develop Prompts with Claude](https://docs.anthropic.com/en/docs/build-with-claude/develop-prompts) — 2026
- [Grizzly Peak — LLM Provider Pricing 2026](https://www.grizzlypeaksoftware.com/library/comparing-llm-provider-pricing-and-performance-19oanku0) — 2026
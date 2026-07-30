---
name: MLOps
category: data-ai
status: researched
last-updated: 2026-07-30
sources:
  - https://ml-ops.org/
  - https://github.com/cdfoundation/cdfi
  - https://github.com/EvanBacon/expo-mlops
  - https://www.kubeflow.org/
  - https://www.kubeflow.org/docs/
  - https://github.com/kubeflow/kubeflow
  - https://github.com/mlflow/mlflow
  - https://mlflow.org/
  - https://github.com/iterative/dvc
  - https://dvc.org/
  - https://github.com/feast-dev/feast
  - https://feast.dev/
  - https://docs.feast.dev/
  - https://github.com/bentoml/BentoML
  - https://www.bentoml.com/
  - https://github.com/argoproj/argo-workflows
  - https://www.zenml.io/
  - https://github.com/zenml-io/zenml
  - https://www.anyscale.com/
  - https://github.com/ray-project/ray
  - https://www.ray.io/
tags: [mlops, kubeflow, mlflow, dvc, feast, bentoml, argo, zenml, ray, model-deployment, feature-stores]
---

# MLOps

## One-liner

The DevOps for machine learning — versioning data + models, training pipelines, deployment, monitoring, and the tooling that turns ML experiments into reliable production systems.

## What It Is

MLOps is the set of practices that takes ML models from research notebooks to production systems and keeps them healthy. It covers:

| Stage | Activities |
|-------|-----------|
| **Data versioning** | Track datasets; DVC, Pachyderm, lakeFS. |
| **Experiment tracking** | Log params, metrics, artifacts; MLflow, Weights & Biases, Neptune. |
| **Model training** | Reproducible training pipelines; orchestrated compute. |
| **Model registry** | Versioned model artifacts; staged deploys. |
| **Feature store** | Shared feature definitions for online + offline; Feast, Tecton. |
| **Model deployment** | Batch, real-time, streaming; BentoML, Triton, KServe, vLLM. |
| **Model monitoring** | Drift, accuracy decay, latency; Evidently, Arize, Fiddler. |
| **CI/CD for ML** | Automated retrain + deploy; GitHub Actions + Argo. |
| **Compute orchestration** | Kubernetes + Kubeflow, Ray, Anyscale. |

### The 2026 tooling landscape

| Category | Tools |
|----------|-------|
| **Experiment tracking** | [MLflow](https://mlflow.org/), Weights & Biases, Neptune, Comet, ClearML. |
| **Data versioning** | [DVC](https://dvc.org/), Pachyderm, lakeFS. |
| **Pipeline orchestration** | [Kubeflow](https://www.kubeflow.org/), [ZenML](https://www.zenml.io/), Metaflow, Flyte, Argo Workflows. |
| **Model serving** | [BentoML](https://www.bentoml.com/), Triton Inference Server, KServe, [vLLM](https://www.vllm.ai/), TGI, Ray Serve. |
| **Feature stores** | [Feast](https://feast.dev/), Tecton, Hopsworks. |
| **Compute** | [Ray](https://www.ray.io/), [Anyscale](https://www.anyscale.com/), Kubernetes, AWS SageMaker, Vertex AI. |
| **Monitoring** | Arize, Fiddler, [Evidently](https://www.evidentlyai.com/), whylogs. |
| **CI/CD** | GitHub Actions + Argo, GitLab CI + Kubeflow. |

### Key concepts

| Concept | Description |
|---------|-------------|
| **Reproducibility** | Given code + data + config + environment, produce the same model. |
| **Lineage** | Track which data trained which model, deployed where, served to whom. |
| **Drift detection** | Statistical shift in input features or predictions. |
| **Champion / Challenger** | Run new model alongside current; route traffic gradually. |
| **Shadow deployment** | Send traffic to new model but don't return results; compare. |
| **Canary release** | Route 5% traffic to new model; monitor; ramp up. |
| **Model registry** | Versioned model artifacts with metadata + stage (staging / production). |
| **Online vs Offline features** | Online = low-latency lookup (Redis); offline = batch computation (warehouse). |
| **LLM-specific ops** | Prompt versioning, eval, RAG eval, agent traces (see [`../ai-ml-llm/llm-ops.md`](../ai-ml-llm/llm-ops.md)). |

Adoption: MLOps is the fastest-growing engineering discipline. MLflow has >20K GitHub stars; Kubeflow is CNCF incubating; every serious ML team has some form of MLOps tooling. The 2026 reality is that **most ML projects never make it to production** — MLOps is the answer to that gap.

## When To Use It

- **You're shipping ML models to production** — period.
- **You need reproducibility** — for compliance, debugging, or team coordination.
- **You retrain models regularly** — automated pipelines pay off.
- **You have many models** — registry + versioning.
- **You need feature consistency** between training (offline) and serving (online) — feature store.
- **You're an AI app team** — see the dedicated [`../ai-ml-llm/llm-ops.md`](../ai-ml-llm/llm-ops.md) for LLM-specific ops (prompts, evals, RAG, agents).

## When NOT To Use It

- **You don't ship ML to production** — research-only; notebook is fine.
- **You have one model, train once, ship once** — overkill.
- **You have no team** — solo projects can use notebooks.
- **You have no observability budget** — MLOps requires observability investment.
- **Premature optimization** — get the model working first.

## Why It Matters in 2026

Three forces:

1. **LLM-specific ops emerged.** Prompt versioning, RAG eval, agent traces — [`../ai-ml-llm/llm-ops.md`](../ai-ml-llm/llm-ops.md) covers the LLM layer. MLOps handles the classical ML layer.
2. **Feature stores became standard.** Feast (OSS) and Tecton (managed) matured; online + offline parity is now expected.
3. **K8s + Argo + MLflow stack standardized.** The "MLOps on Kubernetes" stack is real; Kubeflow + Argo Workflows + MLflow + BentoML is a complete pipeline.

Practitioner playbook in 2026:
1. **Experiment tracking**: **MLflow** (default) or Weights & Biases (managed).
2. **Data versioning**: **DVC** for small teams; lakeFS / Pachyderm for large.
3. **Pipelines**: **Kubeflow** (K8s-native) or **ZenML** (Pythonic).
4. **Serving**: **BentoML** for traditional ML; **vLLM** for LLMs.
5. **Feature store**: **Feast** (OSS) for most; **Tecton** if enterprise.
6. **Monitoring**: **Arize** or **Evidently**.
7. **LLM ops**: see [`../ai-ml-llm/llm-ops.md`](../ai-ml-llm/llm-ops.md).

## Scoring Matrix (0–100)

### MLflow
| Criterion | Score | Evidence |
|-----------|-------|----------|
| Maturity | 95 | 8+ years; the standard. |
| Community | 95 | Massive; integrated with every major ML framework. |
| Learning curve | 80 | Easy to start; advanced features take study. |
| Performance | 80 | Handles most use cases; scales to thousands of experiments. |
| Cost | 95 | OSS free; managed options reasonable. |
| DX | 85 | Mature UI; CLI; integrations. |
| Production readiness | 95 | Battle-tested at scale. |

### Kubeflow
| Criterion | Score | Evidence |
|-----------|-------|----------|
| Maturity | 85 | 8+ years; CNCF incubating. |
| Community | 80 | Strong in K8s-native shops. |
| Learning curve | 50 | Steep; requires K8s expertise. |
| Performance | 95 | K8s-native scaling. |
| Cost | 70 | OSS free; infra cost (K8s cluster). |
| DX | 65 | Complex but powerful. |
| Production readiness | 90 | Used at Google, Cisco, etc. |

## Comparison With Alternatives

| Alternative | Better when | Worse when |
|-------------|-------------|------------|
| **MLflow** | You want experiment tracking; you want one tool. | You need full pipeline orchestration. |
| **Kubeflow** | You're on K8s; you have a platform team. | Small team; no K8s expertise. |
| **ZenML** | You want Pythonic pipelines. | You need maximum K8s integration. |
| **Weights & Biases** | You want managed + best UX. | Cost-sensitive; you want OSS. |
| **SageMaker / Vertex AI** | You're all-in on AWS / GCP. | Multi-cloud. |
| **Ray / Anyscale** | You need distributed compute. | You just need a pipeline orchestrator. |
| **No MLOps** | Research-only. | Anything in production. |

## Sources

- [MLOps.org](https://ml-ops.org/) — 2026
- [CDF (Continuous Delivery Foundation)](https://github.com/cdfoundation/cdfi) — 2026
- [Kubeflow](https://www.kubeflow.org/) — 2026
- [Kubeflow Docs](https://www.kubeflow.org/docs/) — 2026
- [Kubeflow GitHub (kubeflow/kubeflow)](https://github.com/kubeflow/kubeflow) — 2026
- [MLflow GitHub (mlflow/mlflow)](https://github.com/mlflow/mlflow) — 2026
- [MLflow](https://mlflow.org/) — 2026
- [DVC GitHub (iterative/dvc)](https://github.com/iterative/dvc) — 2026
- [DVC](https://dvc.org/) — 2026
- [Feast GitHub (feast-dev/feast)](https://github.com/feast-dev/feast) — 2026
- [Feast](https://feast.dev/) — 2026
- [Feast Docs](https://docs.feast.dev/) — 2026
- [BentoML GitHub (bentoml/BentoML)](https://github.com/bentoml/BentoML) — 2026
- [BentoML](https://www.bentoml.com/) — 2026
- [Argo Workflows GitHub (argoproj/argo-workflows)](https://github.com/argoproj/argo-workflows) — 2026
- [ZenML](https://www.zenml.io/) — 2026
- [ZenML GitHub (zenml-io/zenml)](https://github.com/zenml-io/zenml) — 2026
- [Anyscale](https://www.anyscale.com/) — 2026
- [Ray GitHub (ray-project/ray)](https://github.com/ray-project/ray) — 2026
- [Ray](https://www.ray.io/) — 2026
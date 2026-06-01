# Dataset and Training Selection

Use when prompt/RAG/tool changes are insufficient and adaptation may be needed.

Decision order:

1. Verify the failure is not product scope, context, retrieval, prompt, tool, or eval mismatch.
2. Define target behavior and data schema.
3. Choose data source: human labels, production replay, synthetic generation, self-instruct, Evol-Instruct, distillation, preference pairs.
4. Choose method: SFT, LoRA/QLoRA, DPO/IPO/KTO/ORPO/GRPO/SimPO, reward modeling, reranker training, embedding tuning.
5. Create eval gates before training.
6. Train small first; compare against non-training alternatives.

Always include data QA, contamination checks, privacy review, and rollback.

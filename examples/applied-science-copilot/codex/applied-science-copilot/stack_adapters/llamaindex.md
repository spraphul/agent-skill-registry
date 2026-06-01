# LlamaIndex Adapter

Use LlamaIndex when data ingestion, indexing, retrieval, and query orchestration are the central product risks.

## Good fit

- RAG systems over heterogeneous documents or structured/unstructured stores.
- Indexing and retrieval experiments.
- Query engines with citations and source provenance.

## Workflow

1. Define source inventory, ACLs, freshness, and provenance requirements.
2. Select loaders/connectors and chunking strategy.
3. Choose index/retriever/reranker path.
4. Build retrieval evals before answer-generation evals.
5. Add citation and context contract checks.
6. Track retrieval failures separately from answer-generation failures.

## Required artifacts

- Source/context contract
- Index config
- Retrieval eval set
- Reranking/context packing plan
- Citation policy

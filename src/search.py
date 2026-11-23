from qdrant_client import QdrantClient, models

client = QdrantClient(
    url="http://localhost:6333"
)

query_text = "headphones"

results, _ = client.scroll(
    collection_name="products",
    scroll_filter=models.Filter(
        must=[
            models.FieldCondition(
                key="name",
                match=models.MatchText(
                    text=query_text
                )
            )
        ]
    ),
    with_payload=True,
    limit=5
)

for product in results:
    print("Name:", product.payload.get("name", "N/A"))
    print("Details:", product.payload)
    print("-" * 40)

import os
from dotenv import load_dotenv
from neo4j import GraphDatabase

load_dotenv()

NEO4J_URI = os.getenv("NEO4J_URI", "bolt://127.0.0.1:7687")
NEO4J_USERNAME = os.getenv("NEO4J_USERNAME", "neo4j")
NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD")
NEO4J_DATABASE = os.getenv("NEO4J_DATABASE", "neo4j")

if not NEO4J_PASSWORD:
    raise ValueError("NEO4J_PASSWORD is missing from .env")

driver = GraphDatabase.driver(
    NEO4J_URI,
    auth=(NEO4J_USERNAME, NEO4J_PASSWORD)
)


def test_connection():
    driver.verify_connectivity()

    with driver.session(database=NEO4J_DATABASE) as session:
        result = session.run(
            "RETURN 'Neo4j connected successfully!' AS message"
        )
        return result.single()["message"]


if __name__ == "__main__":
    try:
        print(test_connection())
    except Exception as error:
        print("Neo4j connection failed:", error)
    finally:
        driver.close()

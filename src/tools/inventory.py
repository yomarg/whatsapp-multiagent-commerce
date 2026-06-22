import sqlite3
import asyncio
from typing import Dict, Any

DB_PATH = "commerce.db"

async def check_stock(product_query: str) -> Dict[str, Any]:
    """
    Busca productos en SQLite asincrónicamente.
    """
    def _query():
        with sqlite3.connect(DB_PATH) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            cursor.execute(
                "SELECT name, price, stock FROM products WHERE name LIKE ? LIMIT 5",
                (f"%{product_query}%",)
            )
            return [dict(row) for row in cursor.fetchall()]
            
    loop = asyncio.get_running_loop()
    results = await loop.run_in_executor(None, _query)
    
    return {"status": "success", "data": results}

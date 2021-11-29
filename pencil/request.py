import sqlite3
import json
from models import Pencil


def get_single_pencil(id):
    with sqlite3.connect("./katapencil.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            p.id,
            p.point_durability,
            p.length,
            p.eraser_durability
            
            FROM pencil p
            WHERE p.id = ?
            """, (id, ))
        
        data = db_cursor.fetchone()
        
        pencil = Pencil(['id'], data['point_durability'], data['length'], data['eraser_durability'])
        
        return json.dumps(pencil.__dict__)
    
    
def update_pencil(id, new_pencil):
    
    with sqlite3.connect("./katapencil.db") as conn:
        db_cursor = conn.cursor()
        
        db_cursor.execute("""
        UPDATE Pencil
            SET
                point_durability = ?,
                length = ?,
                eraser_durability = ?
            
            WHERE id = ?
            """, (new_pencil['point_durability'], new_pencil['length'], new_pencil['eraser_durability'], id))
        
        rows_affected = db_cursor.rowcount
        
        if rows_affected == 0:
            return False
        else:
            return True
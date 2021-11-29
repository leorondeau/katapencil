import sqlite3
import json
from models import Journal


def get_single_journal(id):
    with sqlite3.connect("./katapencil.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            j.id,
            j.entry
            
            FROM journal j
            WHERE j.id = ?
            """, (id, ))
        
        data = db_cursor.fetchone()
        
        journal = Journal(['id'], data['entry'])
        
        return json.dumps(journal.__dict__)
    
    
def update_journal(id, new_journal):
    
    with sqlite3.connect("./katapencil.db") as conn:
        db_cursor = conn.cursor()
        
        db_cursor.execute("""
        UPDATE Journal
            SET
                entry = ?
            
            WHERE id = ?
            """, (new_journal['entry'], id))
        
        rows_affected = db_cursor.rowcount
        
        if rows_affected == 0:
            return False
        else:
            return True
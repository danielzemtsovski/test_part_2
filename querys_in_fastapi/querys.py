from connection import connection
from logger import log_event

class Querys:
    def performing_query(self, query):
        log_event("INFO", f"Executing query: {query}") 
        try:
            conn = connection.get_connection()
            with conn.cursor() as cursor:
                cursor.execute(query)
                fetchall = cursor.fetchall()
                log_event("INFO", f"The query was executed successfully.")
                return fetchall
        except Exception as e:
            log_event("ERROR",f"query error: {str(e)}")
            raise e
        finally:
            if conn:
                conn.close()

    def query_1(self):
        log_event("INFO", f"Running query 1")
        query = """
                select entity_id, target_name, priority_level, movement_distance_km
                from targets
                where priority_level in (1,2) and movement_distance_km > 5;
                """
        return self.performing_query(query)

    def query_2(self):
        log_event("INFO", f"Running query 2")
        query = """
                select signal_type, count(*) as count_signal
                from intel_signals
                group by signal_type
                order by count_signal desc;
                """
        return self.performing_query(query)
    
    def query_3(self):
        log_event("INFO", f"Running query 3")
        query = """
                select entity_id, count(*) as count
                from intel_signals
                where priority_level = 99
                group by entity_id
                order by count desc
                limit 3; 
                """
        return self.performing_query(query)
    
    def query_4(self):
        log_event("INFO", f"Running query 4")
        query = """
            with day as (
                    select entity_id
                    from intel_signals
                    where hour(timestamp) >= 8 and hour(timestamp) < 20
                    group by entity_id
                    having sum(distance_from_last) = 0
                
            ),
            night as (
                    select entity_id
                    from intel_signals
                    where hour(timestamp) >= 20 or hour(timestamp) < 8
                    group by entity_id
                    having sum(distance_from_last) >= 10
            )
            select d.entity_id
            from day as d
            inner join night as n 
            on d.entity_id = n.entity_id;
          """
        return self.performing_query(query)
    
    def query_5(self):
        log_event("INFO", f"Running query 5")
        query = ""
        return self.performing_query(query)
    
    def query_6(self):
        log_event("INFO", f"Running query 6")
        query = ""
        return self.performing_query(query)
    
    def query_7(self):
        log_event("INFO", f"Running query 7")
        query = ""
        return self.performing_query(query)
    
    
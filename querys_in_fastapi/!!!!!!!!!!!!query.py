query_1 = """
            select entity_id, target_name, priority_level, movement_distance_km
            from targets
            where priority_level in (1,2) and movement_distance_km > 5;
          """


query_2 = """
            select signal_type, count(*) as count_signal
            from intel_signals
            group by signal_type
            order by count_signal desc;
          """

query_3 = """
            select entity_id, count(*) as count
            from intel_signals
            where priority_level = 99
            group by entity_id
            order by count desc
            limit 3;
          """

# query_4 = """
#             with a as(
#                 select entity_id
#                 from targets
#                 where hour(timestamp) >= 8 and hour(timestamp) <= 20
#                 group by entity_id
#                 having max(reported_lat) = min(reported_lat) and max(reported_lon) = min(reported_lon))


#            
#           """

query_5 = """
          
          """




query_6 = """
          with aaaa as (
              select a.entity_id, a.timestamp as attack_time -- הוספנו Alias כדי שיתאים להמשך
              from attacks as a
              inner join damage_assessments as d on a.attack_id = d.attack_id
              where d.result != "destroyed"
          ), 
          speed_before AS (
              SELECT aaaa.entity_id, aaaa.attack_time, AVG(s.movement_distance_km) AS avg_before
              FROM aaaa
              JOIN intel_signals s ON aaaa.entity_id = s.entity_id
              WHERE s.timestamp BETWEEN DATE_SUB(aaaa.attack_time, INTERVAL 3 HOUR) AND aaaa.attack_time
              GROUP BY aaaa.entity_id, aaaa.attack_time
          ),
          speed_after AS (
              SELECT aaaa.entity_id, aaaa.attack_time, AVG(s.movement_distance_km) AS avg_after
              FROM aaaa
              JOIN intel_signals s ON aaaa.entity_id = s.entity_id
              WHERE s.timestamp BETWEEN aaaa.attack_time AND DATE_ADD(aaaa.attack_time, INTERVAL 3 HOUR)
              GROUP BY aaaa.entity_id, aaaa.attack_time
          )
          SELECT 
              b.entity_id,
              b.avg_before,
              a.avg_after,
              ((a.avg_after - b.avg_before) / b.avg_before) * 100 AS speed_change_percent
          FROM speed_before b
          JOIN speed_after a ON b.entity_id = a.entity_id AND b.attack_time = a.attack_time
          WHERE a.avg_after >= b.avg_before * 1.5;
          """




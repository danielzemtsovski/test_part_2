query_1 = """
            select entity_id, target_name, priority_level, movement_distance_km
            from targets
            where priority_level in (1,2) and movement_distance_km < 5;
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


query_6 = """
            with aaaa as(
                        select a.entity_id, a.timestamp
                        from attacks as a
                        inner join damage_assessments as d
                        on a.attack_id = d.attack_id
                        where d.result != destroyed
                        )

                    
          """




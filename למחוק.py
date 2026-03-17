 ###############   תקיפות   ################### 

`attacks`  = (
  `attack_id` varchar(36) NOT NULL,
  `timestamp` datetime(6) NOT NULL,
  `entity_id` varchar(50) NOT NULL,
  `weapon_type` varchar(100) NOT NULL,
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`attack_id`),
  KEY `idx_entity_id` (`entity_id`),
  KEY `idx_timestamp` (`timestamp`)
)

##################   נזקים    ##############
`damage_assessments` = (
  `id` int NOT NULL AUTO_INCREMENT,
  `timestamp` datetime(6) NOT NULL,
  `attack_id` varchar(36) NOT NULL,
  `entity_id` varchar(50) NOT NULL,
  `result` enum('destroyed','damaged','no_damage') NOT NULL,
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `idx_attack_id` (`attack_id`),
  KEY `idx_entity_id` (`entity_id`),
  KEY `idx_timestamp` (`timestamp`)
)

####################            דיווחים    #####################

`intel_signals` =  (
  `signal_id` varchar(36) NOT NULL,
  `timestamp` datetime(6) NOT NULL,
  `entity_id` varchar(50) NOT NULL,
  `reported_lat` double NOT NULL,
  `reported_lon` double NOT NULL,
  `signal_type` enum('SIGINT','VISINT','HUMINT') NOT NULL,
  `priority_level` int NOT NULL,
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`signal_id`),
  KEY `idx_entity_id` (`entity_id`),
  KEY `idx_signal_type` (`signal_type`),
  KEY `idx_timestamp` (`timestamp`)
)

###############    מטרות    ###############

`targets` =  (
  `entity_id` varchar(50) NOT NULL,
  `target_name` varchar(100) NOT NULL,
  `target_type` varchar(50) NOT NULL,
  `initial_lat` double NOT NULL,
  `initial_lon` double NOT NULL,
  `last_known_lat` double DEFAULT NULL,
  `last_known_lon` double DEFAULT NULL,
  `priority_level` int NOT NULL,
  `status` enum('active','attacked','damaged','destroyed') NOT NULL DEFAULT 'active',
  `movement_distance_km` double NOT NULL DEFAULT '0',
  `avg_speed_m_per_s` double DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`entity_id`)
)
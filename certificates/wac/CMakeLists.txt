INSTALL(FILES ${CMAKE_CURRENT_SOURCE_DIR}/wac.publisherid.pem
        DESTINATION ${WAC_DIR}
        PERMISSIONS OWNER_READ
                    GROUP_READ
                    WORLD_READ)

INSTALL(FILES ${CMAKE_CURRENT_SOURCE_DIR}/wac.root.preproduction.pem
        DESTINATION ${WAC_DIR}
        PERMISSIONS OWNER_READ
                    GROUP_READ
                    WORLD_READ)

INSTALL(FILES ${CMAKE_CURRENT_SOURCE_DIR}/wac.root.production.pem
        DESTINATION ${WAC_DIR}
        PERMISSIONS OWNER_READ
                    GROUP_READ
                    WORLD_READ)

INSTALL(FILES ${CMAKE_CURRENT_SOURCE_DIR}/tizen-distributor-root-ca-partner-manufacturer.pem
        DESTINATION ${TIZEN_DIR}
        PERMISSIONS OWNER_READ
                    GROUP_READ
                    WORLD_READ)

INSTALL(FILES ${CMAKE_CURRENT_SOURCE_DIR}/tizen-distributor-root-ca-partner-operator.pem
        DESTINATION ${TIZEN_DIR}
        PERMISSIONS OWNER_READ
                    GROUP_READ
                    WORLD_READ)

INSTALL(FILES ${CMAKE_CURRENT_SOURCE_DIR}/tizen-distributor-root-ca-partner.pem
        DESTINATION ${TIZEN_DIR}
        PERMISSIONS OWNER_READ
                    GROUP_READ
                    WORLD_READ)

INSTALL(FILES ${CMAKE_CURRENT_SOURCE_DIR}/tizen-partner-class-developer-root.pem
        DESTINATION ${TIZEN_DIR}
        PERMISSIONS OWNER_READ
                    GROUP_READ
                    WORLD_READ)

INSTALL(FILES ${CMAKE_CURRENT_SOURCE_DIR}/tizen-partner-class-root-authority.pem
        DESTINATION ${TIZEN_DIR}
        PERMISSIONS OWNER_READ
                    GROUP_READ
                    WORLD_READ)

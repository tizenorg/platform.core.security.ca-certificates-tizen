INSTALL(FILES ${CMAKE_CURRENT_SOURCE_DIR}/tizen-developer-root-ca.pem
        DESTINATION ${TIZEN_DIR}
        PERMISSIONS OWNER_READ
                    GROUP_READ
                    WORLD_READ)

INSTALL(FILES ${CMAKE_CURRENT_SOURCE_DIR}/tizen-developers-root.pem
        DESTINATION ${TIZEN_DIR}
        PERMISSIONS OWNER_READ
                    GROUP_READ
                    WORLD_READ)

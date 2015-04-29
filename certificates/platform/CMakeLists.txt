INSTALL(FILES ${CMAKE_CURRENT_SOURCE_DIR}/tizen-platform-class-developer-root.pem
        DESTINATION ${TIZEN_DIR}
        PERMISSIONS OWNER_READ
                    GROUP_READ
                    WORLD_READ)

INSTALL(FILES ${CMAKE_CURRENT_SOURCE_DIR}/tizen-platform-class-root-authority.pem
        DESTINATION ${TIZEN_DIR}
        PERMISSIONS OWNER_READ
                    GROUP_READ
                    WORLD_READ)

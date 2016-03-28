INSTALL(FILES 
        ${CMAKE_CURRENT_SOURCE_DIR}/tizen_store_public.pem
        ${CMAKE_CURRENT_SOURCE_DIR}/tizen_store_platform.pem
        ${CMAKE_CURRENT_SOURCE_DIR}/tizen_store_partner.pem
        DESTINATION ${TIZEN_DIR}
        PERMISSIONS OWNER_READ
                    GROUP_READ
                    WORLD_READ)

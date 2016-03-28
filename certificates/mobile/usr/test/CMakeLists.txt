INSTALL(FILES 
        ${CMAKE_CURRENT_SOURCE_DIR}/tizen_association_dev_public.pem
        ${CMAKE_CURRENT_SOURCE_DIR}/tizen_association_dev_platform.pem
        ${CMAKE_CURRENT_SOURCE_DIR}/tizen_association_dev_partner.pem
        DESTINATION ${TIZEN_DIR}
        PERMISSIONS OWNER_READ
                    GROUP_READ
                    WORLD_READ)

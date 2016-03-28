INSTALL(FILES 
        ${CMAKE_CURRENT_SOURCE_DIR}/tizen_association_dev_partner.pem
        ${CMAKE_CURRENT_SOURCE_DIR}/tizen-distributor-root-ca-partner.pem
        ${CMAKE_CURRENT_SOURCE_DIR}/tizen-partner-class-developer-root.pem
        ${CMAKE_CURRENT_SOURCE_DIR}/tizen_store_partner.pem
        ${CMAKE_CURRENT_SOURCE_DIR}/tizen_store_test_partner.pem
        DESTINATION ${TIZEN_DIR}
        PERMISSIONS OWNER_READ
                    GROUP_READ
                    WORLD_READ)

INSTALL(FILES 
        ${CMAKE_CURRENT_SOURCE_DIR}/tizen_association_dev_public.pem
        ${CMAKE_CURRENT_SOURCE_DIR}/tizen-distributor-root-ca-public.pem
        ${CMAKE_CURRENT_SOURCE_DIR}/tizen-public-class-developer-root.pem
        ${CMAKE_CURRENT_SOURCE_DIR}/tizen_store_public.pem
        ${CMAKE_CURRENT_SOURCE_DIR}/tizen_store_test_public.pem
        DESTINATION ${TIZEN_DIR}
        PERMISSIONS OWNER_READ
                    GROUP_READ
                    WORLD_READ)

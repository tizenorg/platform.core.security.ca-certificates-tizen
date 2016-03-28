INSTALL(FILES 
        ${CMAKE_CURRENT_SOURCE_DIR}/tizen-developer-root-ca.pem
        ${CMAKE_CURRENT_SOURCE_DIR}/Tizen_Developers_Root_Class.pem
        ${CMAKE_CURRENT_SOURCE_DIR}/tizen-developers-root.pem
        DESTINATION ${TIZEN_DIR}
        PERMISSIONS OWNER_READ
                    GROUP_READ
                    WORLD_READ)

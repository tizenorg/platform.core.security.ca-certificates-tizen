MESSAGE("Release mode : ${RELMODE}")
MESSAGE("Copying ${RELMODE} root CA certificates")

ADD_SUBDIRECTORY(${RELMODE})

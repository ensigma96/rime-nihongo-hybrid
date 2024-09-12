#!/bin/bash

readonly JMDICT_E_URI='ftp://ftp.edrdg.org/pub/Nihongo//JMdict_e.gz'
readonly DIR=`pwd`
readonly JMDICT_DIR="${DIR}/data/JMdict"
readonly JMDICT_E="${JMDICT_DIR}/JMdict_e.xml"

wget -O - "${JMDICT_E_URI}" | gzip -d > "${JMDICT_E}"

#!/bin/bash
cp platina_sdk/pcc_api.py platina_sdk/pcc_api.py.original
cat internal/pcc_sdk_internal.py >> platina_sdk/pcc_api.py
./build-sdk.sh
mv -f platina_sdk/pcc_api.py.original platina_sdk/pcc_api.py

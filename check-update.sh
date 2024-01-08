#!/bin/sh
curl -L "https://www.rfdump.org/hw.shtml" 2>/dev/null |sed -ne 's,.*RFDump V\(.*\) Sources.*,\1,p' |head -n1


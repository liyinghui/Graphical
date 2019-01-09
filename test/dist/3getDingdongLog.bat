
chcp 65001

if "%time:~0,2%" lss "10" (set "hms=0%time:~1,1%%time:~3,2%%time:~6,2%") else    (set "hms=%time:~0,2%%time:~3,2%%time:~6,2%")

set dt=dingdong_%hms%


adb pull /tmp/dingdong.log  C:/Users/liyinghui3/Desktop/%dt%.log

pause
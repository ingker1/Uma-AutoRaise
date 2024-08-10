cd adb
adb shell wm size 1080x2280
adb shell wm density 420
cd ..
adb shell am start com.komoe.kmumamusumegp/jp.co.cygames.umamusume_activity.UmamusumeActivity
python start.py
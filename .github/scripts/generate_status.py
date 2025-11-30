from datetime import datetime, timedelta
import re

now_utc = datetime.utcnow()
JST_OFFSET_HOURS = 9
now_jst = now_utc + timedelta(hours=JST_OFFSET_HOURS)

hour = now_jst.hour
minute = now_jst.minute
day = now_jst.day

status = ""
total_minutes = hour * 60 + minute

if total_minutes >= 5 * 60 and total_minutes < 9 * 60 + 30:
    status = "☀️ 早朝起動: システムチェックと日次タスク準備中"

elif total_minutes >= 9 * 60 + 30 and total_minutes < 15 * 60:
    status = "🌤 ピーク稼働中: 集中して開発とコンパイルを行っています"

elif total_minutes >= 15 * 60 and total_minutes < 18 * 60:
    status = "🌆 クールダウン: 一日の成果を確認し、ログを整理中"

elif total_minutes >= 18 * 60 and total_minutes < 24 * 60:
    status = "🌙 最終調整: プッシュ前の確認作業中"
    
else:
    status = "🌑 深夜の指示: 指示に従ってコードが稼働中"

status += f" | {day} 日目のログ"

with open("README.md", "r", encoding="utf-8") as f:
    content = f.read()

pattern = r"<!--STATUS-->.*?<!--/STATUS-->"
replacement = f"<!--STATUS-->\n{status}\n<!--/STATUS-->"

if re.search(pattern, content, re.DOTALL):
    new_content = re.sub(pattern, replacement, content, 1, re.DOTALL)
else:
    new_content = content.replace("<!--STATUS-->", f"<!--STATUS-->\n{status}\n<!--/STATUS-->")
    
with open("README.md", "w", encoding="utf-8") as f:
    f.write(new_content)


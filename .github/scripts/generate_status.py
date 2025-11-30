from datetime import datetime, timedelta
import re

now_utc = datetime.utcnow()
JST_OFFSET_HOURS = 9
now_jst = now_utc + timedelta(hours=JST_OFFSET_HOURS)

hour = now_jst.hour
day = now_jst.day

if 5 <= hour < 12:
    status = "☀️ 朝: システム起動中… 実験開始"
elif 12 <= hour < 18:
    status = "🌤 昼: ツールコンパイル中、混乱管理"
elif 18 <= hour < 24:
    status = "🌙 夜: 静かに調整中"
else:
    status = "🌑 深夜: 不安定コード稼働中"

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


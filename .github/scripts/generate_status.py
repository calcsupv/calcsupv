from datetime import datetime, timedelta
import re
import random
import json
import os

now_utc = datetime.utcnow()
JST_OFFSET_HOURS = 9
now_jst = now_utc + timedelta(hours=JST_OFFSET_HOURS)

hour = now_jst.hour
minute = now_jst.minute
day = now_jst.day

time_key_en = ""
total_minutes = hour * 60 + minute

if total_minutes >= 5 * 60 and total_minutes < 9 * 60 + 30:
    time_key_en = "morning"

elif total_minutes >= 9 * 60 + 30 and total_minutes < 15 * 60:
    time_key_en = "daytime"

elif total_minutes >= 15 * 60 and total_minutes < 18 * 60:
    time_key_en = "evening"

elif total_minutes >= 18 * 60 and total_minutes < 24 * 60:
    time_key_en = "night"

else:
    time_key_en = "midnight"

messages = {}
message_filepath = "./.github/scripts/messages.json"

error_msg = " エラー: JSONファイルが見つからないため、ステータスの自動更新が停止しています。"

try:
    with open(message_filepath, "r", encoding="utf-8") as f:
        messages = json.load(f)
except Exception as e:
    messages["morning"] = [error_msg]
    messages["daytime"] = [error_msg]
    messages["evening"] = [error_msg]
    messages["night"] = [error_msg]
    messages["midnight"] = [error_msg]
    
if time_key_en in messages and messages[time_key_en]:
    status_message = random.choice(messages[time_key_en])
else:
    status_message = f" エラー: {time_key_en} のメッセージがJSONに見つかりません"

status = f"{status_message} | {day} 日目のログ"

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


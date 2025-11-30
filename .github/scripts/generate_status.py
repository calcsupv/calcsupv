from datetime import datetime

# 現在の時間と日付
now = datetime.now()
hour = now.hour
day = now.day

# 時間帯による文章
if 5 <= hour < 12:
    status = "☀️ 朝: システム起動中… 実験開始"
elif 12 <= hour < 18:
    status = "🌤 昼: ツールコンパイル中、混乱管理"
elif 18 <= hour < 24:
    status = "🌙 夜: 静かに調整中"
else:
    status = "🌑 深夜: 不安定コード稼働中"

# 日ごとに少し変化
status += f" | {day} 日目のログ"

# README の置換
with open("README.md", "r", encoding="utf-8") as f:
    content = f.read()

new_content = content.replace("<!--STATUS-->", status)

with open("README.md", "w", encoding="utf-8") as f:
    f.write(new_content)

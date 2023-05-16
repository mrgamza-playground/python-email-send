import smtplib
from email.mime.text import MIMEText

sender = '지메일 계정'
receiver = '수신자 이메일'
password = '지메일 앱 비밀번호'

# 세션 생성
s = smtplib.SMTP('smtp.gmail.com', 587)

# TLS 보안 시작
s.starttls()

# 로그인 인증
s.login(sender, password)

# 보낼 메시지 설정
msg = MIMEText('본문')
msg['Subject'] = '제목'

# 메일 보내기
s.sendmail(sender, receiver, msg.as_string())

# 세션 종료
s.quit()

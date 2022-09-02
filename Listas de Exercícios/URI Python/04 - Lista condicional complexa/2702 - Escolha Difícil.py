Ca, Ba, Pa =map(int, input().split())
Cr, Br, Pr =map(int, input().split())
total=0
if Cr>Ca:
    total=total+(Cr-Ca)
if Br>Ba:
    total=total+(Br-Ba)
if Pr>Pa:
    total=total+(Pr-Pa)
print(total)

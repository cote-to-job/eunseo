def solution(video_len, pos, op_start, op_end, commands):
    str_to_int = [video_len,pos,op_start,op_end]
    already = []
    for change in str_to_int:
        temp = change.split(':')
        already.append(60*int(temp[0])+int(temp[1]))
    video_len, pos, op_start, op_end = already
    for user in commands:
        if op_start <= pos <= op_end:
            pos = op_end
        if user == 'next':
            pos += 10
            if pos > video_len: pos = video_len
        elif user == 'prev':
            pos -= 10
            if pos < 0: pos = 0
        if op_start <= pos <= op_end:
            pos = op_end
    m = str(pos//60)
    s = str(pos%60)
    if len(s) == 1: s = '0'+s
    if len(m) == 1: m = '0' + m
    return m + ':' + s
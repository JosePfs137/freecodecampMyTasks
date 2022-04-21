def add_time(h1, h2, d = None):
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    prH = []
    prM = []
    data = h1.split()
    hm1 = data[0].split(':')
    h1 = int(hm1[0])
    m1 = int(hm1[1])

    if d is not None:
        da = d.lower()
        da = da[0].upper() + da.strip(da[0])

    if h1 > 12:
        time = 'AM'
    else:
        time = data[1]

    hm2 = h2.split(':')
    h2 = int(hm2[0])
    m2 = int(hm2[1])

    h1_m = h1 * 60
    h2_m = h2 * 60

    if time == 'AM':
        m_sum = h1_m + h2_m + m1 + m2
    elif time == 'PM':
        m_sum = h1_m + h2_m + m1 + m2 + 12*60
    else:
        print('I think you forgot the AM/PM')
        quit()

    dR = m_sum // ( 24 * 60)
    m_sum = m_sum - dR*24*60

    if d is not None and da in days:
        i = 0
        for day in days:
            if da == day:
                break
            i = i + 1
        R = dR + i
        if R > 6: R = R % 6 - 1
        DR = days[R]

    d_t = m_sum // ( 12 * 60)


    m_sum = m_sum - d_t * 12 * 60
    h = m_sum // 60
    m = m_sum - h * 60

    if d_t == 1:
        timeR = 'PM'
    else:
        timeR = 'AM'
    pH = [h1, h2, h]
    pM = [m1, m2, m]

    if h1 > 12:
        time = ''
    count = 0
    for j in pH:
        count = count + 1
        if j == 0 and count != 2:
            h = '12'
            prH.append(h)
            continue
        h = str(j)
        if len(h) == 1:
            h = '0' + h
        prH.append(h)
    for n in pM:
        k = str(n)
        if len(k) == 1:
            k = '0' + k
        prM.append(k)

    #print(prH, prM)
    if d is not None:
        print('{}:{} {} at {} + {}:{}'.format(prH[0], prM[0], time, d, prH[1], prM[1]))
        if dR == 1:
            print('Returns: {}:{} {} {} (next day)'.format(prH[2], prM[2], timeR, DR))
        if dR < 1:
            print('Returns: {}:{} {} {}'.format(prH[2], prM[2], timeR, DR))
        else:
            print('Returns: {}:{} {} {} ({} days later)'.format(prH[2], prM[2], timeR, DR, dR))
    elif dR == 1:
        print('{}:{} {} + {}:{}'.format(prH[0], prM[0], time, prH[1], prM[1]))
        print('Returns: {}:{} {} (next day)'.format(prH[2], prM[2], timeR))
    elif dR > 1:
        print('{}:{} {} + {}:{}'.format(prH[0], prM[0], time, prH[1], prM[1]))
        print('Returns: {}:{} {} ({} days later)'.format(prH[2], prM[2], timeR, dR))
    else:
        print('{}:{} {} + {}:{}'.format(prH[0], prM[0], time, prH[1], prM[1]))
        print('Returns: {}:{} {}'.format(prH[2], prM[2], timeR))

add_time("3:00 PM", "3:10")
add_time("11:30 AM", "2:32", "Monday")
add_time("11:43 AM", "00:20")
add_time("10:10 PM", "3:30")
add_time("11:43 PM", "24:20", "tueSday")
add_time("6:30 PM", "205:12")
add_time('13:00', '1:10', 'Sunday')

def cal(d, m, y):
    m_30d = [4, 6, 9, 11]
    m_31d = [1, 3, 5, 7, 8, 10, 12]
    if 0 < d <= 31 and m in m_31d:
        return True
    if 0 < d <= 30 and m in m_30d:
        return True
    if m == 2:
        if y % 100 != 0 and y % 4 == 0 or y % 100 == 0 and y % 400 == 0:
            if 0 < d <= 29:
                return True
        if 0 < d <= 28:
            return True
    return False

'''
#연습
ko, en, ma, sc = 100, 86, 81, 91

def get_max_score(*args):
    return max(args)

max_score = get_max_score(ko, en, ma, sc)
print('높은 점수:', max_score)
max_score = get_max_score(en, sc)
print('높은 점수:', max_score)
'''

#심사
ko, en, ma, sc = map(int, input().split())
def get_min_max_score(*kwargs):
    min_score = min(kwargs)
    max_score = max(kwargs)
    return min_score, max_score

def get_avg(**kwargs):
    return sum(kwargs.values())/len(kwargs.keys())

min_score, max_score = get_min_max_score(ko, en, ma, sc)
avg_score = get_avg(ko=ko, en=en, ma=ma, sc=sc)
print('낮은 점수:{0:.2f}, 높은 점수:{1:.2f}, 평균점수: {2:.2f}'.format(min_score, max_score, avg_score))

min_score, max_score = get_min_max_score(en, sc)
avg_score = get_avg(en=en, sc=sc)
print('낮은 점수:{0:.2f}, 높은 점수:{1:.2f}, 평균점수: {2:.2f}'.format(min_score, max_score, avg_score))

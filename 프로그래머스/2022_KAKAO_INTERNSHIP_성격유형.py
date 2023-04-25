dct = {1: 7, 2: 6, 3: 5, 4: 4, 5: 3, 6: 2, 7: 1}
result = {'A': 0, 'N': 0, 'J': 0, 'M': 0, 'C': 0, 'F': 0, 'R': 0, 'T': 0}
score = [0, 3, 2, 1, 0, 1, 2, 3]


def solution(survey, choices):
    answer = ''

    for i in range(len(survey)):
        if survey[i][0] > survey[i][1]:
            survey[i] = survey[i][1] + survey[i][0]
            choices[i] = dct[choices[i]]

    for j in range(len(survey)):
        if choices[j] > 4:
            result[survey[j][1]] += score[choices[j]]
        else:
            result[survey[j][0]] += score[choices[j]]

    for k in range(4):
        if k == 0:
            if result['R'] >= result['T']:
                answer += 'R'
            else:
                answer += 'T'
        if k == 1:
            if result['C'] >= result['F']:
                answer += 'C'
            else:
                answer += 'F'
        if k == 2:
            if result['J'] >= result['M']:
                answer += 'J'
            else:
                answer += 'M'
        if k == 3:
            if result['A'] >= result['N']:
                answer += 'A'
            else:
                answer += 'N'

    return answer
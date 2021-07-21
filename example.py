def solution(people, limit):
    answer = 0
    people.sort()
    while people:
        boat=[]
        boat.append(people[-1])
        people.pop()
        while True:
            boat_people = 0
            for b in boat:
                boat_people += b
            rest_limit = limit - boat_people
            if rest_limit<40 or people == []:
                answer+=1
                break
            if people == True and rest_limit>=people[-1]:
                boat.append(people[-1])
                people.pop()
                continue
            first = 0
            final = len(people)
            while True:
                middle = int((first+final)/2)+1
                if middle < len(people)+1:
                    boat.append(people[0])
                    people.pop()

                    break
                if people[middle]>rest_limit:
                    final = middle
                elif people[middle]>rest_limit:
                    first = middle
                else:
                    boat.append(people[middle])
                    people.pop(middle)

                    break
        
    return answer

people = [70, 80, 50]
limit = 100
print(solution(people, limit))
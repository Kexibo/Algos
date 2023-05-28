#Сложность O(n)
def twoCitySchedCost(costs):
        #Переменная для общей суммы
        sum = 0
        #Отправляем всех в город А
        for cost_a, cost_b in costs:
            sum += cost_a
        #Сортируем список так чтобы все люди которым в город а дороже были в первой половине
        costs.sort(key = lambda x : x[1] - x[0])
        #Проходим по той части где в город В дешевле 
        for i in range(len(costs)//2):
            cost_a, cost_b = costs[i]
            sum += cost_b - cost_a

        return sum

#twoCitySchedCost([[10,20],[30,200],[400,50],[30,20]])
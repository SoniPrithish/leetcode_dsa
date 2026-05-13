class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        ss=set(supplies)
        q=deque()
        adjm=defaultdict(set)
        adjj=defaultdict(list)
        for i,recipe in enumerate(recipes):
            ing_reqd=set(ingredients[i])
            ct_reqd=len(ing_reqd)
            ct=0
            for ing in ing_reqd:
                if ing in ss:
                    ct+=1
                else:
                    adjm[recipe].add(ing)
                    adjj[ing].append(recipe)
            if ct==ct_reqd:
                    q.append(recipe)
        result=[]
        while q:
            new_supply=q.pop()
            result.append(new_supply)
            ss.add(new_supply)
            for recipe in adjj[new_supply]:
                adjm[recipe].remove(new_supply)
                if not adjm[recipe]:
                    q.append(recipe)

        return result

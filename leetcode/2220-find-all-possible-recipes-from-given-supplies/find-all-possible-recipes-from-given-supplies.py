class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        """
            yeast -> bread
            flour -> bread
            bread -> sandwich
            meat -> sandwich

            {
                bread: 2,
                sandwich: 2
            }
        """
        adj_list = defaultdict(list)
        edge_count = defaultdict(int)

        for rec, ing in zip(recipes, ingredients):
            edge_count[rec] += len(ing)
            for i in ing:
                adj_list[i].append(rec)
    
        ans = []
        q = deque(supplies)
        recipes = set(recipes)
        while q:
            ing = q.popleft()
            if ing in recipes:
                ans.append(ing)

            for rec in adj_list[ing]:
                edge_count[rec] -= 1
                if edge_count[rec] == 0:
                    q.append(rec)
        return ans

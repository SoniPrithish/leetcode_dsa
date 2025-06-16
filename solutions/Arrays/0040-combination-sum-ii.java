class Solution {
    public List<List<Integer>> combinationSum2(int[] candidates, int target) {
        List<List<Integer>> result =new ArrayList<>();
        Arrays.sort(candidates);
        makeCombination(candidates,target,0,new ArrayList<>(),result);
        return result;
    }
    private void makeCombination(int[] candidates,int target,int index, List<Integer> combination,List<List<Integer>> result)
    {   
        
        if(target==0)
        {
            result.add(new ArrayList<>(combination));
            return;
        }
       
        
        for(int i=index; i<candidates.length; i++)
        {
            if(i>index && candidates[i]==candidates[i-1])
            {
                continue;
            }
            if(candidates[i]>target)
            {
                break;
            }
            combination.add(candidates[i]);

            makeCombination(candidates,target-candidates[i],i+1,combination,result);

            combination.remove(combination.size()-1);
        }
    }
}

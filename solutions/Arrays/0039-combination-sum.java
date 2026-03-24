class Solution {
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        List<List<Integer>> result =new ArrayList<>();

        makeCombination(candidates,target,0,new ArrayList<>(),0,result);
        return result;
    }
    private void makeCombination(int[] candidates, int target, int index, List<Integer> combination,int total,List<List<Integer>> result)
    {
        if (total ==target)
        {   
            result.add(new ArrayList<>(combination));
            return ;
        }
        if(total >target || index>= candidates.length)
        {
            return;
        }
        combination.add(candidates[index]);
        makeCombination(candidates,target,index,combination,total+candidates[index],result);
        combination.remove(combination.size()-1);
        makeCombination(candidates,target,index+1,combination,total,result);
    }
}

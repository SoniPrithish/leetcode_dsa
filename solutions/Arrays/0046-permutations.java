class Solution {
    public List<List<Integer>> permute(int[] nums) {
       List<List<Integer>> result=new ArrayList<>();
       allpermutation(nums,new ArrayList<>(),result);
       return result; 
    }
    private void allpermutation(int[] nums,List<Integer> current,List<List<Integer>> result)
    {
        if(current.size()==nums.length)
        {
            result.add(new ArrayList<>(current));
            return;
        }
        for(int i:nums)
        {
            if(current.contains(i)){continue;}
            current.add(i);
            allpermutation(nums,current,result);
            current.remove(current.size()-1);
        }
    }
}

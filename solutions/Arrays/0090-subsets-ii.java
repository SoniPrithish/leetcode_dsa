class Solution {
    public List<List<Integer>> subsetsWithDup(int[] nums) {
        List<List<Integer>> list= new ArrayList<>();

        Arrays.sort(nums);
        recursion(nums,0,new ArrayList<>(),list);

        return list;
    }

    void recursion(int[] nums, int start, List<Integer> path, List<List<Integer>> list)
    {
        list.add(new ArrayList<>(path));


        for(int i=start; i<nums.length; i++)
        {
            if(i>start && nums[i]==nums[i-1])
            {
                continue;
            }

            path.add(nums[i]);

            recursion(nums,i+1,path,list);

            path.remove(path.size()-1);
        }
    }
}

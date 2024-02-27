def permutations(nums):
    main_array = []

    if len(nums)==1:
        return [nums[:]]

    for i in range(len(nums)):
        n = nums.pop(0)
        res = permutations(nums)
        for r in res:
            r.append(n)
        main_array.extend(res)
        nums.append(n)
    return main_array


print(permutations([1,2,3,4]))
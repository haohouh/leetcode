nums = [1,3,4,4,6,8]
l = 0
r = 3
while l <= r:
  mid = l + (r-l) // 2
  if nums[mid] >= 4:
      r = mid - 1
  else:
      l = mid + 1
print(l)
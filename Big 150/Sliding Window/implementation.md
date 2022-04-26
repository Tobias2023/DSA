# How-to Guide/Resources 

* [How to implement guide](https://stackoverflow.com/questions/8269916/what-is-sliding-window-algorithm-examples?msclkid=915742d1c0bd11ec8e47a978392db6b0)
* [How to guide](https://www.pluralsight.com/guides/algorithm-templates:-two-pointers-part-3) 

### Visual

`[a b c d e f g h]`

```html
[a b c]
  [b c d]
    [c d e]
      [d e f]
        [e f g]
          [f g h]
```

### Template

```
# start & end of sliding window: |start-> ... end->|
# short version of sliding window, focus on two pointers
def start_end_sliding_window(self, seq):
    start, end = 0, 0
    while end < len(seq):
        # end pointer grows in the outer loop
        end += 1
        
        # start pointer grows with some restrict
        while self.start_condition(start):
            # process logic before pointers movement
            self.process_logic1(start, end)
            # start grows in the inner loop
            start += 1
            
        # or process logic after pointers movement
        self.process_logic2(start, end)

```

### More specific template

```

# more specific version of sliding window
# s - source sequence, p - pattern or restrict sequence
def sliding_window_template_with_examples(s, p):
    # initialize the hash map
    # counter is used to record current state, usually use Counter or defaultdict
    counter = Counter(p)
    # two pointers, boundary of sliding window
    start, end = 0, 0
    # condition checker, update it when trigger some key changes
    # the initial value depend on your situation
    count = 0
    # result, return int (such as max or min) or list (such as all index)
    res = 0

    # loop the source sequence from begin to end
    while end < len(s):
        counter[s[end]] += 1
        # update count based on some condition
        if counter[s[end]] > 1:
            count += 1
        # end pointer grows in the outer loop    
        end += 1

        # count condition, the condition may be different
        while count > 0:
            '''
            update res here if finding minimum
            '''
            # increase start pointer to make it invalid or valid again
            counter[s[start]] -= 1
            # update count based on some condition
            if counter[s[start]] > 0:
                count -= 1
            # start pointer grows in the inner loop
            start += 1
        '''
        update res here if finding maximum
        '''
        # the result logic may be different
        res = max(res, end - start)
    return res

```
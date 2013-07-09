def PermuteString(string):
     if not string:
             return ['']
     ret = []
     for i, d in enumerate(string):
             perms = PermuteString(string[:i] + string[i+1:])
             for perm in perms:
                     ret.append(d + perm)
     return ret

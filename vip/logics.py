

def need_perm(perm_name):
    '''检查用户是否具有某种权限'''
    def deco(view_func):
        def wrap(request, *args, **kwargs):
            # 先获取当前用户
            # perm in user.vip.perms


            return response
        return wrap
    return deco

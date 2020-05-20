class ResourceScopeManager():
    def __init__(self):
        '''
        The global scope is always available
        You can access the current scope in the scope list
        '''
        self.global_scope = dict()
        self.scopes = []
        #-1 means we currently have no scope
        self.scope_level = -1

    def get_variable(self, name):
        '''
        Checks the scope and returns the var from there
        Defaults to 0
        '''
        scoped = self.get_scoped_vars()
        if name in scoped.keys():
            return scoped[name]
        else:
            return 0

    def set_variable(self, name, value):
        if self.scope_level == -1:
            self.global_scope[name] = value
        else:
            self.get_current_scope()[name] = value

    def get_scoped_vars(self):
        '''
        returns the global and current scope merged, with precedence to the local scope
        '''
        current_scope = self.get_current_scope()
        global_scope = self.global_scope

        merged_scope = global_scope.copy()
        for key in current_scope.keys():
            merged_scope[key] = current_scope[key]

        return merged_scope

    def del_variable(self, name):
        if name in self.get_current_scope():
            self.get_current_scope().pop(name)
        elif name in self.global_scope:
            self.global_scope.pop(name)

    def get_global_vars(self):
        return self.global_scope

    def get_current_scope(self) -> dict:
        return self.scopes[self.scope_level] if self.scope_level > -1 else dict()

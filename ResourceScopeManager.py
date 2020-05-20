class ResourceScopeManager():
    def __init__(self, max_scopes=64):
        '''
        The global scope is always available
        You can access the current scope in the scope list
        '''
        self.global_scope = dict()
        self.scopes = []
        #-1 means we currently have no scope
        self.scope_level = -1
        self.max_scopes = max_scopes

    def get_variable(self, name:str):
        '''
        Checks the scope and returns the var from there
        Defaults to 0
        '''
        scoped = self.get_scoped_vars()
        if name in scoped.keys():
            return scoped[name]
        else:
            return None

    def set_variable(self, name:str, value)->None:
        if self.scope_level == -1:
            self.global_scope[name] = value
        else:
            self.get_current_scope()[name] = value

    def get_scoped_vars(self)->dict:
        '''
        returns the global and current scope merged, with precedence to the local scope
        '''
        current_scope = self.get_current_scope()
        global_scope = self.global_scope

        merged_scope = global_scope.copy()
        for key in current_scope.keys():
            merged_scope[key] = current_scope[key]

        return merged_scope

    def del_variable(self, name:str)->None:
        if name in self.get_current_scope():
            self.get_current_scope().pop(name)
        elif name in self.global_scope:
            self.global_scope.pop(name)

    def get_global_vars(self)->dict:
        return self.global_scope

    def get_current_scope(self) -> dict:
        return self.scopes[self.scope_level] if self.scope_level > -1 else dict()

    def inc_scope(self)->None:
        #Set recursion limit
        if len(self.scopes) > self.max_scopes:
            raise RecursionError("The program reached max recursion")
        self.scopes.append(dict())
        self.scope_level += 1

    def dec_scope(self)->None:
        self.scopes.pop()
        self.scope_level -= 1

    def is_variable(self, name)->bool:
        '''
        returns wheather the variable exists or not
        '''
        return name in self.get_scoped_vars().keys()

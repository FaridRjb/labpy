import sympy as sp


def err_func(f, err_vars):
    '''
    Parameters
    ----------
    f : sympy expression
        Function f(x) that its error function is to be calculated.
    variables : array_like
        All variables in f(x) as sympy.Symbol.
    err_vars : array_like
        All variables that have error in f(x) as sympy.Symbol.
    
    Returns
    -------
    error : sympy.expression
        Error function
    vars_ : array_like
        List of sympy.Symbol s that have error. Use them to substitute their value.
    '''
    import sympy as sp
    
    vars_ = []
    for var in err_vars:
        var = sp.Symbol('\Delta{' + var.name + '}')
        vars_.append(var)
    print(vars_)
    
    ln_f = sp.ln(f)
    res, error = 0, 0
    for var_i, var in enumerate(err_vars):
        df_var = sp.diff(ln_f, var) * vars_[var_i]
        res += sp.apart(df_var, var)
    for term in res.args:
        error += abs(term)
    
    error *= abs(f)
    return error, vars_